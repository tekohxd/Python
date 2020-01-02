import webbrowser

links = open("discord_codes.txt", "r")

for line in links:
    webbrowser.open_new_tab(line)
