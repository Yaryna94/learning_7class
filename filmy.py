import random
from datetime import date

GENRE = {
    'A': 'Akcia',
    'K': 'Komedia',
    'D': 'Drama',
    'H': 'Horror',
    'S': 'Sci-Fi',
    'F': 'Fantastic'
}

YN = [
    'Y',
    'N'
]

TEXT = [
    'Додати{0} позицію? Y/N: ',
    'Хочеш переглянути{0} фільми/серіали? Y/N: '
]

UNITS = {
    '1': ['один', 'перший'],
    '2': ['два', 'другий'],
    '3': ['три', 'третій'],
    '4': ['чотири', 'четвертий'],
    '5': ['пять', 'пятий'],
    '6': ['шість', 'шостий'],
    '7': ['сім', 'сьомий'],
    '8': ['вісім', 'восьмий'],
    '9': ['девять', 'девятий'],
    '10': 'десятий'
}


def change_to_word(to_change):
    if to_change[0] == '0':
        word = UNITS[to_change[1]][1]
    elif to_change == '10':
        word = UNITS[to_change]
    elif to_change[0] == '1':
        word = UNITS[to_change[1]][0] + "nasty"
    else:
        if to_change[1] == '0':
            word = UNITS[to_change[0]][0] + "dziesty"
        else:
            word = UNITS[to_change[0]][0] + "dziesty " + UNITS[to_change[1]][1]
    return word


class Movie:
    def __init__(self, title, release_year, genre, viewed=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        # Variable
        self.viewed = viewed

    def play(self):
        self.viewed += 1

    def __str__(self):
        return f'{self.title} ({self.release_year}) '


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} - S{self.season}E{self.episode} - сезон {change_to_word(self.season)}, серія {change_to_word(self.episode)}.'


def get_movies(lib):
    return get(Movie, lib)


def get_series(lib):
    return get(Series, lib)


def get(ms_type, lib):
    filtered_library = []
    for record in lib:
        if type(record) == ms_type:
            filtered_library.append(record)
    sorted_by_title = sorted(filtered_library, key=lambda movie: movie.title)
    return sorted_by_title


def search(lib):
    z = input('Який фільм\серіал шукаєш? Напиши назву: ')
    found = False
    for i in lib:
        if i.title.upper() == z.upper():
            searched = i
            found = True
            break
    if found:
        while True:
            x = input(f'Знайшла {searched} хочеш подивитися? Y/N: ')
            if check_dict(x, YN):
                if x.upper() == "Y":
                    searched.play()
                    print('Є така назва - viewed +1')
                else:
                    break
    else:
        print('Не знайшла такої назви.')


def generate_views(lib):
    pick_title = random.choice(lib)
    pick_title.viewed += random.randint(1, 100)


def g10(lib):
    for i in range(10):
        generate_views(lib)


def choose(lib):
    x = input('Фільм/Серіал - F/S: ')
    return generate(x, lib)


def check_dict(x, y):
    return x.upper() in y


def check_int(x):
    while True:
        try:
            w = int(x)
        except ValueError:
            w = input('Напиши номер від 1 дo 99: ')
        else:
            if w in range(1, 100):
                return w
            else:
                x = input('Напиши номер від 1 дo 99: ')


def generate(x, lib):
    title = input('Напиши назву: ')
    release_year = input(f'Напиши рік випуску ({title}): ')
    while True:
        check_genre = input(
            f'Напиши жанр ({title}) - (H)orror / (S)ci-Fi / (F)antastyka / (A)kcja / (D)ramat / (K)omedia: ').upper()
        if check_dict(check_genre, GENRE):
            genre = GENRE[check_genre]
            break
    if x.upper() == 'S':
        episode = str(check_int(input('Напиши номер серії: '))).zfill(2)
        season = str(check_int(input('Укажи номер сезону: '))).zfill(2)
        new = Series(episode, season, title, release_year, genre)
    else:
        new = Movie(title, release_year, genre)
    lib.append(new)
    return lib

def next_operation(y, operation_type):
    while True:
        x = input(TEXT[operation_type].format(y))
        if check_dict(x, YN):
            return x.upper() == 'Y'


def add_new(lib):
    choose_bool = next_operation('', 0)
    while choose_bool:
        choose(lib)
        choose_bool = next_operation(' наступна', 0)

    choose_bool = next_operation('', 1)
    if choose_bool:
        print('Доступні фільми: ')
        [print(item) for item in get_movies(lib)]
        print('\n')
        print('Доступні серіали: ')
        [print(item) for item in get_series(lib)]
        print('\n')


def top_titles(library_list):
    by_popularity = sorted(library_list, key=lambda movie: movie.viewed, reverse=True)
    return by_popularity[:3]


if __name__ == "__main__":
    print('Бібліотека фільмів')
    library = [Movie('DIe hard', 1988, 'Akcja'), Movie('Scam', 2000, 'Komedia'),
               Movie('Joker', 2019, 'Drama'), Series('01', '01', 'South Park', 1996, 'Komedia')]
    add_new(library)
    search(library)
    generate_views(library)
    g10(library)

    print(f'\nНайпопулярніші фільми і серіали дня {date.today().day}-{date.today().month}-{date.today().year}: ')
    [print(f"{i + 1}. {top_titles(library)[i]}") for i in range(3)]