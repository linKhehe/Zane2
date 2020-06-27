from abc import ABC
import io

from wand.image import Image

from ..proxy import Proxy


class WandProxy(Proxy, ABC):

    @staticmethod
    def create(in_bytes: io.BytesIO, *args, **kwargs) -> Image:
        return Image(blob=in_bytes.getvalue(), *args, **kwargs)

    @staticmethod
    def save(image_object, out_bytes: io.BytesIO, image_format):
        image_object.save(out_bytes)

    @staticmethod
    def close(image_object):
        image_object.destroy()

    def __enter__(self) -> Image:
        return super().__enter__()
