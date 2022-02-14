class Action:
    def __init__(self, name, value, benefit):
        self.name = name
        self.value = value
        self.benefit = benefit

    def finalvalue(self, value, benefit):
        final_value = value*(1 + benefit)
        return final_value
