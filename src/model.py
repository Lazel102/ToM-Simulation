import random

class Agent:
    def __init__(self, agent_id, has_tom):
        self.id = agent_id
        self.has_tom = has_tom
        self.resources = 0

    def act(self, environment):
        if self.has_tom:
            # ToM agents adapt based on environment state
            if environment == "high":
                self.resources += 2  # Higher gain in favorable conditions
            else:
                self.resources += 1
        else:
            # Non-ToM agents act randomly
            self.resources += random.choice([1, 2])

class ToMSimulation:
    def __init__(self, num_agents, steps):
        self.num_agents = num_agents
        self.steps = steps
        self.environment = "low"  # Initial state
        self.agents = [Agent(i, random.choice([True, False])) for i in range(num_agents)]

    def step(self):
        # Alternate environment state
        self.environment = "high" if self.environment == "low" else "low"
        # Agents act based on the current environment
        for agent in self.agents:
            agent.act(self.environment)

    def run(self):
        results = {"ToM": [], "NonToM": []}
        for _ in range(self.steps):
            self.step()
            # Record average resources for both agent types
            tom_agents = [a.resources for a in self.agents if a.has_tom]
            nontom_agents = [a.resources for a in self.agents if not a.has_tom]
            results["ToM"].append(sum(tom_agents) / len(tom_agents))
            results["NonToM"].append(sum(nontom_agents) / len(nontom_agents))
        return results
