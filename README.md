# LinkFixer_bot
Бот для нормального отображения превью в сообщениях со ссылками на такие сайты как:
- twitter.com
- x.com
- tiktok.com
- instagram.com*

*Facebook/Instagram — проект Meta Platforms Inc., деятельность которой в России запрещена

И добавляет префиксы, с которыми отображаются превью этих ссылок. Бот отвечает на сообщение пользователя, который прислал сообщение и тегает его по юзернейму.

```
Побочным эффектом превью Instagram является
возможность сохранять рилзы из превью.
```

## EN description
Bot for Telegram that fixes links for previews
- Bot searches for links on twitter.com, x.com and instagram.com and adds prefixes for in Telegram preview.
- Bot replies to that message and tags user by Telegram @username


### Технологии / Technologies
Python 3.11
Aiogram 3.1.1

### Бот запущен и доступен по ссылке / Bot deployed and available - https://t.me/ClippyRover_bot

## Создание бота в Telegram / Telegram Bot Creation

Как получить токен в BotFather:

- Отправьте в чат с BotFather команду /newbot.
- Введите название бота — в этой категории особых ограничений нет.
- Введите юзернейм бота — его техническое имя, которое будет отображаться в адресной строке. Юзернейм должен быть уникальным, написан на латинице и обязательно заканчиваться на bot. Так «Телеграм» защищается от злоумышленников, которые могут выдавать ботов за реальных людей.
- Готово. BotFather пришлет токен бота — его можно использовать для настройки в сторонних сервисах.

How to get a token in BotFather:

- Send to chat with the BotFather /newbot command.
- Enter the name of the bot - there are no special restrictions in this category.
- Enter the bot's username - its technical name, which will be in telegram user search. The username must be solid, written in Latin and must end in bot. This is how Telegram protects itself from attackers who can pretend to be bots.
- Ready. BotFather will send a bot token - it can be used to configure external services.


### Установка и запуск

**Клонируйте репозиторий:**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Rederickmind/LinkFixer_bot.git
```

```
cd LinkFixer_bot
```

**Установите и активируйте виртуальное окружение:**

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

**Обновите менеджер pip и установите зависимости**

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Необходимо заполнить env-файл для запуска
```
touch .env
```

Добавьте токен полученный от @BotFather в ваш .env файл / Put your token from @BotFather here

```
BOT_TOKEN='....'
```

### Запуск проекта:

**Локально:**

```
python main.py
```

**В Docker контейнере:**
```
docker compose up --build
```



- Levushkin Nikita,
- https://github.com/Rederickmind

**Contributors:**
- https://github.com/mstralenya
