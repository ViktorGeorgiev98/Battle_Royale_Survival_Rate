import random


def generate_random_players(num_players, player_class):
    """
    Generates a list of randomly initialized player objects for a battle royale simulation.

    This function simulates a diverse group of players by assigning random attributes to each one,
    such as gender, age, professional background, strategy, injuries, and weapon possession.
    It is intended to create realistic variety and unpredictability in the simulation.

    Args:
        num_players (int): The number of players to generate.
        player_class (class): The class constructor used to instantiate each player (e.g., a Player class).

    Returns:
        list: A list of player_class instances with randomized attributes.
    """

    # List of basic player names
    names = [f"Player{i+1}" for i in range(num_players)]

    # Possible attribute values
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
        # Randomly assign attributes for each player
        age = random.randint(18, 65)  # Players are adults, possibly weaker over age 50
        gender = random.choice(genders)
        background = random.choice(backgrounds)
        strategy = random.choice(strategies)
        injury_severity = round(
            random.uniform(0.0, 0.3), 2
        )  # Random light-to-moderate injuries
        sickness_severity = round(random.uniform(0.0, 0.2), 2)  # Random light illnesses
        has_weapon = random.random() < 0.3  # 30% chance the player starts with a weapon

        # Add background and strategy info to name for better traceability
        name = f"{name} - {background} - {strategy}"

        # Instantiate the player using the provided class
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
