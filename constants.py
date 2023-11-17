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
