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
        self.environment = "low"  # Start in a low-resource state
        self.agents = [Agent(i, random.choice([True, False])) for i in range(num_agents)]

    def step(self):
        # Alternate environment state
        self.environment = "high" if self.environment == "low" else "low"

        # Define total resource pool based on the environment
        total_resources = 100 if self.environment == "high" else 50

        # Track total resource allocation
        total_allocation = 0

        # Distribute resources among agents
        for agent in self.agents:
            # Determine the resources requested by each agent
            if agent.has_tom:
                requested = total_resources * 0.6 if self.environment == "high" else total_resources * 0.4
            else:
                requested = total_resources * random.uniform(0.3, 0.7)

            # Allocate resources without exceeding the total pool
            allocation = min(requested, total_resources - total_allocation)
            agent.resources += allocation
            total_allocation += allocation

            # Stop distributing if the pool is exhausted
            if total_allocation >= total_resources:
                break

    def run(self):
        results = {"ToM": [], "NonToM": []}

        for step in range(self.steps):
            self.step()

            # Calculate average resources for each type
            tom_agents = [a.resources for a in self.agents if a.has_tom]
            nontom_agents = [a.resources for a in self.agents if not a.has_tom]

            avg_tom = sum(tom_agents) / len(tom_agents) if tom_agents else 0
            avg_nontom = sum(nontom_agents) / len(nontom_agents) if nontom_agents else 0

            results["ToM"].append(avg_tom)
            results["NonToM"].append(avg_nontom)

        return results
