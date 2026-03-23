# assistant/main.py
from commands import *
from utils import normalize

print("LEO - Local Environment Operator started 🚀")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ")
    command = normalize(user_input)

    if command == "exit":
        print("LEO: Bye 👋")
        break

    elif "open chrome" in command:
        print("LEO:", open_chrome())

    elif "open notepad" in command:
        print("LEO:", open_notepad())

    elif command.startswith("open folder"):
        folder = command.replace("open folder", "").strip()
        print("LEO:", open_folder(folder))

    elif command.startswith("google search"):
        query = command.replace("google search", "").strip()
        print("LEO:", google_search(query))

    elif command.startswith("youtube search"):
        query = command.replace("youtube search", "").strip()
        print("LEO:", youtube_search(query))

    elif command.startswith("amazon search"):
        query = command.replace("amazon search", "").strip()
        print("LEO:", amazon_search(query))

    else:
        print("LEO:", unknown_command())
