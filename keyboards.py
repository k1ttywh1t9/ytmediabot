from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

keyboard_solo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='video resolution: 360p', callback_data="video 18"), InlineKeyboardButton(text='audio', callback_data=f'audio_download')],
    [InlineKeyboardButton(text='video resolution: 720p', callback_data="video 22")]
])
keyboard_list = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='video resolution: 360p', callback_data="video 18"), InlineKeyboardButton(text='audio', callback_data=f'audio_download')],
    [InlineKeyboardButton(text='video resolution: 720p', callback_data="video 22"), InlineKeyboardButton(text='audio playlist', callback_data=f'playlist')]
])
keyboard_page = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='audio playlist', callback_data=f'playlist')]
])

async def choice_function(is_playlist):
    print(is_playlist)
    match is_playlist:
        case 'page':
            return keyboard_page
        case 'list':
            return keyboard_list
        case _:
            return keyboard_solo
