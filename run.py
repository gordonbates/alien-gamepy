from random import randint
"""
Random module for the dynamic alien attack between
the low and high values set
"""

print("""
............................................................
.                                                          .
.          ----- Welcome to Alien Gamepy -----             .
.                                                          .
............................................................
""")

print("""
           \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._""'  \ _,="=._ /  ""'_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\.
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\.
/'       )                  _                  (       `\.
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \.
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \.
      /,'             | | | | | | |             `,\.
     /'               ` | | | | | '               `\.
                        ` | | | '
                          ` | '
""")

game_running = True
game_results = []


def calculate_alien_attack(att_low, att_hi):
    return randint(att_low, att_hi)
    """
    Calculate random attack number using arguments from dictionary below
    """


def game_over(winner_name):
    print(f'{winner_name} won the battle!!')


while game_running is True:
    counter = 0
    new_battle = True
    player = {'name': '{}', 'attack': 10, 'heal': 12, 'health': 100}
    alien = {'name': 'Xenomorph', 'att_low': 7, 'att_hi': 16, 'health': 100}
    """
    player and alien values
    """

    print('.....' * 12)
    print('-------\n' * 5)
    print('Enter Player name')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(alien['name'] + ' has ' + str(alien['health']) + ' health')

    while new_battle is True:

        counter = counter + 1
        player_win = False
        alien_win = False

        print('-------')
        print('Please Select An Action:\n')
        print('1. Attack')
        print('2. Heal')
        print('3. Exit Game')
        print('4. Show Results')

        player_action = input()

        if player_action == '1':
            alien['health'] = alien['health'] - player['attack']
            if alien['health'] <= 0:
                player_win = True
                """
                Checks if alien health is above 0, if not player wins
                """

            else:
                attack_damage = calculate_alien_attack(
                    alien['att_low'], alien['att_hi'])
                player['health'] -= attack_damage
                if player['health'] <= 0:
                    alien_win = True
                    """
                    Checks if player health is above 0, if not alien wins
                    """

        elif player_action == '2':
            player['health'] = player['health'] + player['heal']

            attack_damage = calculate_alien_attack(
                alien['att_low'], alien['att_hi'])
            player['health'] -= attack_damage
            if player['health'] <= 0:
                alien_win = True
                """
                Control structure for applying heal value to the players health
                """

        elif player_action == '3':
            new_battle = False
            game_running = False
            """
            How to exit the game loop
            """

        elif player_action == '4':
            for stats in game_results:
                print(stats)
                """
                Shows the player(s) stats
                """

        else:
            print('Invalid Action')

        if player_win is False and alien_win is False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(alien['name'] + ' has ' + str(alien['health']) + ' left')
            """
            For showing the remaining health after each round
            """

        elif player_win:
            game_over(player['name'])
            round_result = {
                'name': player['name'], 'health': player['health'],
                'rounds': counter}
            """
            Stores the results of a game in a list for each player
            """
            game_results.append(round_result)
            new_battle = False

        elif alien_win:
            game_over(alien['name'])
            round_result = {
                'name': player['name'], 'health': player['health'],
                'rounds': counter}
            game_results.append(round_result)
            new_battle = False

