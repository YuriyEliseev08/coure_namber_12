import json


def get_operatios_list(file_name):
    """Открыть файл и вернуть список словарей"""
    with open(file_name, encoding="utf8") as file:
        file_name = json.load(file)
        return file_name


def sort_list(my_list):
    """Сортируем по убыванию """
    return sorted(my_list, key=lambda x: x["date"], reverse=True)


def filtr_exequted(my_list):
    """Фильтруем список и выбираем выполненные файлы"""
    result = []
    for element in my_list:
        if element.get("state") == "EXECUTED":
            result.append(element)
    return result


def get_date_format(date):
    """Переводим строку в формат по заданию"""
    data = date.split("T")
    index_data = data[0].split("-")
    return ".".join(index_data[::-1])


def namber_accout_format(number):
    """Выводим скрытые номера счетов и карт"""
    if number:
        if number.startswith("Счет"):
            temp = number.split()
            index_temp = "**" + temp[-1][-4:]
            return f'{temp[0]} {index_temp}'
        else:
            temp = number.split()
            temp[-1] = temp[-1][:4] + " " + temp[-1][4:6] + "** **** " + temp[-1][12:]
            return " ".join(temp)


def get_out_putt(get_out):
    """Вывод конечного результата"""
    data_operetion = get_date_format(get_out['date'])
    description = get_out["description"]
    from_account = namber_accout_format(get_out.get("from"))
    to_account = namber_accout_format(get_out.get("to"))
    summ = float(get_out["operationAmount"]["amount"])
    currency_ = get_out["operationAmount"]["currency"]["name"]
    return f"{data_operetion} {description}\n{from_account} -> {to_account}\n{summ} {currency_}"


