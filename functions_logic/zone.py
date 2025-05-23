# INITIAL ZONE CLASS (HAS FLOWS)
import math


# Define zone class
class Zone:
    """
    This class represents the initial zone in a battle royale game.
    The zone shrinks over time, and players must stay within the zone to avoid damage.
    The zone has a center point and a radius that defines its size.
    The zone shrinks by a fixed amount each round, and players outside the zone take damage.
    The zone is represented as a circle on a 2D plane.
    """

    def __init__(self):
        self.radius = 100  # Initial radius of the zone
        self.center_x = 0  # X-coordinate of the center of the zone
        self.center_y = 0  # Y-coordinate of the center of the zone
        self.shrink_rate = 10  # How fast the zone shrinks per round

    def shrink(self):
        """Shrinks the zone by the shrink_rate each round."""
        self.radius -= self.shrink_rate
        if self.radius < 5:
            self.radius = 5  # Ensure the radius doesn't go below a small enough space for players to fight in

    def is_inside(self, player_x, player_y):
        """Checks if the player is inside the current zone."""
        distance = math.sqrt(
            (self.center_x - player_x) ** 2 + (self.center_y - player_y) ** 2
        )
        return distance <= self.radius
