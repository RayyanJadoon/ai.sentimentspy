import colorama 
import textblob
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to the sentiment spy {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}")

if not user_name:
    user_name = "Mystery user"

conversation_history = []

print(f"{Fore.GREEN} Hello, {user_name}!")
print(f"{Fore.GREEN}Type a sentence, I will analyse the sentiment of it using textblob")
print(f"type {Fore.YELLOW} 'exit' , 'history', 'reset'")

while True:
    user_input = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}please enter a valid command. {Style.RESET_ALL}")

    if user_input.lower() == "exit":
        print(f"{Fore.CYAN} Exiting program.")
        break

    elif user_input.lower() == "reset":
        print(f"{Fore.CYAN} Resetting conversation.{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")

        else:           
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):


                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = ":)"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = ":|"
                else:
                    color = Fore.YELLOW
                    emoji = ":["

                print(f"{idx}: {color}{text} "
                    
                f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue


    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
    
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{sentiment_type} Sentiment detected! "
        f"Polarity: {polarity:.2f}")