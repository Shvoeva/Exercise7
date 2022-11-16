name_phon = {
    'Логинова В.С.': '89055553575',
    'Свитов М.П.': '89003006050',
    'Котов Г.Ю.': '89254504567',
}

phon_name = dict(zip(name_phon.values(), name_phon.keys()))

print(f'\n\tИзначальный словарь: {name_phon}')
print(f'\tИзмененный словарь: {phon_name}')