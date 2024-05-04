from os import remove
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message, FSInputFile, MessageEntity
import keyboards as kb
import pytube
from pytube import YouTube
from utils import downloader
from playlist import playlist_identifier

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello! This bot can download media from Youtube,\n\tSend a link to a video or playlist')

@router.message(F.text.startswith('https://www.youtube.com/'))
async def share_link(message: Message):
    try:
        await message.reply('What you want to download from this url?', reply_markup=await kb.choice_function(is_playlist=(playlist_identifier(message.text))))
    except Exception as ex:
        print(ex)
@router.message(F.text.startswith('http://www.youtube.com/'))
async def share_link(message: Message):
    try:
        await message.reply('What you want to download from this url?', reply_markup=await kb.choice_function(is_playlist=(playlist_identifier(message.text))))
    except Exception as ex:
        print(ex)

@router.message(F.text.startswith('https://youtu.be/'))
async def share_link1(message: Message):
    try:
        await message.reply('What you want to download from this url?', reply_markup=await kb.choice_function(is_playlist=(playlist_identifier(message.text))))
    except Exception as ex:
        print(ex)
@router.message(F.text.startswith('http://youtu.be/'))
async def share_link1(message: Message):
    try:
        await message.reply('What you want to download from this url?', reply_markup=await kb.choice_function(is_playlist=(playlist_identifier(message.text))))
    except Exception as ex:
        print(ex)

@router.callback_query(F.data.startswith('audio_download'))
async def send_audio(callback: CallbackQuery):
    await callback.answer('downloading audio')
    try:
        url = callback.message.reply_to_message.text
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        title = yt.title
        path = downloader(stream, title, 'mp3')
        await callback.message.answer_audio(FSInputFile(path=path))
        remove(path)
    except Exception as ex:
        print(ex)
        return

@router.callback_query(F.data.startswith('video'))
async def send_media(callback: CallbackQuery):
    await callback.answer(f'downloading video')
    try:
        url = callback.message.reply_to_message.text
        yt = YouTube(url)
        itag = str(callback.data).split()[1]
        print(itag)
        stream = yt.streams.get_by_itag(itag)
        title = yt.title
        path = downloader(stream, title, 'mp4')
        await callback.message.answer_video(FSInputFile(path=path))
        remove(path)
    except Exception as ex:
        print(ex)
        return


