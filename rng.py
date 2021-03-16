from random import randint

min_number = int(input('Vennligst skriv inn min nummer:'))
max_number = int(input('Vennligst skriv inn max nummer:'))

if (max_number < min_number):
    print('Invalid input - shutting down...')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)