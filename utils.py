from pytube import YouTube
from title_builder import clear_title
def available_streams():
    
def downloader(stream, title, extension):
    filename = f'{clear_title(title)}.{extension}'
    output_path = 'data/media/'
    path = f'{output_path}{filename}'
    stream.download(output_path=output_path,filename=filename)
    return path
