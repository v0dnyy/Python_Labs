import json
import re
from tqdm import tqdm
import argparse

class File:
    """
    Класс для чтения записей из файла
    Attributes:
        _data : list
        Содержит данные в виде списка, считанные из текстового файла
    """
    def __init__(self, path: str) -> None:
        self._data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> list:
        return self._data


class Validator:
    """
    Класс Validator проверяет данные на корректность
    Attributes:
        _telephone: str - хранит номер телефона пользователя
        _weight: float - хранит вес пользователя
        _snils: str - хранит снилс пользователя
        _passport_series: str - хранит серию паспорта пользователя
        _occupation: str - хранит род деятельности пользователя
        _work_experience: float - хранит рабочий стаж пользователя
        _political_views: str - хранит политические взгляды пользователя
        _worldview: str - хранит мировоззрение пользователя
        _address: str - хранит адрес проживания пользователя
        _valid_political_views: list - хранит список с существующими полит. взглядами
        _valid_worldview: list - хранит список существующих мировоззрений
        _invalid_occupation: list - хранит список невалидных родов деятельности
    """
    _email: str
    _weight: float
    _inn: str
    _passport_series: str
    _occupation: str
    _age: int
    _political_views: str
    _worldview: str
    _address: str
    _valid_political_views: list = ['Индифферентные',
                                    'Социалистические',
                                    'Консервативные',
                                    'Коммунистические',
                                    'Либеральные',
                                    'Умеренные',
                                    'Анархистские',
                                    'Либертарианские']
    _valid_worldview: list = ['Пантеизм',
                              'Секулярный гуманизм',
                              'Деизм',
                              'Атеизм',
                              'Иудаизм',
                              'Католицизм',
                              'Конфуцианство',
                              'Агностицизм',
                              'Буддизм']
    _invalid_occupation = ['Рыцарь смерти',
                           'Воин',
                           'Друид',
                           'Шаман',
                           'Жрец',
                           'Паладин',
                           'Маг',
                           'Охотник на демонов',
                           'Чернокнижник',
                           'Разбойник',
                           'Монах']

    def __init__(self, data: dict):
        """
        Инициализируется объект класса Validator
        :param data: dict
            Передается словарь со всеми полями данных
        """
        self._email = data['email']
        self._weight = data['weight']
        self._inn = data['inn']
        self._passport_series = data['passport_series']
        self._occupation = data['occupation']
        self._age = data['age']
        self._political_views = data['political_views']
        self._worldview = data['worldview']
        self._address = data['address']

    def check_email(self) -> bool:
        """
        Метод проверяет номер телефона пользователя
        Если отсутствуют скобки, знак + перед 7, цифр в номере или больше или меньше, то номер является невалидным
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", self._email) is not None:
            return True
        return False

    def check_weight(self) -> bool:
        """
        Метод проверяет вес пользователя
        Если вес является физически невозможным, то вес является невалидным
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^\d{2,3}$", str(self._weight)) is not None) and (int(float(self._weight) < 150)) and \
                int((float(self._weight)) > 20):
            return True
        return False

    def check_inn(self) -> bool:
        """
        Метод проверяет снилс пользователя
        Если количество цифр в нем отлично от 11, то снилс невалидный
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"[0-9]{11}", str(self._inn)) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        Метод проверяет серию паспорта пользователя
        Если количество цифр больше или меньше 4 и цифры не разбиты на пары, то серия невалидная
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^\d{2}\s\d{2}$", self._passport_series) is not None:
            return True
        return False

    def check_occupation(self) -> bool:
        """
        Метод проверяет род деятельности пользователя
        Если род деятельности записан некорректно, то он не валидный
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._occupation) is not None) and (self._occupation not in self._invalid_occupation):
            return True
        return False

    def check_age(self) -> bool:
        """
        Метод проверяет рабочий стаж пользователя
        Если он состоит не из цифр, или превышает разумное значение, то он невалидный
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"[0-9]{1,3}", str(self._age)) is not None and 0 < int(self._age) <= 108:
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Метод проверяет полит. взгляды пользователя
        Если они не соответствуют существующим полит. взглядам, то они невалидные
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^(([А-яA-z])+\.?\s?-?)+$", self._political_views) is not None) and \
                (self._political_views in self._valid_political_views):
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Метод проверяет мировоззрение пользователя
        Если оно не соответствует существующим мировоззрениям, то оно невалидное
        :return: bool
        Возвращается или True или False
        """
        if (re.match(r"^([А-яA-z]+\.?\s?-?)+$", self._worldview) is not None) and \
                (self._worldview in self._valid_worldview):
            return True
        return False

    def check_address(self) -> bool:
        """
        Метод проверяет адрес пользователя
        Если он не начинается с ул. или Аллея, то он невалидный
        :return: bool
        Возвращается или True или False
        """
        if re.match(r"^[A-я.]+\s[\w .()-]+\d+$", self._address) is not None:
            return True
        return False

    def check_data(self) -> list:
        """
        Метод проверяет все поля на корректность
        Если в каком-либо поле найдена ошибка, то оно записывается в список
        :return: list
        Возвращает список с данными пользователя, у которого присутствует невалидная запись
        """
        invalid_values = []
        if not self.check_email():
            invalid_values.append("email")
        if not self.check_weight():
            invalid_values.append("weight")
        if not self.check_inn():
            invalid_values.append("inn")
        if not self.check_passport_series():
            invalid_values.append("passport_series")
        if not self.check_occupation():
            invalid_values.append("occupation")
        if not self.check_age():
            invalid_values.append("age")
        if not self.check_political_views():
            invalid_values.append("political_views")
        if not self.check_worldview():
            invalid_values.append("worldview")
        if not self.check_address():
            invalid_values.append("address")
        return invalid_values


parser = argparse.ArgumentParser(description="main.py")
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
    '-output_',
    type=str,
    default="Output_Fail.txt",
    help="Это строковый аргумент, который подразумевает ввод пути к выходному файлу, имеет значение по умолчанию",
    dest="file_output_")
args = parser.parse_args()
data = File(args.file_input).data
count_valid = 0
count_invalid = 0
dict_invalid_records = {"email": 0,
                        "weight": 0,
                        "inn": 0,
                        "passport_series": 0,
                        "occupation": 0,
                        "age": 0,
                        "political_views": 0,
                        "worldview": 0,
                        "address": 0}
list_result = []
list_fail_result = []
with tqdm(data, desc="Прогресс обработки записей") as progressbar:
    for elem in data:
        check = Validator(elem).check_data()
        if len(check) == 0:
            count_valid += 1
            list_result.append(
                {
                    "email": elem["email"],
                    "weight": elem["weight"],
                    "inn": elem["inn"],
                    "passport_series": elem["passport_series"],
                    "occupation": elem["occupation"],
                    "age": elem["age"],
                    "political_views": elem["political_views"],
                    "worldview": elem["worldview"],
                    "address": elem["address"]
                }
            )
        else:
            count_invalid += 1
            list_fail_result.append(
                {
                    "email": elem["email"],
                    "weight": elem["weight"],
                    "inn": elem["inn"],
                    "passport_series": elem["passport_series"],
                    "occupation": elem["occupation"],
                    "age": elem["age"],
                    "political_views": elem["political_views"],
                    "worldview": elem["worldview"],
                    "address": elem["address"]
                }
            )
            for item in check:
                dict_invalid_records[item] += 1
        progressbar.update(1)
with open(args.file_output, 'w', encoding='utf-8') as output:
    json.dump(list_result, output, indent=4, ensure_ascii=False)
with open(args.file_output_, 'w', encoding='utf-8') as output_:
    json.dump(list_fail_result, output_, indent=4, ensure_ascii=False)
print(f"Amount of valid records: {count_valid}")
print(f"Amount of invalid records: {count_invalid}")
print("Amount of invalid entries by type of error:")
for key, value in dict_invalid_records.items():
    print(" " * 4 + str(key) + ": " + str(value))