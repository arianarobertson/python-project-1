class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        # Convert inches > 12 into feet
        if self.inches >= 12:
            extra_feet = self.inches // 12
            self.feet += extra_feet
            self.inches = self.inches % 12

        # Handle negative inches by adjusting feet
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
