import os
import sys
import click
from urllib.parse import urlparse
from kinescope import KinescopeVideo, KinescopeDownloader

# Путь к папке с распакованным Python (изменить на свою)
bin_path = r"C:\kinescope-master\bin\Python\python-3.11.9.amd64"

# Путь к папке с библиотеками
lib_path = os.path.join(bin_path, "Lib")

# Путь к папке со скриптами
scripts_path = os.path.join(bin_path, "Scripts")

# Добавляем все в переменную окружения PATH
os.environ['PATH'] = bin_path + os.pathsep + scripts_path + os.pathsep + os.environ.get('PATH', '')
sys.path.append(lib_path)

# Для отладки: выведем текущий путь только при первом запуске
first_run_file = 'first_run.txt'
if not os.path.exists(first_run_file):
    print("PATH:", os.environ['PATH'])
    with open(first_run_file, 'w') as f:
        f.write('This is the first run.')

class URLType(click.ParamType):
    name = 'url'

    def convert(self, value, param, ctx):
        try:
            parsed_url = urlparse(value)
            if parsed_url.scheme and parsed_url.netloc:
                return value
            else:
                self.fail(f'Expected valid url. Got {value}', param, ctx)
        except Exception as E:
            self.fail(f'Expected valid url. Got {value}: {E}', param, ctx)

@click.command()
@click.option(
    '--referer', '-r',
    required=False, help='Referer url of the site where the video is embedded', type=URLType()
)
@click.option(
    '--best-quality',
    default=False, required=False, help='Automatically select the best possible quality', is_flag=True
)
@click.option(
    '--temp',
    default=r'C:\kinescope-master\temp', required=False, help='Path to directory for temporary files', type=click.Path()
)
@click.argument('input_url', type=URLType())
@click.argument('output_file', type=click.Path())
@click.option("--ffmpeg-path", default=r'C:\kinescope-master\bin\ffmpeg.exe', required=False, help='Path to ffmpeg executable', type=click.Path())
@click.option("--mp4decrypt-path", default=r'C:\kinescope-master\bin\mp4decrypt.exe', required=False, help='Path to mp4decrypt executable', type=click.Path())
def main(referer,
         best_quality,
         temp, 
         input_url,
         output_file,
         ffmpeg_path,
         mp4decrypt_path):
    """
    Kinescope-dl: Video downloader for Kinescope

    \b
    <INPUT_URL> is url of the Kinescope video
    <OUTPUT_FILE> is path to the output mp4 file
    """

    kinescope_video: KinescopeVideo = KinescopeVideo(
        url=input_url,
        referer_url=referer
    )

    downloader: KinescopeDownloader = KinescopeDownloader(
        kinescope_video,
        temp,
        ffmpeg_path=ffmpeg_path,
        mp4decrypt_path=mp4decrypt_path
    )

    print('= OPTIONS ============================')
    video_resolutions = downloader.get_resolutions()
    chosen_resolution = video_resolutions[-1] if best_quality else video_resolutions[int(input(
        '   '.join([f'{i + 1}) {r[1]}p' for i, r in enumerate(video_resolutions)]) +
        '\n> Quality: '
    )) - 1]
    print(f'[*] {chosen_resolution[1]}p is selected')
    print('======================================')

    print('\n= DOWNLOADING =================')
    downloader.download(
        output_file if output_file else f'{kinescope_video.video_id}.mp4',
        chosen_resolution
    )
    print('===============================')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[*] Interrupted')
