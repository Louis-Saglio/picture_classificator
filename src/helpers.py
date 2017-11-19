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
