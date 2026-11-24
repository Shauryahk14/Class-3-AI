#rule based travel bot
from colorama import Fore,init
import re,random
init(autoreset = True)
destinations = {"beaches": ["Bali", "Maldives", "Phuket"],"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],"cities": ["Tokyo", "Paris", "New York"]}
jokes = ["Why don't programmers like nature? Too many bugs!","Why did the computer go to the doctor? Because it had a virus!","Why do travelers always feel warm? Because of all their hot spots!"]

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def normalise_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def packing_tips():
    print(Fore.GREEN + f"TravelBot: Packing tips:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalise_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def chat():
    print(Fore.CYAN + "hello I am a travel bot")
    name = input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + "nice to meet you,{name}")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalise_input(user_input)
        if "recommend" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input:
            print(Fore.CYAN + "travelbot:goodbye")
            break
        else:
            print(Fore.RED + "travelbot:could you rephrase?")
if __name__ == "__main__":
    chat()