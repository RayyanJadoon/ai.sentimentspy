import colorama
import textblob
from colorama import Fore, Style
from textblox import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to the sentiment spy {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}")

if not user_name:
    user_name = "Mystery user"

conversation_history = []

print(f"{Fore.GREEN} Hello, {user_name}!")
print(f"{Fore.GEEN}Type a sentence, I will analyse the sentiment of it using textblob")
print(f"type {Fore.YELLOW} 'exit' , 'history', 'reset'")

while True:
    user_name = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()
    if not user_name:
        print(f"{Fore.RED}please enter a valid command. {Style.RESET_ALL}")