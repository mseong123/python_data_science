import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """inverts the color of picture"""
    if array is not None:
        print(array)
        Image.fromarray(255 - array).show()


def ft_red(array) -> np.ndarray:
    """applies red color filter"""
    if array is not None:
        print(array)
        array[:, :, 1] = 0
        array[:, :, 2] = 0
        Image.fromarray((array)).show()


def ft_green(array) -> np.ndarray:
    """applies green color filter"""
    if array is not None:
        print(array)
        array[:, :, 0] = 0
        array[:, :, 2] = 0
        Image.fromarray((array)).show()


def ft_blue(array) -> np.ndarray:
    """applies blue color filter"""
    if array is not None:
        print(array)
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        Image.fromarray((array)).show()


def ft_grey(array) -> np.ndarray:
    """applies grey color filter"""
    if array is not None:
        print(array)
        array = np.mean(array, dtype=np.uint32, axis=2).astype(np.uint8)
        Image.fromarray((array)).show()
