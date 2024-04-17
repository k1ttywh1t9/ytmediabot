from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from test import video_options



async def inline_choice(streams):
    choice = await video_options(streams)
    keyboard = InlineKeyboardBuilder()
    for item in choice:
        keyboard.add(InlineKeyboardButton(text = f'resolution: {item[1]}, format: {item[2]}', callback_data=f'itag_{item[0]}'))
    return keyboard.adjust(2).as_markup()
