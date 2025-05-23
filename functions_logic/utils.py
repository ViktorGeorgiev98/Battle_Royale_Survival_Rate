import random


def generate_random_players(num_players, player_class):
    names = [f"Player{i+1}" for i in range(num_players)]
    genders = ["male", "female"]
    backgrounds = [
        "programmer",
        "mma_fighter",
        "soldier",
        "doctor",
        "construction_worker",
        "default",
    ]
    strategies = ["aggressive", "hiding", "balanced"]

    players = []

    for name in names:
        age = random.randint(18, 65)
        gender = random.choice(genders)
        background = random.choice(backgrounds)
        strategy = random.choice(strategies)
        injury_severity = round(random.uniform(0.0, 0.3), 2)
        sickness_severity = round(random.uniform(0.0, 0.2), 2)
        has_weapon = random.random() < 0.3
        name = f"{name} - {background} - {strategy}"
        player = player_class(
            name=name,
            gender=gender,
            age=age,
            background=background,
            strategy=strategy,
            injury_severity=injury_severity,
            sickness_severity=sickness_severity,
            has_weapon=has_weapon,
        )
        players.append(player)

    return players
