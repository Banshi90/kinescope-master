# ==================== ИМПОРТ БИБЛИОТЕК ====================
import os
import sys
import click
from urllib.parse import urlparse
from kinescope import KinescopeVideo, KinescopeDownloader
from pathlib import Path  # Для работы с путями

# ==================== НАСТРОЙКА ПУТЕЙ ====================
# Получаем путь к директории, где находится этот скрипт
BASE_DIR = Path(__file__).parent

# Пути к исполняемым файлам (относительные от расположения скрипта)
BIN_DIR = BASE_DIR / "bin"  # Папка с бинарными файлами
PYTHON_DIR = BIN_DIR / "Python" / "python-3.11.9.amd64"  # Папка Python
TEMP_DIR = BASE_DIR / "temp"  # Папка для временных файлов

# Пути к библиотекам и скриптам Python
LIB_PATH = PYTHON_DIR / "Lib"
SCRIPTS_PATH = PYTHON_DIR / "Scripts"

# Настройка переменных окружения
os.environ['PATH'] = str(PYTHON_DIR) + os.pathsep + str(SCRIPTS_PATH) + os.pathsep + os.environ.get('PATH', '')
sys.path.append(str(LIB_PATH))

# ==================== ОТЛАДОЧНАЯ ИНФОРМАЦИЯ ====================
# Вывод путей при первом запуске (для диагностики)
first_run_file = 'first_run.txt'
if not os.path.exists(first_run_file):
    print("BASE_DIR:", BASE_DIR)
    print("BIN_DIR:", BIN_DIR)
    print("PYTHON_DIR:", PYTHON_DIR)
    print("PATH:", os.environ['PATH'])
    with open(first_run_file, 'w') as f:
        f.write('This is the first run.')

# ==================== КЛАСС ДЛЯ ПРОВЕРКИ URL ====================
class URLType(click.ParamType):
    """Кастомный тип для валидации URL"""
    name = 'url'

    def convert(self, value, param, ctx):
        """Проверяет, является ли значение валидным URL"""
        try:
            parsed_url = urlparse(value)
            if parsed_url.scheme and parsed_url.netloc:
                return value
            else:
                self.fail(f'Expected valid url. Got {value}', param, ctx)
        except Exception as E:
            self.fail(f'Expected valid url. Got {value}: {E}', param, ctx)

# ==================== ОСНОВНАЯ ФУНКЦИЯ ====================
@click.command()
@click.option(
    '--referer', '-r',
    required=False, 
    help='Referer url of the site where the video is embedded', 
    type=URLType()
)
@click.option(
    '--best-quality',
    default=False, 
    required=False, 
    help='Automatically select the best possible quality', 
    is_flag=True
)
@click.option(
    '--temp',
    default=str(TEMP_DIR),  # Используем относительный путь
    required=False, 
    help='Path to directory for temporary files', 
    type=click.Path()
)
@click.argument('input_url', type=URLType())
@click.argument('output_file', type=click.Path())
@click.option(
    "--ffmpeg-path", 
    default=str(BIN_DIR / "ffmpeg.exe"),  # Относительный путь к ffmpeg
    required=False, 
    help='Path to ffmpeg executable', 
    type=click.Path()
)
@click.option(
    "--mp4decrypt-path", 
    default=str(BIN_DIR / "mp4decrypt.exe"),  # Относительный путь к mp4decrypt
    required=False, 
    help='Path to mp4decrypt executable', 
    type=click.Path()
)
def main(referer, best_quality, temp, input_url, output_file, ffmpeg_path, mp4decrypt_path):
    """
    Kinescope-dl: Video downloader for Kinescope

    \b
    <INPUT_URL> is url of the Kinescope video
    <OUTPUT_FILE> is path to the output mp4 file
    """
    # Создаем объект видео
    kinescope_video: KinescopeVideo = KinescopeVideo(
        url=input_url,
        referer_url=referer
    )

    # Создаем загрузчик с указанными путями
    downloader: KinescopeDownloader = KinescopeDownloader(
        kinescope_video,
        temp,
        ffmpeg_path=ffmpeg_path,
        mp4decrypt_path=mp4decrypt_path
    )

    # Выбор качества видео
    print('= OPTIONS ============================')
    video_resolutions = downloader.get_resolutions()
    if best_quality:
        chosen_resolution = video_resolutions[-1]  # Лучшее качество
    else:
        # Интерактивный выбор качества
        print('   '.join([f'{i + 1}) {r[1]}p' for i, r in enumerate(video_resolutions)]))
        chosen_resolution = video_resolutions[int(input('> Quality: ')) - 1]
    
    print(f'[*] {chosen_resolution[1]}p is selected')
    print('======================================')

    # Процесс загрузки
    print('\n= DOWNLOADING =================')
    downloader.download(
        output_file if output_file else f'{kinescope_video.video_id}.mp4',
        chosen_resolution
    )
    print('===============================')

# ==================== ЗАПУСК ПРОГРАММЫ ====================
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[*] Interrupted')
    except Exception as e:
        print(f'[!] Error: {str(e)}')