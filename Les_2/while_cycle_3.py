import os

while True:
    site = input("Enter a website:\n")
    if site == "quit":
        break

    if 'https://' in site:
        os.system('start ' + site)

    elif 'www.' in site:
        site = 'https://' + site
        os.system('start ' + site)

    else:
        site = 'https://www.' + site
        os.system('start ' + site)
