from pytube import YouTube
from title_builder import clear_title
async def video_options(streams):
    clear_streams = streams.filter(mime_type="video/mp4")
    options = []
    for cstream in clear_streams:
        if cstream.itag<=132:
            options.append((cstream.itag, cstream.resolution, "mp4"))
    return options

def downloader(stream, title, extension):
    filename = f'{clear_title(title)}.{extension}'
    output_path = 'media\\'
    path = f'{output_path}{filename}'
    stream.download(output_path=output_path,filename=filename)
    return path

