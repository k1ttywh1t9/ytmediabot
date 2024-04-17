from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import video_options

async def choice_function(url):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='video', callback_data=f'video_download {url}'),
    InlineKeyboardButton(text='audio', callback_data=f'audio_download {url}')],
    [InlineKeyboardButton(text='audio playlist', callback_data=f'playlist {url}')]])
    return keyboard



async def inline_choice_resolution(streams):
    choice = await video_options(streams)
    keyboard = InlineKeyboardBuilder()
    for item in choice:
        keyboard.add(
            InlineKeyboardButton(text=f'resolution: {item[1]}, format: {item[2]}', callback_data=f'itag {item[0]} mp4'))
    return keyboard.adjust(2).as_markup()
