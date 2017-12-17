from random import randint, choice


def choose(population) -> list:
    if not population:
        return []
    else:
        return choice(population)


def sample(population, maxi, mini=0) -> list:
    assert mini <= maxi, f"mini={mini}, maxi={maxi}"
    nbr = mini if maxi == mini else randint(mini, maxi)
    return [choose(population) for _ in range(nbr)]


def read_from_file(file):
    try:
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return []


def add_to_file(file, content):
    try:
        with open(file, 'a') as f:
            f.write(content)
    except FileNotFoundError:
        pass


def get_random_string(src, length):
    rep = str()
    for _ in range(length):
        rep += src[randint(0, len(src)-1)]
    return rep
