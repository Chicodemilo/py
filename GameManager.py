from PlayerMaker import *
import random

class GameManager(object):

    def __init__(self):
        self.accounts = []
        
    def create_player(self, player_name): 
        player = PlayerMaker(player_name)
        self.name = player.player_name
        self.number = player.number
        print()
        print('** Welcome ', self.name, '. Your account number is: ', self.number, ' **', sep='')
        player.deposit(10)
        self.accounts.append(player)

        
    def deposit(self, name, amount):
        this_account = None
        for account in self.accounts:
            if account.player_name == name:
                this_account = account
                break
        if this_account:
            if this_account.balance > 0:
                print('You can only deposit into your account when your balance is $0.00')
                print('You have $',format(this_account.balance, '.2f'),' in your account', sep='')
            else:
                print('We\'re depositing $%d into your account' % 10)
                this_account.deposit(10)
        else:   
            print()
            print('** No one here has that name **')
        
        
    def check_accounts(self):
        print()
        print('Number \tBalance\t\tName')
        print('-----------------------------')
        for x in self.accounts:
            x.check_balance()
        print()
        
    
            
        
        
    counter = 1000
    hand_counter = 1    
    def bet(self):
        for clear in self.accounts:
            clear.played = False
            clear.guess = 0
            #print(clear.player_name, clear.played) #Testing that I reset everything
            
        if GameManager.hand_counter == 1:
            print()
            print('       ************** GAME NUMBER',GameManager.hand_counter,'**************')
            print('I\'m thinking of a number between 1 and 100.')
            print('Every player will guess what they think the number is.')
            print('The player with the closest guess wins.') 
            print('The winning player gets $1.00 from every other player.')
            print('The winner gets $2.00 from every player if they guess the number exactly!')
    
        else:
            print()
            print('       ************** GAME NUMBER',GameManager.hand_counter,'**************')
            print('I\'m thinking of a new number between 1 and 100')
        
        GameManager.hand_counter += 1

        first_up = None
        
        for turn in self.accounts:
            if turn.number == GameManager.counter:
                first_up = turn
                break
        if first_up:
            turn.guess_list_clear()
            print()
            print(turn.player_name, ', it\'s your turn to guess first.', sep="")
            
            while True:
                try:
                    guess = int(input('What number do you guess: '))
                    break
                except ValueError:
                    print('Please enter a whole number: ')
                    continue
            
            turn.guess_enter(guess)
            
            #print(turn.guess) #Testing The Guess
            turn.played = True
            
            next_player = GameManager.counter + 1
            
            GameManager.counter += 1
            
            max_counter = 1000 + len(self.accounts) -1
            #print(max_counter) #Testing max_counter
            if GameManager.counter > max_counter:
                next_player = 1000           
            
            
            for next in self.accounts:
                if next.number == next_player:
                    if next.played == False:
                        print(next.player_name, ', it\'s your turn to guess.', sep="")
                        
                        while True:
                            try:
                                guess = int(input('What number do you guess: '))
                                break
                            except ValueError:
                                print('Please enter a whole number: ')
                                continue                        
                        
                        
                        guess = self.double_check(guess)
                        
                        next.guess_enter(guess)
                        
                        next.played = True
                        
                        next_player += 1
                        
                        next_max_counter = 1000 + len(self.accounts) -1
                        if next_player > next_max_counter:
                            next_player = 1000
                            
                            for even_next in self.accounts:
                            
                                if even_next.number == next_player:
                                    #print('Test') #Testing that I made it into this loop
                                    if even_next.played == False:
                                        print(even_next.player_name, ', it\'s your turn to guess', sep="")

                                        while True:
                                            try:
                                                guess = int(input('What number do you guess: '))
                                                break
                                            except ValueError:
                                                print('Please enter a whole number: ')
                                                continue

                                        guess = self.double_check(guess)
                                        
                                        even_next.guess_enter(guess)
                                        
                                        even_next.played = True
                                        next_player += 1
                                        
            self.run_game()
            self.pay_out()
                        
            #print(turn.guesses_list) #Testing the guesses_list                       
            if GameManager.counter > max_counter:
                GameManager.counter = 1000  
                
                
    def double_check(self, guess):
        checker = True
        while checker == True:
            if guess in PlayerMaker.guesses_list:
                checker = True
                guess = int(input('That number has been picked! Try again: '))
            else:
                checker = False
        return guess
        
    doubler = None    
    def run_game(self):
        picked_number = random.randint(1, 100)
        print('        ****************************************')
        print('        Here\'s the number I was thinking of: ', picked_number)
        diff_list = []
        print()
        print('Guess \tDifference \tPlayer')
        print('--------------------------------')
        for diff in self.accounts:
            diff.difference = picked_number - diff.guess
            if diff.difference < 0:
                diff.difference *= -1
            print(diff.guess, '\t' ,diff.difference, '\t\t',diff.player_name, sep='')
            diff_list.append(diff.difference)
            
        diff_list.sort()
        #print(diff_list) #Testing Sorting the Dist List
            
        for winner in self.accounts:
            if winner.difference == diff_list[0]:
                winner.winner = True
            else:
                winner.winner = False
                
        GameManager.doubler = diff_list[0]
                
                
    def pay_out(self):
        #print('Test Doubler Value', GameManager.doubler) #Testing Doubler Value
        print()
        pot = 0
        
        if GameManager.doubler == 0:
            print('  ********* EXACT GUESS *********')
            for money in self.accounts:
                if money.winner == False:
                    money.withdraw(2)
                    pot += 2
                    
            for money in self.accounts:
                if money.winner == True:
                    print('  **********',money.player_name,'You Won **********')
                    money.deposit(pot)
        
        else:
            for money in self.accounts:
                if money.winner == False:
                    money.withdraw(1)
                    pot += 1
                
            for money in self.accounts:
                if money.winner == True:
                    print('  ******',money.player_name,'You Won ******')
                    money.deposit(pot)
            
        
        
        
            
            
            
            













 
            
            