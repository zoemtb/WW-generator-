import random

#mogelijke karakters die in het wachtwoord voor kunnen komen:
karakters = 'abcdefghijklmnopqrstuvwqyz1234567890!@#$%^&*()_+=ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#hoeveel wachtwoorden er gemaakt moeten worden:
hoeveelheid = input('Hoeveel wachtwoorden?')
hoeveelheid = int(hoeveelheid)

#hoeveel karakters moet het wachtwoord bevatten:
lengte = input('Aantal karakters?')
lengte = int(lengte)

x = range

for p in x(hoeveelheid):
    wachtwoord = ''
    for c in x(lengte):
        wachtwoord += random.choice(karakters)
    print(wachtwoord)
            
