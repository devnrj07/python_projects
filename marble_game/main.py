import random

bag = ('black','green','red','green', 'red', 'red','green','green','green','white')
wallet = 1000
result = 0
rounds = random.randint(1,30)
marble = ''
current_win = wallet

print(f'You start the game with {wallet} gold pieces')

for draw in range(1,rounds+1):
    
    bet = int(input(f'Current Purse: {current_win} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
    if(bet > current_win):
        print(f'oops! you don\'t have enough gold coins. Your current purse is {current_win}')
        continue
     
    marble = random.choice(bag)

    if marble == 'green':
        result = bet 

    elif marble == 'black':
        result = 2 * bet 

    elif marble == 'white':
        result = -1.5 * bet       

    else:
        result = -bet

    current_win += result

    if current_win < 0.5 * wallet:
        print(f'You have spent too much for today!! \n last draw {marble}')
        break

    print(f'purse: {wallet}, last result: ({marble}): {result}')
    print('')

# print final results
print('starting/ ending purse: ', wallet, '/',current_win)
print('gain/loss: ', ((current_win-wallet)/wallet *100),'%')