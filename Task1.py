# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.


def favorite_movie(title):
    print(f'My favorite movie is named {title}.')


favorite_movie('Pulp Fiction')
answer = '1'
# даём возможность пользователю изменить его любимый фильм
while True:
    answer = input('Do you want to change your mind about your favorite movie (y - yes, n - no)? ')
    if answer.lower() == 'y' or answer.lower() == 'n':
        break
    print('Invalid value! Try again!')

if answer == 'y':
    favorite_movie(input('Type in the name of your new favorite movie: '))
