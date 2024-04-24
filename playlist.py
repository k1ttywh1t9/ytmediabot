from os import remove
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile
from pytube.contrib.playlist import Playlist
import re


router_playlist = Router()

@router_playlist.callback_query(F.data == 'playlist')
async def send_playlist(callback: CallbackQuery):
    await callback.answer('downloading audio playlist')
    try:
        url = callback.message.reply_to_message.text
        videos = Playlist(url).videos
        for yt in videos:
            try:
                output_path = 'media/playlist'
                title = yt.title
                clear_title = re.sub(r'[^a-zA-Z0-9\s]+', '', title)
                filename = f'{clear_title}.mp3'
                yt.streams.get_audio_only().download(output_path=output_path, filename=filename)
                path = f'{output_path}/{filename}'
                await callback.message.answer_audio(FSInputFile(path=path))
                remove(path)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
