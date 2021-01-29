from random import randint
import random

pegs=['R','B','G','W','O','Y'] #Red, Blue, Green, White, Orange, Yellow
rounds=10
board=[
    ['-','-','-','-','|', '-', '-'], #color 1, color 2, color 3, color 4, |, num right place, num right color
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ['-','-','-','-','|', '-', '-'],
    ]

guess_divider=['|']
code=['X','X','X','X'] #mastermind board

#for when computer is player, will systematically eliminate
pos_sols=[]
for i in pegs:
    for j in pegs:
        for k in pegs:
            for l in pegs:
                pos_sols.append([i,j,k,l])
#all possible responses
pos_responses=[]
for i in range(5):
    for j in range(5-i):
        pos_responses.append([i,j])


def choose_code():
    global code
    sol=input('Type the 4 colors you want to put as the solution. Example: "R Y G B": \n')
    sol=sol.strip()
    sol=sol.split()
    code=sol

def generate_guess():
    return ['R', 'R', 'B', 'B']

def get_response(guess, code):
    num_right=0 #num in right spot
    num_right_color=0 #num right color
    guess2=[] #used to store pegs in guess that aren't right spot
    code2=[] #used to store pegs in code that weren't guessed correctly (right spot)
    for i in range(4):
        if guess[i]==code[i]:
            num_right+=1
        else:
            guess2.append(guess[i])
            code2.append(code[i])
    for i in range(len(guess2)):
        try:
            del code2[code2.index(guess2[i])] #try deleting the color of guess[i] from code2. If error (i.e., the color from guess[i] is not in code then....)
            num_right_color+=1 #if no error
        except:
            pass #do nothing
    return [str(num_right), str(num_right_color)]
  
def remove_impossible(guess, response, solutions):
    ret=[]
    for pos_sol in solutions: #loop thru every possible solution
        if response==get_response(guess, pos_sol): #if this pos_sol as code and guess as guess generate same response as given response
            ret.append(pos_sol) #still a possible solution
        else: #if do not receive same response
            pass #do not add, bc not a pos sol
    return ret #return solutions

def choose_next():
    minimax_guess=[]
    minimax_num=1296
    for sol in pos_sols:
        scores=[] #stores how many solutions left for each iteration
        for response in pos_responses:
            how_many_solutions_left=remove_impossible(sol, response, pos_sols)
            scores.append(len(how_many_solutions_left))
        if max(scores)<minimax_num: #if the worst case scenario of this guess is best so far
            minimax_num=max(scores)
            minimax_guess=sol
    return minimax_guess

def draw_board(rnd, guess,response):
    global board
    global guess_divider
    rnd_results=guess+guess_divider+response
    board[-1-rnd]=rnd_results
    print('Round ',rnd+1)
    for i in range(len(board)):
        print(board[i])
    print()
        
def game():
    #choose who is mastermind, skip for now
    global pos_sols
    choose_code()
    guess=generate_guess() #just for initial guess
    for i in range(rounds-1):
        response=get_response(guess,code)
        draw_board(i, guess, response)
        pos_sols=remove_impossible(guess, response, pos_sols)
        guess=choose_next()
        if response[0]=='4': #if 4 right pegs
            print('COMPUTER WINS')
            exit()
    print(pos_sols)      
while True:
    game()
