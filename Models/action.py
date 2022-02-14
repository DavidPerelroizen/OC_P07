class Action:
    def __init__(self, name, value, benefit):
        self.name = name
        self.value = value
        self.benefit = benefit

    def finalvalue(self):
        """This method provides the final benefit made on an action after two years"""
        final_value = self.value*self.benefit
        return final_value

    def displayaction(self):
        """This method helps to visualize the Action infos"""
        print(f'{self.name}, costing {self.value}€ with a benefit of {self.benefit} after two years ')
