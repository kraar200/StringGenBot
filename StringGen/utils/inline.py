from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="بداء الاستخراج", callback_data="gensession")],
        [
            InlineKeyboardButton(text="COURCE", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="- قناة المطور .", url="https://t.me/d8_8q"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروكرام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروكرام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="حاول مرة اخرى", callback_data="gensession")]]
)
