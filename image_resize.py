import argparse
import os.path
from PIL import Image


def argparser():
    parser = argparse.ArgumentParser(description='Ресайзилка изображений')
    parser.add_argument('path_to_input_image',
                        help='Введите путь до исходного изображения')
    parser.add_argument('--width',
                        help='Введите ширину результирующего изображения', type=int)
    parser.add_argument('--height',
                        help='Введите высоту результирующего изображения', type=int)
    parser.add_argument('--scale',
                        help='Введите во сколько раз увеличить изображение', type=float)
    parser.add_argument('--path_to_output_image',
                        help='Введите путь до результирующего изображения')
    return parser.parse_args()


def open_image(path_to_original):
    return Image.open(path_to_original)


def resize_image(image, width, height, scale):
    original_width, original_height = image.size
    proportion = original_width / original_height
    if scale:
        image = image.resize((round(original_width * scale), round(original_height * scale)))
    elif width:
        image = image.resize((width, round(width / proportion)))
    elif height:
        image = image.resize((round(height * proportion), height))
    elif width and height:
        if width / height != proportion:
            print('Пропорции не совпадают с исходным изображением')
        image = image.resize((width, height))
    return image


def save_image(image, path_to_original, path_to_result):
    if not path_to_result:
        original_name, extension = os.path.splitext(path_to_original)
        path_to_result = '{}__{}x{}{}'.format(original_name, *image.size, extension)
    image.save(path_to_result, image.format)


if __name__ == '__main__':
    parser = argparser()
    if not os.path.exists(parser.path_to_input_image):
        print('Файл не найден')
    elif not (parser.width or parser.height or parser.scale):
        print('А что делать то? Никакие опции не указаны')
    elif parser.scale and (parser.width or parser.height):
        print('Если указан масштаб, то ширина и высота указаны быть не могут')
    else:
        user_image = open_image(parser.path_to_input_image)
        formatted_image = resize_image(user_image, parser.width, parser.height, parser.scale)
        save_image(formatted_image, parser.path_to_input_image, parser.path_to_output_image)
        print('Новое изображение готово!')