from abc import ABC
import io

import numpy
import matplotlib.pyplot as plt
import skimage.io

from ..proxy import Proxy


class SkimageProxy(Proxy, ABC):

    # noinspection PyTypeChecker
    @staticmethod
    def create(in_bytes: io.BytesIO, *args, **kwargs) -> numpy.ndarray:
        return skimage.io.imread(in_bytes, *args, **kwargs)

    @staticmethod
    def save(image_object, out_bytes: io.BytesIO, image_format):
        plt.imsave(out_bytes, image_object, format=image_format)

    @staticmethod
    def close(image_object):
        pass

    def __enter__(self) -> numpy.ndarray:
        return super().__enter__()
