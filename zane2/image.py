import io
import os
import typing


class Image:

    def __init__(self, fp: typing.Union[os.PathLike, str, io.BytesIO]):
        self.bytes = None

        if isinstance(fp, io.BytesIO):
            self.bytes = fp
        else:
            with open(fp, "rb") as file:
                self.bytes = io.BytesIO(file.read())

    def edit(self, proxy, *args, **kwargs):
        """
        Proxy is the image proxy for the library you are using.
        close defines whether or not the image object will be automatically closed in __exit__
        *args and **kwargs are passed the the image initializer
        """
        return proxy(self, *args, **kwargs)

    def save(self, fp: typing.Union[os.PathLike, str, io.BytesIO]):
        if isinstance(fp, io.BytesIO):
            return fp
        with open(fp, "wb") as file:
            file.write(self.bytes.getvalue())

    def close(self):
        self.bytes.close()
