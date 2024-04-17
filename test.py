from pytube import YouTube
async def video_options(streams):
    clear_streams = streams.filter(mime_type="video/mp4")
    options = []
    for cstream in clear_streams:
        options.append((cstream.itag, cstream.resolution, "mp4"))
    return options

def downloader(stream, filename):
    stream.download(output_path='media\\',filename=filename)