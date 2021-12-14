import pickle
from tqdm import tqdm
import json


def quick_sort(data: list) -> list:
    import sys

    sys.setrecursionlimit(100000)
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i["age"] <= pivot["age"]]

        greater = [i for i in data[1:] if i["age"] > pivot["age"]]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as rfile:
        database = json.load(rfile)
    return database


def open_file(file_path: str) -> list:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


def save_file(save_path: str, data: list) -> None:
    with open(save_path, 'wb') as file:
        pickle.dump(data, file)


def save_json(save_path: str, data: list) -> None:
    with open(save_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)