# Zane2
A python imaging library that eases the stress of using multiple image libraries.

## Example
```python
import zane2
import skimage.transform

image = zane2.Image("image_in.png")

with image.edit(zane2.WandProxy) as proxy:
    proxy.implode(amount=1.35)

with image.edit(zane2.PILProxy) as proxy:
    proxy.resize((400, 400))

with image.edit(zane2.SkimageProxy) as proxy:
    # this is equal but used instead of proxy = swirl(image)
    proxy + skimage.transform.swirl(proxy)

image.save("image_out.png")
```