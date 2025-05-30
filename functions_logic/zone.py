# INITIAL ZONE CLASS (HAS FLOWS)
import math


# Define zone class
class Zone:
    """
    Represents the dynamic safe zone in a battle royale game.

    The zone is modeled as a circle on a 2D plane, with a center point (center_x, center_y) and a radius.
    Over time (each round), the zone shrinks to encourage player movement and encounters.
    Players outside the zone take damage, so they must stay within the zone to survive.

    Attributes:
        radius (float): The current radius of the zone.
        center_x (float): The X-coordinate of the zone's center.
        center_y (float): The Y-coordinate of the zone's center.
        shrink_rate (float): The amount by which the radius shrinks each round.
    """

    def __init__(self):
        """Initializes the zone with default radius and center point."""
        self.radius = 100  # Initial size of the zone
        self.center_x = 0  # Zone starts centered at origin (0, 0)
        self.center_y = 0
        self.shrink_rate = 10  # Zone shrinks by 10 units each round

    def shrink(self):
        """
        Shrinks the zone's radius by the shrink_rate.

        The radius will not shrink below a minimum value (5 units),
        to ensure there is still a small play area left at the end of the game.
        """
        self.radius -= self.shrink_rate  # Reduce the radius
        if self.radius < 5:
            self.radius = 5  # Clamp to minimum allowed radius

    def is_inside(self, player_x, player_y):
        """
        Checks if a player is inside the current zone.

        Args:
            player_x (float): The X-coordinate of the player.
            player_y (float): The Y-coordinate of the player.

        Returns:
            bool: True if the player is within the zone radius, False otherwise.
        """
        # Calculate distance from the player to the center of the zone
        distance = math.sqrt(
            (self.center_x - player_x) ** 2 + (self.center_y - player_y) ** 2
        )
        # Player is inside the zone if their distance is less than or equal to the radius
        return distance <= self.radius
