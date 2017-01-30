﻿# Ресайзилка изображений

## Данный скрипт:

Изменяет размер изображений.

Для его работы при запуске нужно ввести обязательный аргумент - путь до исходного изображения. 

Также есть несколько необязательных аргументов:

• --width, ширина результирующего изображения;

• --height, высота результирующего изображения;

• --scale, во сколько раз увеличить(уменьшить) изображение;

• --path_to_output_image, куда класть результирующий файл.

## Логика работы программы такая:

• Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. И наоборот.

• Если указан масштаб, то ширина и высота указаны быть не могут.

• Если не указан путь до финального файла, то результат кладётся рядом с исходным файлом. 

## Запуск:

	python 3.5 image_resize.py *путь до исходного файла* *другие аргументы* 

## Пример вывода программы в консоль:

В случае ошибки:

	Никакие опции для работы с изображением не указаны

В случае успешной работы скрипта:

	Новое изображение готово!

## Зависимости:

Скрипт написан на языке Python 3, поэтому требует его наличия.
Для его правильной работы нужно установить библиотеку Pillow (см. requirements).

	pip install -r requirements.txt

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
