import random

word_list=["python", "jumble", "easy", "difficult", "answer",  "xylophone",'apple']

word=random.choice(word_list)

display=[]

for i in range(len(word)):
    display+='_'
    
print(display)
game_over=False
lives=6
while not game_over:
    
    user_guess=input("enter the gussed character")
    
    for p in range(len(word)):
        l=word[p]
        if l == user_guess:
            display[p]=user_guess
    print(display)
            
    if user_guess not in word:
        lives-=1
        if lives==0:
            game_over = True
            print("game lost")
    if '_' not in display:
        game_over = True
        print("game Win")
                  
    
    


