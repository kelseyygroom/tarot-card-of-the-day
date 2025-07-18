'''
STEPS:


TO DO's
* Need to store a database of tarot cards - their numbers, and their meanings. Could probs use SQL to manage the database but may be trivial?
    -> aka just need to store them somehow - could just be in some sort of data structure like a dict but could also be a database and use SQL
       to access! apparently a JSON file is the best option for my use case
* could eventually incorporate AI features! 
    -> what does your day look like today? Anything coming up that youre anxious/excited/out of the ordinary?
    -> n then use the AI responses to analyze the user input against the card meaning and present the findings to the user. 
      {this is a much later implementation/addition}
* Develop my meanings for each card - this will be a long process
* create original art for each card. 
* develop a GUI with some animations! (can do this for now without the tarot illustrations yet - just understand the mechanics)



First iteration of my app :)     
1. Generate a random number
2. pick the card associated w that number.
3. display the card && meaning to the user (user being me for now)
    -> Give a quick description of the card
    -> Things to focus on/be aware of/notice today
    -> {potential: affirmation, song of the day}

'''

import random, json
import datetime


def draw_card():
    '''
    Function that selects random number from 1-78, selects the card associated with that number from a database. 
    Current database abstraction is a JSON file, since the database doesn't need to store any persistent user 
    data yet, and doesn't frequently change. Returns the database array entry.
    '''
    card_num = random.randint(1, 78)
    with open("cards.json", mode="r", encoding="utf-8") as file:
        db = json.load(file)

    return db[card_num]



def get_date_string():
    today = datetime.datetime.now()
    day_of_week = today.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day = today.day

    if 10 <= day <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    
    date_string = f"{days[day_of_week]}, {today.strftime("%B")} {str(day)}{suffix}, {today.year}"
    print(date_string)
    return date_string


if __name__ == "__main__":
    get_date_string()