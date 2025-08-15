class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches = self.inches % 12

        if self.inches < 0:
            self.feet -= 1
            self.inches += 12

    def __sub__(self, other):
        feet_diff = self.feet - other.feet
        inches_diff = self.inches - other.inches
        result = Height(feet_diff, inches_diff)
        result.normalize()
        return result

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

    def __lt__(self, other):
        return (self.feet, self.inches) < (other.feet, other.inches)

    def __le__(self, other):
        return (self.feet, self.inches) <= (other.feet, other.inches)

    def __eq__(self, other):
        return (self.feet, self.inches) == (other.feet, other.inches)

    def __gt__(self, other):
        return (self.feet, self.inches) > (other.feet, other.inches)

    def __ge__(self, other):
        return (self.feet, self.inches) >= (other.feet, other.inches)

    def __ne__(self, other):
        return (self.feet, self.inches) != (other.feet, other.inches)
