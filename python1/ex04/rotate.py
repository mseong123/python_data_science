import load_image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def rotate(im: np.ndarray) -> np.ndarray:
    """function to rotate image"""
    mylist = im.tolist()
    rotated_list = [[row[i] for row in mylist] for i in range(len(mylist[0]))]
    return np.array(rotated_list)


def zoom(im: np.ndarray) -> np.ndarray:
    """function to zoom image"""
    size = 400
    y_start = 120
    x_start = 390
    im = im[y_start:y_start + size, x_start:x_start + size]
    return im


def main():
    """main"""
    im = load_image.ft_load("animal.jpeg")
    if im is not None:
        im = np.array(Image.fromarray(im).convert("L"))
        im = zoom(im)
        print("The shape of image is: " + str(im.shape))
        print(im)
        im = rotate(im)
        plt.imshow(im, cmap="gray")
        print("New shape after Transpose: " + str(im.shape))
        print(im)
        try:
            plt.show()
        except KeyboardInterrupt:
            print("Pressed Ctrl-C")


if __name__ == "__main__":
    main()
