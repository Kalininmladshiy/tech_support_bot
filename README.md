# tech_support_bot
Данный репозиторий представляет собой три скрипта, два из которых боты поддержки для Телеграма и [VK](https://vk.com), которые используют
облачный сервис распознавания естественного языка от Google - Dialogflow. Третий, это скрипт для загрузки тренировочных фраз из .json файла.

## tech_support_bot.py
Это скрипт бота технической поддержки в телеграм.

## vk_bot.py
Это скрипт бота технической поддержки во Вконтакте.

## Установка:

### 1. Копируем содержимое проекта себе в рабочую директорию

### 2. Создаем проект в [Google](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

### 3. Создаем агента [Dialogflow](https://dialogflow.cloud.google.com/#/getStarted)

### 4. Создаем JSON-ключ:
```
gcloud auth application-default login
```
Необходимо будет перейти по ссылке в консоли, выбрать аккаунт и затем появившийся ключ скопировать в консоль.

### 5. Добавляем ваш Google проект в ключ:
```
gcloud auth application-default set-quota-project <YOUR_PROJECT>
```

### 6. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
В проекте используются следующие переменные окружения:  
`TG_BOT_TOKEN` - Телеграм токен. Его вы получите при регистрации бота  
`PROJECT_ID` - ID вашего проекта Google  
`VK_BOT_TOKEN` - VK токен бота. Его можно получить в настройках своего сообщества

### 7. Разворачиваем внутри скопированного проекта виртуальное окружение:
```
python -m venv <название виртуального окружения>
```

### 8. Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

### 9. Запускаем бота
```
python3 tech_support_bot.py
```

## download_phrase.py
Данный скрипт загружает фразы, которыми вы планируете обучать бота из .json файла по url. Пример данных:
```
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту прийдёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}
```
```
python download_phrase.py --url <https://адрес/с/вашим/файлом/с/фразы.json>
```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).
