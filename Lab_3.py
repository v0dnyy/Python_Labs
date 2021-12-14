from Package.validator import file_validate
from Package.quick_sort import *
import os
import argparse


parser = argparse.ArgumentParser(description="main.py")
group = parser.add_mutually_exclusive_group()
parser.add_argument(
    '-input',
    type=str,
    default="85.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к входному файлу, имеет значение по умолчанию",
    dest="file_input")
parser.add_argument(
    '-output',
    type=str,
    default="Output.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к выходному файлу, имеет значение по умолчанию",
    dest="file_output")
parser.add_argument(
    '-sorted',
    type=str,
    default="Sorted.txt",
    help="Путь к файлу с отсортированными данными в формате pickle",
    dest="file_sorted"
)
parser.add_argument(
    '-sortedj',
    type=str,
    default="Sorted_json.txt",
    help="Путь к файлу с отсортированными данными в формате json",
    dest="file_sortedj"
)
parser.add_argument(
    '-o',
    '--opt',
    type=str,
    default='age',
    help="Выбор параметра для сортировки",
    dest="opt")
parser.add_argument(
    '-s',
    '--sort',
    help="Производит сортировку данных",
    dest="sort")
parser.add_argument(
    '-v',
    '--valid',
    help="Производит валидацию данных",
    dest="valid")
args = parser.parse_args()

input_path = os.path.realpath(args.file_input)
output_path = os.path.realpath(args.file_output)
sorted_path = os.path.realpath(args.file_sorted)
sortedj_path = os.path.realpath(args.file_sortedj)
option = args.opt
if args.valid is not None:
    file_validate(input_path, output_path)
elif args.sort is not None:
    data = read_data(output_path)
    data = quick_sort(data)
    save_json(sortedj_path, data)
    save_file(sorted_path, data)
    open_file(sorted_path)