import pandas as pd

player_name = str(input('Whats is your name? '))

matches = {
    1: {'id': 1, 'home': 'Atlético MG', 'away': 'Goiás' }, 2: {'id': 2, 'home': 'Fluminense', 'away': 'Coritiba'},
    3: {'id': 3, 'home': 'Juventude', 'away': 'Botafogo'}, 4: {'id': 4, 'home': 'Palmeiras', 'away': 'Flamengo'},
    5: {'id': 5, 'home': 'Fortaleza', 'away': 'Corinthians'}, 6: {'id': 6, 'home': 'Atlético GO', 'away': 'Cuiabá'},
    7: {'id': 7, 'home': 'Athletico PR', 'away': 'América MG'}, 8: {'id': 8, 'home': 'Bragantino', 'away': 'Ceará'},
    9: {'id': 9, 'home': 'Santos', 'away': 'São Paulo'}, 10: {'id': 10, 'home': 'Avaí', 'away': 'Internacional'}
}

dict_player = {
    1: {'id': 1, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    2: {'id': 2, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    3: {'id': 3, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    4: {'id': 4, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    5: {'id': 5, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    6: {'id': 6, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    7: {'id': 7, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    8: {'id': 8, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    9: {'id': 9, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''},
    10: {'id': 10, 'player': player_name, 'home': '', 'away': '', 'winner': '', 'points': ''}
}

count = 1

while count <= 10:
    # for key, value in matches.items():
    print('GAME ', count)
    print('-'*20)
    print(matches[count]['home'] + ' X ' + matches[count]['away'])

    while True:
        try:
            home_score = int(input(matches[count]['home'] + ': '))
            break
        except ValueError:
            print('Only numbers!')

    while True:
        try:
            away_score = int(input(matches[count]['away'] + ': '))
            break
        except ValueError:
            print('Only numbers!')

    print('-'*20)
    confirm = str(input('Do you confirm [y]: yes / [n]: no\n' + matches[count]['home'] + ' ' + str(home_score) + ' X ' +
                        str(away_score) + ' ' + matches[count]['away'] + ' ')).lower()

    if confirm == 'y':

        if home_score > away_score:
            winner = matches[count]['home']

        elif home_score < away_score:
            winner = matches[count]['away']

        elif home_score == away_score:
            winner = 'empate'

        dict_player[count]['home'] = home_score
        dict_player[count]['away'] = away_score
        dict_player[count]['winner'] = winner

        print('\n')
        print('-=' * 10)
        print('\n')

        count += 1

    else:
        print('-' * 10)
        print('---INSERT AGAIN---')
        count = count

    # else:
    #   print('invalid')
    #  count = count

df = pd.DataFrame(dict_player).T.set_index('id')
df.to_csv(player_name + '.csv')
