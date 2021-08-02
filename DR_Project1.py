import random # importing something is always on top

def q_and_a(): #supposed to be an answer
    # list []  of question and the answer 
    # didn't need input because the answer would be choosen randomly
    # random.randrange(0, len(team)  - len of the list
    # random.choice
    quote = ['what is your favorite color? pastel colors', 'do you enjoy walking or swimming? walking', 'Anime or Cartoons?  Anime']
    random.shuffle(quote)
    print(quote[random.randrange(0,len(quote))]) # prints out one random question
    main()

def guestbook():
    
    Fname = input("What is your first name \n")

    Lname = input('What is your last name \n')

    message = input('Enter a message\n')
    profile = {} #empty dict
    
    if Fname is not profile:
            profile[Fname + " " +Lname] = message #input key and value
    print('data has been saved')
    
    # print[Fname] + [Lname + message]
    return profile  # it will recreate each time

    
def randomstate(): #() - function   [] - list/add keys  {} - sets/dicts
    stuff = ['I like coffee' , 'I am a gamer' ,  'I collect anime figures']
    print(stuff[random.randrange(0,len(stuff))])
    main()


def about_me(): #multi string
    print(' Hi, my name is Daizaria and I love anime<3!\n' , )
    main() #takes back to the menu

def main() :

#checking the menu

    print("Learn About Me !")
    print('Enter 1: about me')
    print('Enter 2: q&a')
    print('Enter 3: added to the guestbook')
    print('Enter 4: something random')
    print('Enter 5: goodbye')

    number = int(input('Pick a number: '))
    
    if number == 1:
        print (about_me())

    elif number == 2 : 
        print(q_and_a())

    elif number == 3:
        print(guestbook())

    elif number == 4:
        randomstate()

    elif number == 5:
        print("goodbye") # why did my print statement stop working?
main()

# def about_me(): #multi string
    # 1print(' Hi, my name is Daizaria and I love anime<3!' , )

# def about_me(): #multi string
#     print(' Hi, my name is Daizaria and I love anime<3!' , )


    


#q_and_a= {'what is your first name': 1 , 'what is your last name': 2, 'what is your favorite color': 3}

#random_element = random.choice(list(q_and_a.items())

#print(random_element) 






#questions
#--- how do i get the .random to work
# how to select function I want to see in the terminal. Ex: how to test specific function in the function. 


