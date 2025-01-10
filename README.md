# Kinescope Master 2025

**Описание**  
Исходный материал для этого проекта был взят из [kinescope-dl](https://github.com/anijackich/kinescope-dl). 
Проект Kinescope Master 2025 предоставляет инструмент для скачивания видео с платформы Kinescope. 
Мы постарались сделать программу максимально простой, чтобы каждый, даже не имея опыта работы с подобными инструментами, смог её использовать.

**Подробная инструкция**  
Полную инструкцию по установке и работе с проектом можно найти в файле `Инструкция Kinescope Master 2025.pdf`. Ниже краткое изложение процесса.

### Скачивание видео с платформы Kinescope

Для скачивания видео с платформы Kinescope выполните следующие шаги:

1. **Скачайте архив с проектом.**  

2. **Распакуйте архив.**  
   Найдите загруженный файл и разархивируйте его. Переместите папку с проектом в корень диска C, чтобы путь к папке был:  
   `C:\kinescope-master`

3. **Получите команду для скачивания видео.**  
   Откройте видео на платформе Kinescope. Кликните правой кнопкой мыши по видео и выберите «Сохранить системный журнал».
   Файл будет сохранён с именем `kinescope_player_log_xxxxxxxxxxxxx.json`.  
   Отправьте этот JSON файл боту: [@Kinescope_Downloader_Video_bot](https://t.me/Kinescope_Downloader_Video_bot).
   Бот сгенерирует команду для скачивания видео, которая будет выглядеть примерно так:  
   
   & "C:\kinescope-master\bin\Python\python-3.11.9.amd64\python.exe" "C:\kinescope-master\kinescope-dl.py" -r "https://адрес_сайта" --best-quality --ffmpeg-path "C:\\kinescope-master\\bin\\ffmpeg.exe" --mp4decrypt-path "C:\\kinescope-master\\bin\\mp4decrypt.exe" "https://kinescope.io/id_видео" "название_видео.mp4"

4. **Установите все зависимости.**
Мы уже встроили Python в проект, так что вам не нужно устанавливать его отдельно.
Откройте папку C:\kinescope-master и в пустом месте внутри этой папки кликните правой кнопкой мыши, затем выберите «Открыть в терминале». Вставьте команду, полученную от бота, в терминал и нажмите Enter. Программа автоматически установит все необходимые библиотеки.

5. **Скачивание видео.**
После установки зависимостей начнется процесс скачивания видео с выбором самого высокого качества. Программа автоматически скачает видео и сохранит его в папке C:\kinescope-master.

**Поддержка**
Если у вас возникнут вопросы или проблемы, обратитесь в чат поддержки:
https://t.me/kinescope_downloader

**Бот для генерации команд для скачивания видео:**
https://t.me/Kinescope_Downloader_Video_bot
