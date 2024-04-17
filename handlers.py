from os import remove
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message, FSInputFile, MessageEntity
import keyboards as kb
from pytube import YouTube
from utils import downloader

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello! This bot can download media from Youtube,\n\tSend a link to a video or playlist')

@router.message(F.text.startswith('https://'))
async def share_link(message):
    url = message.text
    await message.reply('What you want to download from this url?', reply_markup=await kb.choice_function(url))
@router.callback_query(F.data.startswith('video_download'))
async def chosen_video(callback: CallbackQuery):
    url = callback.data.split()[1]
    yt = YouTube(url)
    streams = yt.streams
    await callback.message.answer(url, reply_markup=await kb.inline_choice_resolution(streams))


@router.callback_query(F.data.startswith('audio_download'))
async def send_audio(callback: CallbackQuery):
    await callback.answer('downloading audio')
    url = callback.data.split()[1]
    yt = YouTube(url)
    try:
        stream = yt.streams.get_audio_only()
        title = yt.title
        path = downloader(stream, title, 'mp3')
        await callback.message.answer_audio(FSInputFile(path=path))
        remove(path)
    except Exception as ex:
        print(ex)
        return


@router.callback_query(F.data.startswith('itag'))
async def send_media(callback: CallbackQuery):
    await callback.answer(f'downloading video')
    url = callback.message.text
    yt = YouTube(url)
    try:
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


