class PlayerMaker(object):

    PLAYER_NUMBER = 1000
    guesses_list = []
    
    def __init__(self, player_name):
        self.number = PlayerMaker.PLAYER_NUMBER
        #print(self.number)
        self.player_name = player_name
        #print(self.player_name)
        self.balance = 0
        self.guess = 0
        self.winner = True
        self.played = False
        self.busted = False
        self.difference = 0
        PlayerMaker.PLAYER_NUMBER += 1
        
        
    def deposit(self, amount):
        self.balance += amount
        print('Your account was credited: $',format(amount, '.2f'), sep='') 
        print('Current Balance: $', format(self.balance, '.2f'), sep='')
        
    def check_balance(self):
        print(self.number, '\t$',format(self.balance, '.0f'),'\t\t',self.player_name, sep="")
        
    def withdraw(self, amount):
        self.balance -= amount
        print(self.player_name, ', you lost $',format(amount, '.2f'), sep='')
        print('Current Balance: $', format(self.balance, '.2f'), sep='')
        print()
        
        
    def guess_enter(self, guess):
    
        if self.balance == 0:
            self.busted = True
        if self.busted == True:
            print('You\'re broke!  You can\'t play this hand!')
            print('Make a deposit after the hand.')
                    
        
        while guess > 100 or guess < 1:
            print('That\'s not right!')
            guess = int(input('Enter a whole number between 1 and 100: ')) 
            
        
        self.guess = guess
        self.guesses_list.append(guess)
        print()
        
        
    def guess_list_clear(self):
        self.guesses_list[:] = []
    


        
    
if __name__ == '__main__':
    account = PlayerMaker('Fred')
    account.deposit(200)
    account.check_balance()
    account.withdraw(50)