Kinescope-Master 2.0 (Windows)
Бот, генерирующий команду для скачивания видео:
@Kinescope_Downloader_New_bot
Поддержка:
Если у тебя возникнут вопросы или проблемы, обратись в поддержку:
@Kinescope_Downloader
=================================================================
Инструкция по использованию Kinescope-Master 2.0 (Windows)
📌 Оглавление
1. Введение
2. Что вам понадобится
3. Установка программы
4. Работа с Telegram-ботом
5. Скачивание видео
=================================================================
1. Введение
Kinescope-Master — это специализированный инструмент для быстрого и удобного скачивания видео с платформы Kinescope.io. Программа разработана для пользователей любого уровня подготовки — от новичков до профессионалов.
🔹 Основные возможности
✅ Простота использования
Не требует технических знаний
Работает в 1 клик после настройки
✅ Поддержка разных форматов
Скачивание в MP4 (стандартное качество)
Опция --best-quality для максимального разрешения
✅ Гибкие настройки
Возможность выбора пути сохранения
Автоматическое именование файлов
✅ Безопасность
Локальная обработка данных
Не требует доступа к вашим аккаунтам
✅ Анонимность скачивания
Автор видео не получит уведомлений о том, что его контент был загружен.
Kinescope-Master не оставляет следов в системе Kinescope.
✅ Локальная обработка
Все операции выполняются на вашем устройстве без передачи данных на сторонние серверы.
Исходные файлы (JSON) автоматически удаляются с сервера после обработки.
✅ Защита пользователя
Не требует ввода логинов/паролей от Kinescope.
Не использует cookies или другие методы отслеживания.
=================================================================
🛠 2. Что вам понадобится
- Компьютер с Windows 10/11
- Доступ к Telegram (для работы с ботом)
- 5-10 минут свободного времени
=================================================================
⚙️ 3. Установка программы
Шаг 1: Скачивание архива
1. Перейдите по ссылке для скачивания
2. Сохраните архив `kinescope-master 2.0.zip` на компьютер
Шаг 2: Распаковка
1. Нажмите правой кнопкой мыши на скачанный архив
2. Выберите "Извлечь в kinescope-master 2.0"
3. Укажите путь для распаковки:
•	Можно выбрать любое удобное место на вашем компьютере
•	Рекомендуется использовать корень диска C: (C:\kinescope-master 2.0) для:
o	Простоты доступа
o	Минимизации проблем с правами доступа
o	Совместимости с инструкциями по установке
4. Нажмите "Извлечь"
=================================================================
🔧 4. Работа с Telegram-ботом
Шаг 1: Начало работы
1. Откройте Telegram и найдите бота: 
@Kinescope_Downloader_New_bot
2. Нажмите "Start" или отправьте команду `/start`
Шаг 2: Получение системного журнала:
1. Откройте видео на платформе Kinescope в браузере
2. Нажмите правой кнопкой мыши на видео
3. Выберите "Сохранить системный журнал"
4. Файл сохранится как `kinescope_player_log_xxxxxx.json`
Шаг 3: Отправка файла боту
1. Перетащите файл.json прямо в диалоговое окно с ботом
2. Дождитесь обработки (5-10 секунд)
     • В это время не закрывайте диалог
     • Дождитесь ответа от бота
Шаг 4: Получение команды
        Бот пришлет вам готовую команду вида:
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ & "bin\Python\python-3.11.9.amd64\python.exe" "kinescope-dl.py" -r "api_endpoint_url"  │
│ --best-quality --ffmpeg-path "bin\ffmpeg.exe" --mp4decrypt-path "bin\mp4decrypt.exe"   │
│ "kinescope_video_url" "output_filename.mp4"                                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
Где:
api_endpoint_url - адрес API-сервиса
kinescope_video_url - ссылка на видео в Kinescope
output_filename.mp4 - желаемое имя сохраняемого файла

Шаг 5: Обработка ошибок
Если бот ответит:
❌ «Не найдена валидная ссылка»
Это означает, что:
• Видео использует специальную систему защиты (DRM)
• Данный тип контента в настоящее время не поддерживается
===========================================================================
💾 5. Скачивание видео
Шаг 1: Открытие терминала
Перейдите в папку с распакованными файлами:
Если следовали рекомендации, то: C:\kinescope-master 2.0\
Если выбрали другое место: перейдите в вашу пользовательскую папку
o	Способ открытия терминала:
Нажмите правой кнопкой мыши на пустом месте в папке
Выберите "Открыть в Терминале" (Windows)
Шаг 2: Вставка команды
1. Скопируйте команду из Telegram
2. В терминале кликните правой кнопкой мыши для вставки
3. Нажмите Enter
Шаг 3: Ожидание завершения
Программа выполнит следующие действия автоматически:
1. Установит необходимые компоненты (при первом запуске)
2. Выберет лучшее качество видео
3. Скачает видео и аудио дорожки
4. Объединит их в один файл

Пример успешного завершения:
= DOWNLOADING =================
Video: 100% |██████████| [8/8]
Audio: 100% |██████████| [3/3]
[*] Decrypting... Done
[*] Merging tracks... Done

📁 Шаг 4: Готовый файл
Расположение файла:
По умолчанию: C:\kinescope-master 2.0\
Либо в выбранной вами папке при распаковке архива
Имя файла: соответствует указанному при запуске команды
Формат: .mp4 (например, Мое_Видео.mp4)


# Kinescope-Master 2.0 (Windows)
Bot generating download commands:
@Kinescope_Downloader_New_bot
Support:
If you have questions or issues, contact support:
@Kinescope_Downloader
=================================================================
User Manual for Kinescope-Master 2.0 (Windows)
📌 Table of Contents
1. Introduction
2. Requirements
3. Program Installation
4. Working with Telegram Bot
5. Downloading Videos
=================================================================
1. Introduction
Kinescope-Master is a specialized tool for quick and convenient video downloading from Kinescope.io. Designed for users of all levels - from beginners to professionals.
🔹 Key Features
✅ Easy to use
No technical knowledge required
One-click operation after setup
✅ Multiple format support
MP4 downloads (standard quality)
--best-quality option for maximum resolution
✅ Flexible settings
Custom save paths
Automatic file naming
✅ Security
Local data processing
No account access required
✅ Download anonymity
Video authors won't receive download notifications
Kinescope-Master leaves no traces in Kinescope system
✅ Local processing
All operations performed on your device
Source files (JSON) automatically deleted after processing
✅ User protection
No Kinescope logins/passwords required
No cookies or tracking methods used
=================================================================
🛠 2. Requirements
- Windows 10/11 computer
- Telegram access (for bot operation)
- 5-10 minutes of free time
=================================================================
⚙️ 3. Program Installation
Step 1: Downloading archive
1. Follow the download link
2. Save archive `kinescope-master 2.0.zip` to your computer
Step 2: Extraction
1. Right-click downloaded archive
2. Select "Extract to kinescope-master 2.0"
3. Choose extraction path:
• Any location on your computer
• Recommended: C: drive root (C:\kinescope-master 2.0) for:
o Easy access
o Minimal permission issues
o Compatibility with installation guide
4. Click "Extract"
=================================================================
🔧 4. Working with Telegram Bot
Step 1: Getting started
1. Open Telegram and find bot:
@Kinescope_Downloader_New_bot
2. Click "Start" or send `/start` command
Step 2: Getting system log:
1. Open video on Kinescope in browser
2. Right-click video
3. Select "Save system log"
4. File will save as `kinescope_player_log_xxxxxx.json`
Step 3: Sending file to bot
1. Drag-and-drop .json file into bot chat
2. Wait for processing (5-10 seconds)
• Keep chat open during this
• Wait for bot response
Step 4: Getting command
Bot will send ready command:
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ & "bin\Python\python-3.11.9.amd64\python.exe" "kinescope-dl.py" -r "api_endpoint_url" │
│ --best-quality --ffmpeg-path "bin\ffmpeg.exe" --mp4decrypt-path "bin\mp4decrypt.exe"  │
│ "kinescope_video_url" "output_filename.mp4"                                           │
└───────────────────────────────────────────────────────────────────────────────────────┘
Where:
api_endpoint_url - API service address
kinescope_video_url - Kinescope video link
output_filename.mp4 - desired output filename

Step 5: Error handling
If bot responds:
❌ "No valid link found"
This means:
• Video uses DRM protection
• This content type is currently unsupported
=================================================================
💾 5. Downloading Videos
Step 1: Opening Terminal
Navigate to extracted files:
Recommended path: C:\kinescope-master 2.0\
Custom path: Your chosen folder
o How to open terminal:
Right-click empty space in folder
Select "Open in Terminal" (Windows)
Step 2: Pasting command
1. Copy command from Telegram
2. Right-click in terminal to paste
3. Press Enter
Step 3: Completion
Program will automatically:
1. Install required components (first run only)
2. Select best video quality
3. Download video and audio tracks
4. Merge them into single file

Example output:
= DOWNLOADING =================
Video: 100% |██████████| [8/8]
Audio: 100% |██████████| [3/3]
[*] Decrypting... Done
[*] Merging tracks... Done

📁 Step 4: Output File
Location:
Default: C:\kinescope-master 2.0\
Or your chosen extraction folder
Filename: matches command specification
Format: .mp4 (e.g., My_Video.mp4)
