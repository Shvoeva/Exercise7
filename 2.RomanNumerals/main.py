arabic_number = int(input('\n\tВведите число от 1 до 3999: '))
if 1 > arabic_number or arabic_number > 3999:
    print(f'\tЧисло не входит в диапазон!')
    exit(0)

dictionary_of_arabic_roman_number = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

decreasing_number = arabic_number
roman_number = ''
while decreasing_number:
    for arabic_key, roman_value in dictionary_of_arabic_roman_number.items():
        if arabic_key <= decreasing_number:
            roman_number += roman_value
            decreasing_number -= arabic_key
            break

print(f'\tРимское число: {roman_number}')