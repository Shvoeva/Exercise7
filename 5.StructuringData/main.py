dates = ['2022-11-08', '2022-11-09', '2022-11-10', '2022-11-11', '2022-11-12']
rates = [61.24, 60.98, 61.06, 61.24, 60.22]

dates_rates = dict(zip(dates, rates))

print(f'\n\tСписок дат: {dates}')
print(f'\tСписок курсов: {rates}')
print(f'\tСловарь число-курс: {dates_rates}')