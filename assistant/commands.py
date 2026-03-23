# assistant/commands.py
import os
import webbrowser
import subprocess

BASE_USER_PATH = os.path.expanduser("~")

# ---------- SYSTEM COMMANDS ----------

def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Chrome opened"

def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Notepad opened"

def open_folder(folder_name):
    # Agar user full path deta hai
    if ":\\" in folder_name:
        path = folder_name
    else:
        path = os.path.join(BASE_USER_PATH, folder_name)

    if os.path.exists(path):
        os.startfile(path)
        return f"Opened folder: {path}"
    else:
        return "Folder not found"

# ---------- SEARCH COMMANDS ----------

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching Google for: {query}"

def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    return f"Searching YouTube for: {query}"

def amazon_search(query):
    url = f"https://www.amazon.in/s?k={query}"
    webbrowser.open(url)
    return f"Searching Amazon for: {query}"

def unknown_command():
    return "Sorry, command samajh nahi aayi"
