import sys

banks_rates = {
    'Alfa Bank': 60.65,
    'VTB': 64.60,
    'Gazprombank': 68.90,
    'Rosselhozbank': 70.50,
    'SberBank': 66.54,
    'Sovkombank': 64.50,
    'Tinkoff Bank': 64.55,
}

min_rate = sys.float_info.max
for bank, rate in banks_rates.items():
    if rate < min_rate:
        min_rate = rate
        min_bank = bank

print(f'\n\tБанки и курс доллара: {banks_rates}')
print(f'\tНаиболее привлекательным предложением является {min_rate:,.2f} в банке {min_bank}.')