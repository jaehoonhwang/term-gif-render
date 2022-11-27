import curses
import argparse
from time import sleep
import sys

from PIL import Image, ImageSequence

wait_time = 0.1  # in seconds

default_square_height = 64
default_square_width = 128
new_line = "\n"

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

sample_name = "giffo.gif"


def convert_to_pixel(image: Image, height: int, width: int) -> list[list[int]]:
    pixels = list(image.getdata())
    listified_pixels = [
        pixels[(i * width):((i + 1) * width)] for i in range(height)]
    return listified_pixels


def create_square(height: int, width: int, value: str) -> list[list[int]]:
    row = [value] * width
    square = [row for _ in range(height)]
    return square


def convert_pixel_to_ascii(pixel):
    max_brightness = 255 * len(pixel)
    pixel_brightness = sum(pixel)
    # pixel_brightness = pixel
    # max_brightness = 255
    brightness_weight = len(
        ascii_characters_by_surface) / (max_brightness)
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def render_square(square: list[list[int]]):
    line: str = ""

    for row in square:
        row_line = ""

        for ch in row:
            row_line += convert_pixel_to_ascii(ch)

        row_line += new_line
        line += row_line

    return line


def render_image(image: Image.Image, height: int, width: int):
    line: str = ""

    for x in range(height):
        row_line = ""

        for y in range(width):
            row_line += convert_pixel_to_ascii(image.getpixel((y, x)))

        row_line += new_line
        line += row_line

    return line


def main(argv):
    """main.py
    > python3 main.py <image_location> <wait_time>

    """
    parser = argparse.ArgumentParser(description="animating stuff on terminal")
    parser.add_argument('--file_name', type=str, default="giffo.gif",
                        help="location of file relative to python file; if in doubt, use an absolute path.")
    parser.add_argument('--wait_time', type=float, default=wait_time,
                        help="time in seconds between frames")
    parser.add_argument('--window_width', type=int, default=default_square_width,
                        help="window width")
    parser.add_argument('--window_height', type=int, default=default_square_height,
                        help="widnow height")

    args = parser.parse_args()

    std_scr = curses.initscr()
    image = Image.open(args.file_name)

    while True:
        i = 0
        for frame in ImageSequence.Iterator(image):
            if i == 0:
                i += 1
                continue
            resized_img: Image.Image = frame.resize(
                (args.window_width, args.window_height))
            std_scr.addstr(0, 0, render_image(
                resized_img, args.window_height, args.window_width))

            std_scr.refresh()
            sleep(args.wait_time)
            i += 1


if __name__ == "__main__":
    main(sys.argv)
