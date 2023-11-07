from PIL import Image
import numpy as np


def ft_load(path: str):
    """function to load image using PIL image library and return ndarray"""
    try:
        im = Image.open(path)
    except Exception as e:
        print(f"{e}")
    else:
        arr = np.array(im)
        return arr
