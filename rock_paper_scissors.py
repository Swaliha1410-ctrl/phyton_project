import random
emojis={'r':'👊','p':'🖐🏻','s':' ✂'}
c='rps'
count_comp=0
count_user=0
comp_ch=random.choice(c)
for i in range (3):
    try:
       for i in c:
        user_ch=input('Choose stone,paper or scissors(r/p/s)').lower()
        print(f'your choice:-{emojis[user_ch]}')
        print(f'computer choice:-{emojis[comp_ch]}') 
        if  comp_ch==user_ch:
            i+=1
        elif (comp_ch=='r' and user_ch=='p') or (comp_ch=='s' and user_ch=='r') or (comp_ch=='p' and user_ch=='s'):
            count_user+=1
            i+=1
        else:
            count_comp+=1
            i+=1
    except:
        print('invalid choice,enter valid input')

if count_comp>count_user:
    print(f'final your count:- {count_user}" : " computer count:- {count_comp} You lose ☹')
elif count_comp<count_user:
    print(f'final count :- {count_user}" : " computer count:- {count_comp} you won ☺')
else:
    print('it"s a tie!!')
     

