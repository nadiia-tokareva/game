import random

should_continue = True

while should_continue:
    player_choice = input('Player choice: [R/S/P]  ').lower()
    if player_choice not in ['r', 'p', 's']:
        print('Not correct. Try again')
        continue

    comp_choice = random.choice(['r','p','s'])
    print('comp_choice = {}'.format(comp_choice))

    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

    if comp_choice == player_choice:
        print('It is draw.')
    elif (player_choice, comp_choice) in winning_combinations:
        print('Player is winner')
    else:
        print('Computer is winner')
    should_continue = input('Do you want play again? y/n  ') == 'y'
