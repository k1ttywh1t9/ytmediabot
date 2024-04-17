from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery, Message, FSInputFile
import keyboards as kb
from pytube import YouTube
from title_builder import clear_title
from test import downloader

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!')

@router.message(F.text.startswith('https://'))
async def share_link(message):
    url = message.text
    yt = YouTube(url)
    streams = yt.streams
    await message.reply(url, reply_markup=await kb.inline_choice(streams))
@router.callback_query(F.data.startswith('itag'))
async def send_media(callback: CallbackQuery):
    await callback.answer('downloading media')
    url = callback.message.text
    yt = YouTube(url)
    try:
        itag = str(callback.data).split('_')[1]
        print(itag)
        stream = yt.streams.get_by_itag(itag)

        title = yt.title

        filename = f'{clear_title(title)}.mp4'
        downloader(stream, filename)
        await callback.message.answer_video(FSInputFile(path=f'media\\{filename}'))
    except Exception as ex:
        print(ex)
        return


