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


def calculate_alien_attack():
    return randint(alien['att_low'], alien['att_hi'])
    """
    Calculate random attack number
    """


while game_running is True:
    new_battle = True
    player = {'name': 'Manuel', 'attack': 10, 'heal': 18, 'health': 100}
    alien = {'name': 'Xenomorph', 'att_low': 8, 'att_hi': 20, 'health': 100}
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

        player_win = False
        alien_win = False

        print('-------')
        print('Please Select An Action:\n')
        print('1. Attack')
        print('2. Heal')
        print('3. Exit Game')

        player_action = input()

        if player_action == '1':
            alien['health'] = alien['health'] - player['attack']
            if alien['health'] <= 0:
                player_win = True
                """
                Checks if alien health is above 0, if not player wins
                """

            else:
                player['health'] = player['health'] - calculate_alien_attack()
                if player['health'] <= 0:
                    alien_win = True
                    """
                    Checks if player health is above 0, if not alien wins
                    """

        elif player_action == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_alien_attack()
            if player['health'] <= 0:
                alien_win = True

        elif player_action == '3':
            new_battle = False
            game_running = False

        else:
            print('Invalid Action')

        if player_win is False and alien_win is False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(alien['name'] + ' has ' + str(alien['health']) + ' left')

        elif player_win:
            print(player['name'] + ' wins!!')
            new_battle = False

        elif alien_win:
            print('Alien wins! GAME OVER!!')
            new_battle = False
