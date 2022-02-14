class Action:
    def __init__(self, name, value, benefit):
        self.name = name
        self.value = value
        self.benefit = benefit

    def finalvalue(self):
        final_value = self.value*(1 + self.benefit)
        return final_value

    def displayaction(self):
        print(f'{self.name}, costing {self.value}€ with a benefit of {self.benefit} after two years ')
