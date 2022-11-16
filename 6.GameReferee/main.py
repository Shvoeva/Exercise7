import re

victory = {
    r'(XXX.{6})|(...XXX...)|(.{6}XXX)|(X..X..X..)|(.X..X..X.)|(..X..X..X)|(X...X...X)|(...X.X.X..)': 'X',
    r'(OOO.{6})|(...OOO...)|(.{6}OOO)|(O..O..O..)|(.O..O..O.)|(..O..O..O)|(O...O...O)|(...O.O.O..)': 'O',
}

line1 = input('\n\tВведите первую строку: ')
line2 = input('\tВведите вторую строку: ')
line3 = input('\tВведите третью строку: ')
list_game_result = [line1, line2, line3]

str_game_result = ''.join(list_game_result)
if (re.search(r'[^OX.]', str_game_result) or len(str_game_result) != 9):
    print('\n\tРезультат игры введен неверно!')
    exit(0)

winner = 'D'
for key_result, value_winner in victory.items():
    if re.search(key_result, str_game_result):
        winner = value_winner
        break

print(f'\n\tПобедитель в игре крестики-нолики: {winner}')