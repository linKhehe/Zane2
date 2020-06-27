import io

import abc


class Proxy(metaclass=abc.ABCMeta):

    def __init__(self, image, *args, **kwargs):
        self.image = image
        self.args = args
        self.kwargs = kwargs

        self.object = None

    @staticmethod
    @abc.abstractmethod
    def create(in_bytes: io.BytesIO, *args, **kwargs):
        """
        Create an image with this proxy's image library.

        Parameters
        ----------
        in_bytes: io.BytesIO
            The BytesIO object to create the image with.
        args
            To be passed to the image initializer/classmethod.
        kwargs
            To be passed to the image initializer/classmethod.

        Returns
        -------
        Image
            Image created with the proxy's image library.
        """
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def save(image_object, out_bytes: io.BytesIO, image_format):
        """
        Save the image object to out_bytes. Image_format is not for converting
        the format, just stating the current format.

        Parameters
        ----------
        image_object
            The image object, specific to the proxy's image library.
        out_bytes: io.BytesIO
            The BytesIO object to write the bytes to
        image_format
            The format to save the image in. This will never be a conversion,
            it's just a specifier for what format the image is currently in.
        """
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def close(image_object):
        """
        Close the image object.

        Parameters
        ----------
        image_object
            The image object to close
        """
        image_object.close()

    def __enter__(self):
        self.object = self.create(self.image.bytes, *self.args, **self.kwargs)
        return self.object

    def __exit__(self, *args, **kwargs):
        self.image.bytes.close()
        self.image.format = getattr(self.object, "format", getattr(self.image, "format", None))

        b = io.BytesIO()
        self.save(self.object, b, self.image.format)
        b.seek(0)

        self.close(self.object)

        self.image.bytes = b

    def __add__(self, new):
        self.object = new



