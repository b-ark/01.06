# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.


# не понял, зачем создавать словарь в функции, если он все равно удалится после отработки функции
# сделал так, чтобы функция возвращала полученный словарь и дозаписывала значение в словарь в мейне.
def make_country(name, capital):
    country_capital = {name: capital}
    return country_capital


answer = 'y'
countries_and_their_capitals = {}

while answer.lower() == 'y':
    country_mane = input('Type in the country\'s name: ')
    capital_mane = input('Type in the country\'s capital: ')

    countries_and_their_capitals.update(make_country(country_mane, capital_mane))
    while True:
        answer = input('Do you want to type in more countries and their capitals (y - yes, n - no)? ')
        if answer.lower() == 'y' or answer.lower() == 'n':
            break
        print('Invalid value! Try again!')

print(countries_and_their_capitals)
