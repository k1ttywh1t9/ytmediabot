import pytube
from pytube import YouTube
class OversizingException(Exception):
    def __init__(self, name):
        self.name = name
async def get_filesize_compared_to_limit(stream):
    size = stream.filesize_mb
    if size > 50:
        raise OversizingException
    return True