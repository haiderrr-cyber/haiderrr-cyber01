class ThermostatAgent:
    def __init__(self):
        self.past_temperatures = []

    def sense(self, temperature):
        self.past_temperatures.append(temperature)
        if len(self.past_temperatures) > 5:
            self.past_temperatures.pop(0)  

    def decide(self):
        if len(self.past_temperatures) < 2:
            return "No action"

        current = self.past_temperatures[-1]
        avg_trend = self.past_temperatures[-1] - self.past_temperatures[-2]

        if current < 20:
            return "Turn heating ON"
        elif current > 24:
            return "Turn cooling ON"
        elif avg_trend > 1:
            return "Temperature rising rapidly — prepare cooling"
        elif avg_trend < -1:
            return "Temperature dropping rapidly — prepare heating"
        else:
            return "Maintain current state"


agent = ThermostatAgent()
temperatures = [21, 22, 23, 24, 25, 24, 22, 20, 19]

for t in temperatures:
    agent.sense(t)
    action = agent.decide()
    print(f"Temperature: {t}°C → {action}")
