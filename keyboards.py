from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def choice_function(is_playlist):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='video resolution: 360p', callback_data="video 18")
    keyboard.button(text='audio', callback_data=f'audio_download')
    keyboard.button(text='video resolution: 720p', callback_data="video 22")
    if is_playlist!=-1:
        keyboard.button(text='audio playlist', callback_data=f'playlist')
    return keyboard.adjust(2,2).as_markup()
