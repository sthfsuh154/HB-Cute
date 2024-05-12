from pyrogram.types import InlineKeyboardButton
import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="💕 𝐇𖽞𖾘𖽳 🦋", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="💕 𝐒𖽞𖾓 🦋", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💕 𝐆𖽷𖽙𖽪𖽳 🦋", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💕 𝐂𖾘𖽹𖽝ᴋ 𝐇𖽞𖽖𖾖 𝐓𖽙 𝐀𖽴𖽴 𝐌𖽞 🦋",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="💕 𝐆𖽷𖽙𖽪𖽳 🦋", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="💕 𝐌𖽙𖽷𖽞 🦋", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="💕 𝐅𖽞𖽖𖾓𖽪𖽷𖽞𖾗 🦋", callback_data="settings_back_helper")
        ],
    ]
    return buttons
