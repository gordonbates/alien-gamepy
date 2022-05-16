print("""
.........................................................
.                                                       .
.                Welcome to Alien Gamepy                .
.                                                       .
.........................................................
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


player = {'name': 'Manuel', 'attack': 10, 'heal': 10, 'health': 100}
alien = {'name': 'Xenomorph XX121', 'attack': 15, 'health': 100}
game_running = True

while game_running == True:

    print('Please Select An Action\n')
    print('1. Attack')
    print('2. Heal')

    player_action = input()

    if player_action == '1':
        alien['health'] = alien['health'] - player['attack']
        player['health'] = player['health'] - alien['attack']
        print('Alien:')
        print(alien['health'])
        print('-------')
        print('Player:')
        print(player['health'])


    elif player_action == '2':
        print('Heal')
    else:
        print('Invalid Action')
    if player['health'] <= 0:
        game_running = False