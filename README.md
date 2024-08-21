# Telegram Chat Search Tool

## Описание

Эта программа предназначена для поиска ключевых слов внутри ваших чатов Telegram. Она предоставляет возможность быстро находить чаты, содержащие указанный вами ключ, и сохранять результаты поиска в файл для дальнейшего использования.

## Установка и настройка

### Требования для конфигурации

- Python 3.7 или выше
- Установленные библиотеки:
  - `pyinstaller`
  - `python-dotenv`
  - `telethon`

### Установка

- Клонируйте репозиторий:

  ```bash
  git clone https://github.com/memeLordo/telegram-chat-search.git
  cd telegram-chat-search-tool
  ```

- Скачайте архив
  ```sh
  wget https://github.com/memeLordo/where-is-coffee-script/archive/refs/heads/main.zip
  ```

## Использование программы

1. **Запуск исполняемого файла**

   После получения API ключей, вы можете запустить один из двух представленных исполняемых файлов программы, которые находится в папках, соответствующих поддерживаемым ими ОС.
   Название исполняемого файла: `ChatSearchTool`.

   - **Для Linux:** Откройте терминал, перейдите в папку `linux`, и выполните команду:

     ```bash
     ./ChatSearchTool
     ```

   - **Для Windows:** Откройте проводник, перейдите в папку `windows`, и дважды щелкните на файл `ChatSearchTool.exe`.

2. **Ввод API ID и API Hash**

   После запуска программы вам будет предложено ввести ваши API ID и API Hash, полученные на предыдущем этапе.

3. **Авторизация через номер телефона**

   Далее, введите ваш номер телефона. Telegram отправит вам код авторизации, который нужно ввести для завершения настройки.

4. **Поиск по чатам**

   В поле "Поиск:" введите ключевое слово или фразу, которую вы хотите найти в своих чатах.

5. **Получение результатов**

   Программа выведет ссылки на чаты, где встречается указанное ключевое слово.

6. **Сохранение результатов**

   По завершении поиска программа предложит вам сохранить результаты в файл. Созданные файлы будут расположены в созданной папке `./requests/`.

7. **Завершение работы**

   Если вы хотите выйти из программы, нажмите `Ctrl+C` в консоли. В противном случае, программа вернётся к шагу 4 и предложит выполнить новый поиск.

## Лицензия

Этот проект лицензируется на условиях MIT License.
