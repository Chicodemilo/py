from GameManager import *

def main():
    print()
    print()
    print('            ***************************')
    print('            *** Welcome To Wagerer! ***')
    print()
    print('Please add a few players, then play a game.')
    
    game = GameManager()
    
    action = 'X'
    
    while action != 'Q':
        print()
        print('What would you like to do:')
        print('A : Add a Player')
        print('P : Play A Game')
        print('C : Check Player Balances')
        print('D : Deposit Into An Account')
        print('Q : Quit')
         
        action = input('Enter Your Choice: ')
        action = action.upper()
        
        if action == 'A':
            name = input('Enter the player name: ')
            player_name = game.create_player(name)
            
            
            
        if action == 'C':
            game.check_accounts()
            
            
        if action == 'D':
            name = input('Please enter the player name: ')
            print()
            game.deposit(name, 20)
            
        if action == 'P':
            game.bet()
            
            
    print()        
    print('           ** Thanks for Playing Wagerer **')        
    print('           *********** Goodbye ************')
    print()
            
main()