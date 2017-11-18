from random import randint, choice


def sample(population, mini=1, maxi=None) -> list:
    if maxi is None:
        maxi = len(population)
    if not maxi > mini:
        return []
    return [choice(population) for _ in range(randint(mini, maxi))]
