import art 
from wikibot import WikiBot
from time import sleep

print(art.logo)
print("_______________________________________________________________________________")
print("")

print("Welcome to the random wiki page generator!")
sleep(2)
print("This program fetches a random wikipedia article from the internet.")
sleep(2)

# INITIALISE WIKIBOT
bot = WikiBot()

# FETCH A RANDOM WIKI ARTICLE
def start():
    print("Fetching...")
    sleep(2)
    article = bot.fetch_article()
    open_article = input(f"We've found an article on {article.upper()}. Would you like to read it? Type 'y' or 'n': ")
    
    
    # if the answer is yes, open the wiki page
    if open_article.lower() == "y":
        print("Opening...")
        bot.open_article(title=article)
        return
    
    # otherwise, another random report is presented
    else:
        start()


# ASK THE USER IF THEY WISH TO PROCEED 
game_end = False
while not game_end:
    print('''         
___________________________________________________________________________________________
          
          ''')  
    user_input = input("Enter 'y' if you wish to proceed... ")
        
    if user_input.lower() == "y":
        start()

    elif user_input == "n":
            print("Goodbye!")
            game_end = True
    else:
        print("That is not a correct input. Please try again.")
