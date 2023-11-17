from aiogram import F

LINK_FILTER = (
    F.text.contains("https://x.com")
    | F.text.contains("https://twitter.com")
    | F.text.contains("https://x.com")
    | F.text.contains("https://www.twitter.com")
    | F.text.contains("https://mobile.twitter.com")
    | F.text.contains("https://www.instagram.com")
    | F.text.contains("https://instagram.com")
)

START_TEXT = (
    """
Привет, {}.

Это простой бот для замены префикса в ссылках соцсетей,
превью которых не отображается в Telegram.
(Twitter.com, x.com, instagram.com*)

Побочным эффектом превью Instagram является
возможность сохранять рилзы из превью.

*Facebook/Instagram — проект Meta Platforms Inc.,
деятельность которой в России запрещена
"""
)

HELP_TEXT = """
Даже не представляю какие ошибки могут возникнуть при работе с этим ботом,
но вы всегда можете мне написать в телеграм @Rederickmind
"""
