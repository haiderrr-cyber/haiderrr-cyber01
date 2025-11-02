class SmartLightAgent:
    def __init__(self):
        self.light_on = False

    def decide(self, is_dark, is_person_present):
        if is_dark and is_person_present:
            self.light_on = True
        else:
            self.light_on = False
        return self.light_on


agent = SmartLightAgent()
print(agent.decide(is_dark=True, is_person_present=True))   
print(agent.decide(is_dark=False, is_person_present=True))  
print(agent.decide(is_dark=True, is_person_present=False))  
