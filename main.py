import random
import re #process user input
from colorama import Fore,init #colored input in the terminal
init(autoreset=True)
#travel options
places={
    "Beach": ["Maldives", "Bali", "Hawaii", "Diani", "Zanzibar", "Phuket"],
    "Mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Kilimanjaro", "Andes", "Atlas Mountains"],
    "City": ["New York", "Paris", "Tokyo", "Copenhagen", "London", "Nairobi","Mombasa", "Paris", "CapeTown"],
    "Rivers": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River", "Danube River", "Ganges River"],
    "Desert": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Mojave Desert", "Thar Desert", "Atacama Desert"],
    "Forest": ["Amazon Rainforest", "Congo Rainforest", "Daintree Rainforest", "Black Forest", "Taiga Forest", "Redwood Forest"],
    "Oceans": ["Pacific", "Indian", "Atlantic", "Southern", "Arctic", "Antarctic", "Artic", "Southern Ocean"],
    "Countries": ["Italy", "France", "Japan", "Australia", "Brazil", "South Africa", "Kenya", "Morocco", "Spain", "Greece", "Nigeria", "Congo", "Morocco", "Niger"],
}
#function-clean user input
def clean(text):
    return re.sub(r"\s+"," ",text.strip().lower())#converts the text to lower case, removes special charactes and unecessary spaces
#suggest the place of travel
def suggest_place():
    print (Fore.LIGHTMAGENTA_EX+"Bot:Which type of place do you want to go?")
    trip_type=clean(input(Fore.BLUE+"You: "))
    if trip_type in places:
        destination=random.choice(places[trip_type])
        print (Fore.GREEN+f"Bot: You should try out {destination}.")
    else:
        print (Fore.RED+"Bot: Sorry, I can't make a suggestion for that category.")
#display the menu
def menu():
    print(Fore.YELLOW+"Bot: Travelling Suggestions!")
    print(Fore.YELLOW+("⏺ Type 'travel' to get suggestion menu"))
    print(Fore.YELLOW+("⏺ Type 'exit' to quit"))
#main function
def chat():
    print(Fore.CYAN+"🙃Welcome to TravelBot!")
    #display the menu
    menu()
    while True:
        user_input=clean(input(Fore.MAGENTA_"You: "))
        if 'travel' in user_input or "suggest" in user_input:
            #display the travelling options
            suggest_place()            
        elif 'exit' in user_input or "quit" in user_input or 'close' in user_input:
            print(Fore.LIGHTCYAN_EX+"Goodbye..........")
        else:
            print(Fore.YELLOW+"Sorry I cannot understand the command")
if __name__=="__main__":
    chat()