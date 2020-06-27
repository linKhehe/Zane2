from abc import ABC
import io

from PIL import Image

from ..proxy import Proxy


class PILProxy(Proxy, ABC):

    @staticmethod
    def create(in_bytes: io.BytesIO, *args, **kwargs) -> Image:
        return Image.open(in_bytes, *args, **kwargs)

    @staticmethod
    def save(image_object, out_bytes: io.BytesIO, image_format):
        image_object.save(out_bytes, format=image_format)

    @staticmethod
    def close(image_object):
        image_object.close()

    def __enter__(self) -> Image:
        return super().__enter__()
