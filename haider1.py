import random

class Environment:
    def __init__(self):
        self.rooms = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty']),
            'C': random.choice(['Clean', 'Dirty'])
        }

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = random.choice(list(environment.rooms.keys()))
        self.cleaning_count = 0

    def sense(self):
        return self.environment.rooms[self.location]

    def clean(self):
        print(f"Cleaning room {self.location}")
        self.environment.rooms[self.location] = 'Clean'
        self.cleaning_count += 1

    def move(self):
        next_room = random.choice(list(self.environment.rooms.keys()))
        print(f"Moving from {self.location} to {next_room}")
        self.location = next_room

    def act(self):
        perception = self.sense()
        if perception == 'Dirty':
            self.clean()
        else:
            
            if all(status == 'Clean' for status in self.environment.rooms.values()):
                self.move()
            else:
                
                self.move()


env = Environment()
agent = VacuumAgent(env)

for _ in range(10):
    agent.act()

print(f"Final Environment State: {env.rooms}")
print(f"Total Cleaning Actions: {agent.cleaning_count}")
