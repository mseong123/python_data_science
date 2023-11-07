from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """__str__method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="blue", hairs="light"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """__str__method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return Lannister(first_name, is_alive)
