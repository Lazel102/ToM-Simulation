import random

class Agent:
    def __init__(self, agent_id, has_tom):
        self.id = agent_id
        self.has_tom = has_tom
        self.resources = 0

    def decide_cooperation(self, memory, partner_id):
        if not self.has_tom:
            # Non-ToM agents cooperate randomly
            return random.choice([True, False])
        else:
            # ToM agents decide based on partner's history from centralized memory
            partner_history = memory.get(partner_id, [])
            if partner_history:
                # Calculate partner's cooperation rate
                cooperation_rate = sum(partner_history) / len(partner_history)
                return cooperation_rate > 0.5  # Cooperate if partner cooperates > 50% of the time
            return True  # Default to cooperation if no history exists

class ToMSimulation:
    def __init__(self, num_agents, steps):
        self.num_agents = num_agents
        self.steps = steps
        self.agents = [Agent(i, random.choice([True, False])) for i in range(num_agents)]
        self.memory = {agent.id: [] for agent in self.agents}  # Centralized memory for cooperation history

    def update_memory(self, agent_id, partner_id, action):
        # Update the cooperation history for the pair in centralized memory
        if partner_id not in self.memory:
            self.memory[partner_id] = []
        self.memory[partner_id].append(action)

    def step(self):
        # Separate agents into ToM and non-ToM groups
        tom_agents = [agent for agent in self.agents if agent.has_tom]
        nontom_agents = [agent for agent in self.agents if not agent.has_tom]

        # Shuffle and create pairs within each group
        random.shuffle(tom_agents)
        random.shuffle(nontom_agents)

        tom_pairs = [(tom_agents[i], tom_agents[i + 1]) for i in range(0, len(tom_agents), 2) if i + 1 < len(tom_agents)]
        nontom_pairs = [(nontom_agents[i], nontom_agents[i + 1]) for i in range(0, len(nontom_agents), 2) if i + 1 < len(nontom_agents)]

        # Process cooperation decisions for each group
        for agent1, agent2 in tom_pairs + nontom_pairs:
            # Each agent decides whether to cooperate
            agent1_cooperates = agent1.decide_cooperation(self.memory, agent2.id)
            agent2_cooperates = agent2.decide_cooperation(self.memory, agent1.id)

            # Update memory
            self.update_memory(agent1.id, agent2.id, agent2_cooperates)
            self.update_memory(agent2.id, agent1.id, agent1_cooperates)

            # Assign resources based on cooperation decisions
            if agent1_cooperates and agent2_cooperates:
                agent1.resources += 2
                agent2.resources += 2
            elif not agent1_cooperates and not agent2_cooperates:
                agent1.resources += 1
                agent2.resources += 1
            elif agent1_cooperates and not agent2_cooperates:
                agent1.resources += 0
                agent2.resources += 4
            elif not agent1_cooperates and agent2_cooperates:
                agent1.resources += 4
                agent2.resources += 0

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
