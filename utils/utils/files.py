from os.path import getsize

from django.core.files import File

def iter_file_content(file_path, chunk_size=File.DEFAULT_CHUNK_SIZE):
    file_size = getsize(file_path)
    with open(file_path, 'rb') as f:
        while f.tell() != file_size:
            data = f.read(chunk_size)
            yield data