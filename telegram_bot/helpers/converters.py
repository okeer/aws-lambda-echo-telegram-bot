import io
from numdl.utils.data import image_to_np_array


def download_file(bot, file_id):
    file_bytes = io.BytesIO()
    file = bot.get_file(file_id)
    file.download(out=file_bytes)
    return file_bytes


def convert_bytes_to_image_array(file_bytes):
    return image_to_np_array(file_bytes, 64, 64)/255.


def compose_reply(data, backend):
    repl = "Classified objects:\n\n"

    for label in data:
        repl += "**{Confidence:.2f}%** --- `{Name}`\n\n".format(**label)

    repl += f"Served by **{backend}**"
    return repl
