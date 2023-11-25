from random import choice, randint


def __random_phone_numbers():
    prefixos = ["629", "669", "419"]
    prefixo = choice(prefixos)
    resto_n = randint(80000000, 99999999)
    return f'{prefixo}{resto_n}'


def __random_id():
    random_n = randint(0,99)
    return random_n

print(__random_id())