from os import remove
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile
import pytube
from pytube.contrib.playlist import Playlist
import re
from filesize_control import get_filesize_compared_to_limit, OversizingException

router_playlist = Router()


def playlist_identifier(text: str):
    if text.find('playlist') != -1:
        return 'page'
    if text.find('list=') != -1:
        return 'list'


@router_playlist.callback_query(F.data == 'playlist')
async def send_playlist(callback: CallbackQuery):
    await callback.answer('downloading audio playlist')
    try:
        url = callback.message.reply_to_message.text
        videos = Playlist(url).videos
        for yt in videos:
            try:
                output_path = 'data/media/playlist'
                title = yt.title
                clear_title = re.sub(r'[^a-zA-Z0-9\s]+', '', title)
                filename = f'{clear_title}.mp3'
                stream = yt.streams.get_audio_only()
                await get_filesize_compared_to_limit(stream)
                stream.download(output_path=output_path, filename=filename)
                path = f'{output_path}/{filename}'
                await callback.message.answer_audio(FSInputFile(path=path))
                remove(path)
            except OversizingException:
                await callback.message.answer(f'audio {title} is not downloaded, size of the file is bigger than 50 Mb')
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
