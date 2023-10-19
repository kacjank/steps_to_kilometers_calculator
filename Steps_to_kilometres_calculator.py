# mechanizm przeliczania #####
def counter(step_length):
    # step_length jest int-em
    steps_count = input(f'\nIle kroków dziś {ending}? ')
    # Zabezpieczenie poprawności wprowadzanych danych
    while not steps_count.isdigit():
        steps_count = input('\nBłędne dane! Podaj liczbę kroków: ')
    steps_count = int(steps_count)
    while steps_count < 0:
        steps_count = input('\nBłędne dane! Podaj liczbę kroków: ')
    print()
    distance_in_m = round(((step_length * steps_count) / 100))
    distance_in_km = round((distance_in_m / 1000), 2)
    print(f'{correct_name}, {ending} dziś {steps_count} kroków - to jest około {distance_in_m} m, czyli'
          f' około {distance_in_km} km!')
    if steps_count >= 10000:
        steps_more = steps_count - 10000
        if str(steps_more)[-1] == '2' or str(steps_more)[-1] == '3' or str(steps_more)[-1] == '4':
            steps_ending = 'kroki'
        else:
            steps_ending = 'kroków'
        print(f'Świetnie, {ending} o {steps_more} {steps_ending} więcej niż dzienne minimum '
              f'zalecane przez WHO (10 000)! Tak trzymaj!')
    else:
        steps_left = 10000 - steps_count
        if str(steps_left)[-1] == '2' or str(steps_left)[-1] == '3' or str(steps_left)[-1] == '4':
            steps_ending = 'kroki'
        else:
            steps_ending = 'kroków'
        print(f'Do przejścia dziennego minimum zalecanego przez WHO (10 000) brakuje Ci {steps_left} {steps_ending}. '
              f'Maszeruj dalej!')


############################

print('Witaj w przeliczniku ilości kroków na kilometry!\n')
name = input('Jak masz na imię? ')

while not name.isalpha():
    name = input('\nTo nie jest imię! Podaj swoje imię: ')

correct_name = name.capitalize()

if correct_name[-1] == 'a' and correct_name != 'Barnaba':
    sex = 'female'
    ending = 'przeszłaś'
else:
    sex = 'male'
    ending = 'przeszedłeś'

print(f'\nCześć {correct_name}!\n')

question = input('Czy znasz długość swojego kroku? (T/N) ')

# Zabezpieczenie poprawności wprowadzanych danych
while question != 'T' and question != 't' and question.lower() != 'tak' and question != 'N' and question != 'n' and \
        question.lower() != 'nie':
    print('\nBłędna odpowiedź. Udziel poprawnej odpowiedzi!')
    question = input('Czy znasz długość swojego kroku? (T/N) ')

if question == 'T' or question == 't' or question.lower() == 'tak':
    print('\nTo świetnie!')
    step_length = input('W takim razie jaka jest długość Twojego kroku (w centymetrach)? ')
    # Zabezpieczenie poprawności wprowadzanych danych
    while not step_length.isdigit():
        step_length = input('\nBłędne dane! Podaj długość kroku w centymetrach: ')
    # step_length = int(step_length)
    while int(step_length) > 100 or int(step_length) < 0:
        step_length = input('Błędna wartość! Podaj poprawną wartość: ')
    counter(int(step_length))
else:
    question = input('\nCzy w takim razie chcesz skorzystać z uśrednionych danych z internetu? (T/N) ')
    # Zabezpieczenie poprawności wprowadzanych danych
    while question != 'T' and question != 't' and question.lower() != 'tak' and question != 'N' and question != 'n' and \
            question.lower() != 'nie':
        print('\nUdziel odpowiedzi na pytanie!')
        question = input('Czy chcesz skorzystać z uśrednionych danych z internetu? (T/N) ')
    if question == 'n' or question == 'N' or question.lower == 'nie':
        print('\nW takim razie wróć, gdy zmierzysz już długość swojego kroku albo zmienisz zdanie.')
    else:
        height = input('\nŚwietnie, w takim razie podaj swój wzrost (w centymetrach): ')
        # Zabezpieczenie poprawności wprowadzanych danych
        while not height.isdigit():
            height = input('\nBłędne dane! Podaj swój wzrost w centymetrach: ')
        while int(height) > 250 or int(height) < 20:
            height = input('Błędna wartość! Podaj poprawną wartość: ')
        # Dopasowanie długości kroku do wzrostu
        if int(height) <= 160:  # cm
            step_length = 52  # cm
        elif 160 < int(height) <= 170:
            step_length = 55
        elif 170 < int(height) <= 180:
            step_length = 58
        elif int(height) > 180:
            step_length = 61
        counter(step_length)

input('\n(Wciśnij Enter aby zakończyć)')
