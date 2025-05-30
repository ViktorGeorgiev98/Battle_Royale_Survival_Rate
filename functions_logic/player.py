import random
import math


# BASIC PLAYER CLASS
class Basic_Player:
    """
    Basic player class to represent a player in the game.
    It only has name, gender, age, background and strategy
    """

    def __init__(self, name, gender, age, background, strategy="balanced"):
        self.name = name
        self.gender = gender.lower()
        self.age = age
        self.background = background.lower()
        self.strategy = strategy.lower()

        self.base_skill = 1.0

        # Gender modifier
        gender_multipliers = {
            "male": 1.0,  # balanced
            "female": (
                1.0 if self.strategy == "hiding" or self.strategy == "balanced" else 0.8
            ),  # smaller chance if aggressive, because males are generally physically stronger
        }
        self.M_gender = gender_multipliers.get(
            self.gender, 1.0
        )  # Default to 1.0 if unknown

        # Age penalty: -5% per year over 50
        if self.age > 50:
            self.M_age = 1 - 0.05 * (self.age - 50)
        else:
            self.M_age = 1.0

        # Background multiplier
        background_multipliers = {
            "programmer": (
                1.3 if self.strategy == "hiding" else 1.1
            ),  # bigger chance if hiding strategy, because he will think more
            "mma_fighter": (
                1.3
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.1
            ),  # higher if strategy is aggressive, because he will use his ability to fight
            "soldier": (
                1.35
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.15
            ),  # same as mma fighter, but a bit higher since he is technically trained to fight in battles
            "doctor": 1.1,  # balanced, a bit bigger because he can heal injuries better
            "construction_worker": 1.1,  # has strength from working
            "default": 1.0,  # anything else
        }
        self.M_background = background_multipliers.get(self.background, 1.0)

        # Total skill modifier
        self.skill = self.base_skill * self.M_gender * self.M_age * self.M_background

    def __repr__(self):
        return f"{self.name} | Gender: {self.gender} | Age: {self.age} | Background: {self.background} | Skill: {self.skill:.2f}"


# PLAYER WITH STRATEGY
# Let us add strategy to the class and check if it is working as expected


class Player_With_Strategy:
    """
    Same as Basic_Player but with strategy
    """

    def __init__(self, name, gender, age, background, strategy):
        self.name = name
        self.gender = gender.lower()
        self.age = age
        self.background = background.lower()
        self.strategy = strategy.lower()

        self.base_skill = 1.0

        # Gender multiplier
        gender_multipliers = {
            "male": 1.0,  # balanced
            "female": (
                1.0 if self.strategy == "hiding" or self.strategy == "balanced" else 0.8
            ),  # smaller chance if aggressive, because males are generally physically stronger
        }
        self.M_gender = gender_multipliers.get(self.gender, 1.0)

        # Age multiplier
        self.M_age = 1 - 0.05 * max(0, self.age - 50)

        # Background multiplier
        background_multipliers = {
            "programmer": (
                1.3 if self.strategy == "hiding" else 1.1
            ),  # bigger chance if hiding strategy, because he will think more
            "mma_fighter": (
                1.3
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.1
            ),  # higher if strategy is aggressive, because he will use his ability to fight
            "soldier": (
                1.35
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.15
            ),  # same as mma fighter, but a bit higher since he is technically trained to fight in battles
            "doctor": 1.1,  # balanced, a bit bigger because he can heal injuries better
            "construction_worker": 1.1,  # has strength from working
            "default": 1.0,  # anything else
        }
        self.M_background = background_multipliers.get(self.background, 1.0)

        # Strategy multiplier
        strategy_multipliers = {"aggressive": 0.8, "hiding": 0.8, "balanced": 1.0}
        self.M_strategy = strategy_multipliers.get(self.strategy, 1.0)

        # Final skill/survival multiplier
        self.skill = (
            self.base_skill
            * self.M_gender
            * self.M_age
            * self.M_background
            * self.M_strategy
        )

    def __repr__(self):
        return (
            f"{self.name} | Gender: {self.gender} | Age: {self.age} | "
            f"Background: {self.background} | Strategy: {self.strategy} | "
            f"Skill: {self.skill:.2f}"
        )


# ADD INJURY AND SICKNESS
# Redefine the class by adding injury methods and sickness methods


class Player_With_Injury_Sickness:
    """
    Same as Player_With_Strategy but with injury and sickness
    """

    def __init__(self, name, gender, age, background, strategy):
        self.name = name
        self.gender = gender.lower()
        self.age = age
        self.background = background.lower()
        self.strategy = strategy.lower()

        self.base_skill = 1.0
        self.injury_severity = 0.0  # R_injury
        self.sickness_severity = 0.0  # R_sickness

        # Gender multiplier
        gender_multipliers = {
            "male": 1.0,  # balanced
            "female": (
                1.0 if self.strategy == "hiding" or self.strategy == "balanced" else 0.8
            ),  # smaller chance if aggressive, because males are generally physically stronger
        }
        self.M_gender = gender_multipliers.get(self.gender, 1.0)

        # Age multiplier
        self.M_age = 1 - 0.05 * max(0, self.age - 50)

        # Background multiplier
        background_multipliers = {
            "programmer": (
                1.3 if self.strategy == "hiding" else 1.1
            ),  # bigger chance if hiding strategy, because he will think more
            "mma_fighter": (
                1.3
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.1
            ),  # higher if strategy is aggressive, because he will use his ability to fight
            "soldier": (
                1.35
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.15
            ),  # same as mma fighter, but a bit higher since he is technically trained to fight in battles
            "doctor": 1.1,  # balanced, a bit bigger because he can heal injuries better
            "construction_worker": 1.1,  # has strength from working
            "default": 1.0,  # anything else
        }
        self.M_background = background_multipliers.get(self.background, 1.0)

        # Strategy multiplier
        strategy_multipliers = {"aggressive": 0.8, "hiding": 0.8, "balanced": 1.0}
        self.M_strategy = strategy_multipliers.get(self.strategy, 1.0)

        # Final base survival multiplier (before dynamic updates)
        self.base_survival = (
            self.base_skill
            * self.M_gender
            * self.M_age
            * self.M_background
            * self.M_strategy
        )

    def apply_injury(self, severity):
        """Severity: 0 (none) to 1 (fatal)."""
        self.injury_severity = min(max(severity, 0), 1)

    def apply_sickness(self, severity):
        """Severity: 0 (none) to 1 (fatal)."""
        self.sickness_severity = min(max(severity, 0), 1)

    def get_survival_probability(self):
        survival = (
            self.base_survival
            * (1 - self.injury_severity)
            * (1 - self.sickness_severity)
        )
        return round(survival, 4)

    def __repr__(self):
        return (
            f"{self.name} | Skill: {self.base_survival:.2f} | "
            f"Injury: {self.injury_severity:.2f} | Sickness: {self.sickness_severity:.2f} | "
            f"Survival P: {self.get_survival_probability():.4f}"
        )


# TEAMS
# Continue with teams
# Add teams to the player class and check whether injury/sickness is fatal and add weapons


class Player_With_Teams:
    """
    Same as Player_With_Injury_Sickness but with teams and weapons
    """

    def __init__(
        self,
        name,
        age,
        gender,
        background,
        strategy,
        injury_severity=0.0,
        sickness_severity=0.0,
        has_weapon=False,
        teammates=None,
    ):
        self.name = name
        self.age = age
        self.gender = gender  # "male" or "female"
        self.background = background  # e.g., "programmer", "soldier"
        self.strategy = strategy  # "aggressive", "hiding", "balanced"
        self.injury_severity = injury_severity  # between 0 and 1
        self.sickness_severity = sickness_severity  # between 0 and 1
        self.has_weapon = has_weapon
        self.teammates = teammates or []
        self.is_alive = True

        # Base skill and multipliers
        self.base_survival = 1.0
        self.age_multiplier = self.get_age_multiplier()
        self.background_multiplier = self.get_background_multiplier()
        self.strategy_multiplier = self.get_strategy_multiplier()
        self.weapon_multiplier = 1.5 if has_weapon else 1.0
        self.gender_multiplier = self.get_gender_multiplier()

    def get_age_multiplier(self):
        return max(0.0, 1 - 0.05 * max(0, self.age - 50))

    def get_background_multiplier(self):
        background_multipliers = {
            "programmer": (
                1.3 if self.strategy == "hiding" else 1.1
            ),  # bigger chance if hiding strategy, because he will think more
            "mma_fighter": (
                1.3
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.1
            ),  # higher if strategy is aggressive, because he will use his ability to fight
            "soldier": (
                1.35
                if self.strategy == "balanced" or self.strategy == "aggressive"
                else 1.15
            ),  # same as mma fighter, but a bit higher since he is technically trained to fight in battles
            "doctor": 1.1,  # balanced, a bit bigger because he can heal injuries better
            "construction_worker": 1.1,  # has strength from working
            "default": 1.0,  # anything else
        }
        return background_multipliers.get(
            self.background.lower(), background_multipliers["default"]
        )

    def get_strategy_multiplier(self):
        strategy_multipliers = {"aggressive": 0.8, "hiding": 0.8, "balanced": 1.0}
        return strategy_multipliers.get(self.strategy.lower(), 1.0)

    def get_gender_multiplier(self):
        # Optional: you can define gender-specific multipliers
        # For now, both are neutral
        gender_multipliers = {
            "male": 1.0,  # balanced
            "female": (
                1.0 if self.strategy == "hiding" or self.strategy == "balanced" else 0.8
            ),  # smaller chance if aggressive, because males are generally physically stronger
        }
        return gender_multipliers.get(self.gender.lower(), 1.0)

    def get_team_multiplier(self):
        if not self.teammates:
            return 1.0
        compatible_backgrounds = [
            teammate.background == self.background for teammate in self.teammates
        ]
        return 1.2 if any(compatible_backgrounds) else 1.0

    def get_survival_probability(self):
        M_team = self.get_team_multiplier()
        survival = (
            self.base_survival
            * self.age_multiplier
            * self.background_multiplier
            * self.strategy_multiplier
            * self.weapon_multiplier
            * self.gender_multiplier
            * (1 - self.injury_severity)
            * (1 - self.sickness_severity)
            * M_team
        )
        survival = round(survival, 4)
        self.is_alive = survival > 0
        return survival


# PLAYER WITH THE INITIAL ZONE (PLAYERS DIE IF OUTSIDE THE ZONE)


class Player_With_Initial_Zone:
    """
    Player class that includes team mechanics and zone-awareness.

    This class models a player in a battle royale simulation with features like:
    - Survival skills based on age, gender, background, and strategy.
    - The effect of teammates with similar backgrounds.
    - Zone-based elimination (player dies if outside the zone).
    - Random events each round (injuries, sickness, finding weapons, changing teammates).
    """

    def __init__(
        self,
        name,
        age,
        gender,
        background,
        strategy,
        injury_severity=0.0,
        sickness_severity=0.0,
        has_weapon=False,
        teammates=[],
    ):
        """
        Initializes a new player with given attributes and random position.

        Args:
            name (str): Player's name.
            age (int): Age of the player (affects survival after 50).
            gender (str): 'male' or 'female'.
            background (str): Role like 'programmer', 'soldier', etc.
            strategy (str): 'aggressive', 'hiding', or 'balanced'.
            injury_severity (float): Injury level from 0 to 1.
            sickness_severity (float): Sickness level from 0 to 1.
            has_weapon (bool): Whether the player starts with a weapon.
            teammates (list): List of teammates' backgrounds.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.background = background
        self.strategy = strategy
        self.injury_severity = injury_severity
        self.sickness_severity = sickness_severity
        self.has_weapon = has_weapon
        self.teammates = teammates or []
        self.is_alive = True

        # Random position in a circular map (radius 100)
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 100)
        self.x = radius * math.cos(angle)
        self.y = radius * math.sin(angle)

        # Base survival attributes and modifiers
        self.base_survival = 1.0
        self.age_multiplier = self.get_age_multiplier()
        self.background_multiplier = self.get_background_multiplier()
        self.strategy_multiplier = self.get_strategy_multiplier()
        self.weapon_multiplier = 1.5 if has_weapon else 1.0
        self.gender_multiplier = self.get_gender_multiplier()

    def get_age_multiplier(self):
        """
        Returns a multiplier based on age.
        Players above 50 have reduced survival.
        """
        return max(0.0, 1 - 0.05 * max(0, self.age - 50))

    def get_background_multiplier(self):
        """
        Returns a multiplier based on professional background.
        Different backgrounds have strengths depending on strategy.
        """
        background_multipliers = {
            "programmer": 1.3 if self.strategy == "hiding" else 1.1,
            "mma_fighter": 1.3 if self.strategy in ["balanced", "aggressive"] else 1.1,
            "soldier": 1.35 if self.strategy in ["balanced", "aggressive"] else 1.15,
            "doctor": 1.1,
            "construction_worker": 1.1,
            "default": 1.0,
        }
        return background_multipliers.get(
            self.background.lower(), background_multipliers["default"]
        )

    def get_strategy_multiplier(self):
        """
        Returns a multiplier based on the chosen strategy.
        Aggressive and hiding strategies carry higher risk.
        """
        strategy_multipliers = {"aggressive": 0.8, "hiding": 0.8, "balanced": 1.0}
        return strategy_multipliers.get(self.strategy.lower(), 1.0)

    def get_gender_multiplier(self):
        """
        Returns a gender-based multiplier.
        Currently affects only aggressive strategy slightly.
        """
        gender_multipliers = {
            "male": 1.0,
            "female": 1.0 if self.strategy in ["hiding", "balanced"] else 0.8,
        }
        return gender_multipliers.get(self.gender.lower(), 1.0)

    def get_team_multiplier(self):
        """
        Returns a bonus multiplier if teammates share the same background.
        """
        if not self.teammates:
            return 1.0
        compatible_backgrounds = [
            background == self.background for background in self.teammates
        ]
        return 1.2 if any(compatible_backgrounds) else 1.0

    def get_survival_probability(self, zone):
        """
        Computes the probability of survival based on all modifiers.
        If outside the zone, player dies immediately.

        Args:
            zone (object): Zone with properties (center_x, center_y, radius).

        Returns:
            float: Survival probability (0.0 to 1.0).
        """
        if not self.is_alive:
            return 0.0

        if not self.is_inside_zone(zone):
            self.is_alive = False
            return 0.0

        M_team = self.get_team_multiplier()

        survival = (
            self.base_survival
            * self.age_multiplier
            * self.background_multiplier
            * self.strategy_multiplier
            * self.weapon_multiplier
            * self.gender_multiplier
            * (1 - self.injury_severity)
            * (1 - self.sickness_severity)
            * M_team
        )

        survival = round(min(survival, 1.0), 4)
        self.is_alive = survival > 0
        return survival

    def move(self):
        """
        Moves the player to a new position to simulate repositioning on the map.
        Distance is randomly chosen up to 10 units in a random direction.
        """
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, 10)
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)

    def is_inside_zone(self, zone):
        """
        Checks if player is inside the current game zone.

        Args:
            zone (object): Zone with attributes center_x, center_y, and radius.

        Returns:
            bool: True if inside the zone, False otherwise.
        """
        distance = math.sqrt(
            (zone.center_x - self.x) ** 2 + (zone.center_y - self.y) ** 2
        )
        return distance <= zone.radius

    def update_status(self):
        """
        Simulates random changes to player status during the round:
        - Chance to gain injury or sickness.
        - Chance to find a weapon.
        - Randomly change teammates (gain or lose).
        """
        if random.random() < 0.2:
            self.injury_severity += random.uniform(0.05, 0.2)

        if random.random() < 0.1:
            self.sickness_severity += random.uniform(0.05, 0.2)

        if not self.has_weapon and random.random() < 0.15:
            self.has_weapon = True
            self.weapon_multiplier = 1.5

        # Randomly gain or lose teammates with the same background
        if random.random() > 0.5:
            self.teammates.append(self.background)
        else:
            self.teammates = []

        # Clamp severity to a maximum of 1.0
        self.injury_severity = min(self.injury_severity, 1.0)
        self.sickness_severity = min(self.sickness_severity, 1.0)


# FINAL PLAYER CLASS INCLUDING ALL FEATURES

# update the class


class Final_Player:
    """
    Final player class to represent a player in the game simulation.

    Includes:
    - Positioning (x, y)
    - Age, gender, profession (background), and strategy
    - Health status: injury and sickness
    - Weapon possession
    - Team dynamics
    - Zone interaction (inside/outside penalty)
    - Survival probability computation
    - Movement simulation
    """

    def __init__(
        self,
        name,
        age,
        gender,
        background,
        strategy,
        injury_severity=0.0,
        sickness_severity=0.0,
        has_weapon=False,
        teammates=[],
    ):
        """
        Initialize a player with various attributes and randomly placed position on the map.

        Args:
            name (str): Player name.
            age (int): Player age.
            gender (str): 'male' or 'female'.
            background (str): e.g., 'soldier', 'doctor', 'programmer'.
            strategy (str): 'aggressive', 'balanced', 'hiding'.
            injury_severity (float): From 0 to 1.
            sickness_severity (float): From 0 to 1.
            has_weapon (bool): Whether the player has a weapon.
            teammates (list): Optional list of teammate backgrounds.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.background = background
        self.strategy = strategy
        self.injury_severity = injury_severity
        self.sickness_severity = sickness_severity
        self.has_weapon = has_weapon
        self.teammates = teammates or []
        self.is_alive = True

        # Random initial position
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, 100)
        self.x = radius * math.cos(angle)
        self.y = radius * math.sin(angle)

        # Multipliers
        self.base_survival = 1.0
        self.age_multiplier = self.get_age_multiplier()
        self.background_multiplier = self.get_background_multiplier()
        self.strategy_multiplier = self.get_strategy_multiplier()
        self.weapon_multiplier = 1.5 if has_weapon else 1.0
        self.gender_multiplier = self.get_gender_multiplier()

    def get_age_multiplier(self):
        """
        Older players have reduced survival chance if age > 50.
        """
        return max(0.0, 1 - 0.05 * max(0, self.age - 50))

    def get_background_multiplier(self):
        """
        Profession affects survival based on strategy compatibility.
        """
        background_multipliers = {
            "programmer": 1.3 if self.strategy == "hiding" else 1.1,
            "mma_fighter": 1.3 if self.strategy in ["balanced", "aggressive"] else 1.1,
            "soldier": 1.35 if self.strategy in ["balanced", "aggressive"] else 1.15,
            "doctor": 1.1,
            "construction_worker": 1.1,
            "default": 1.0,
        }
        return background_multipliers.get(
            self.background.lower(), background_multipliers["default"]
        )

    def get_strategy_multiplier(self):
        """
        Non-balanced strategies slightly reduce survival (higher risk).
        """
        strategy_multipliers = {"aggressive": 0.8, "hiding": 0.8, "balanced": 1.0}
        return strategy_multipliers.get(self.strategy.lower(), 1.0)

    def get_gender_multiplier(self):
        """
        Gender can impact outcome if aggressive (optional design choice).
        """
        gender_multipliers = {
            "male": 1.0,
            "female": (1.0 if self.strategy in ["hiding", "balanced"] else 0.8),
        }
        return gender_multipliers.get(self.gender.lower(), 1.0)

    def get_team_multiplier(self):
        """
        Provides a bonus if player has teammates with compatible background.
        """
        if not self.teammates:
            return 1.0
        compatible_backgrounds = [
            background == self.background for background in self.teammates
        ]
        return 1.2 if any(compatible_backgrounds) else 1.0

    def get_survival_probability(self, zone):
        """
        Calculates survival probability based on all player attributes,
        status, environment, and multipliers.

        Args:
            zone: Current zone object with method is_inside(x, y).

        Returns:
            float: Survival probability in range [0.0, 1.0].
        """
        if not self.is_alive:
            return 0.0

        # Check if player is in the zone
        in_zone = zone.is_inside(self.x, self.y)
        zone_penalty = 0.7 if not in_zone else 1.0  # 30% penalty if outside

        M_team = self.get_team_multiplier()
        survival = (
            self.base_survival
            * self.age_multiplier
            * self.background_multiplier
            * self.strategy_multiplier
            * self.weapon_multiplier
            * self.gender_multiplier
            * (1 - self.injury_severity)
            * (1 - self.sickness_severity)
            * M_team
            * zone_penalty
        )

        survival = round(survival, 4)
        self.is_alive = survival > 0
        return survival

    def move(self):
        """
        Moves the player randomly in a 2D space to simulate repositioning.
        Max movement per round is 10 units in any direction.
        """
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, 10)
        self.x += distance * math.cos(angle)
        self.y += distance * math.sin(angle)

    def is_inside_zone(self, zone):
        """
        Determines if the player is within the current safe zone.

        Args:
            zone: Zone object with center_x, center_y, and radius.

        Returns:
            bool: True if inside, False otherwise.
        """
        distance = math.sqrt(
            (zone.center_x - self.x) ** 2 + (zone.center_y - self.y) ** 2
        )
        return distance <= zone.radius

    def update_status(self):
        """
        Simulates dynamic changes in player status using probability:

        - 20% chance to receive an injury (0.05 to 0.2 severity).
        - 10% chance to get sick (0.05 to 0.2 severity).
        - 15% chance to find a weapon if the player doesn’t have one.
        - 50% chance to gain a teammate of same background, otherwise lose all teammates.

        This is analogous to **Bayesian updating**:
        we revise the player's internal state based on new simulated "evidence".
        """
        if random.random() < 0.2:
            self.injury_severity += random.uniform(0.05, 0.2)
        if random.random() < 0.1:
            self.sickness_severity += random.uniform(0.05, 0.2)
        if not self.has_weapon and random.random() < 0.15:
            self.has_weapon = True
            self.weapon_multiplier = 1.5

        # Teammate dynamics (random social interaction)
        if random.random() > 0.5:
            self.teammates.append(self.background)
        else:
            self.teammates = []

        # Clamp values to max 1.0
        self.injury_severity = min(self.injury_severity, 1.0)
        self.sickness_severity = min(self.sickness_severity, 1.0)
