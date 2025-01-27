import random
import config
class Agent:
    def __init__(self, agent_id, has_tom):
        self.id = agent_id
        self.has_tom = has_tom
        self.resources = 0
        self.alpha = random.uniform(0, 1) if has_tom else None  # ToM agents get a sampled alpha
        self.cooperated = random.choice([True, False])
    def decide_cooperation(self, memory, partner_id, resource_availability):
        """
        Decide whether to cooperate based on self-prediction and partner prediction probabilities.
        """
        if not self.has_tom:
            # Non-ToM agents cooperate randomly
            self.cooperated = random.choice([True, False])
        else:
            # Retrieve partner's history
            partner_history = memory.get(partner_id, [])
            observed_cooperation_rate_partner = sum(partner_history) / len(partner_history) if partner_history else 0
            # Retrieve own history
            own_history = memory.get(self.id, [])
            # Retrieve partner's history
            partner_history = memory.get(partner_id, [])
            observed_cooperation_rate_partner = sum(partner_history) / len(partner_history) if partner_history else 0
            # Retrieve own history
            own_history = memory.get(self.id, [])
            observed_cooperation_rate_self = sum(own_history) / len(partner_history) if partner_history else 0

            # Self-prediction: Predict the probability of self-cooperation
            self_prediction = self.predict_cooperation(observed_cooperation_rate_self, resource_availability)

            # Partner prediction: Predict the probability of partner cooperation
            partner_prediction = self.predict_cooperation(observed_cooperation_rate_partner, resource_availability)

            # Self-prediction: Predict the probability of self-cooperation
            self_prediction = self.predict_cooperation(observed_cooperation_rate_self, resource_availability)

            # Partner prediction: Predict the probability of partner cooperation
            partner_prediction = self.predict_cooperation(observed_cooperation_rate_partner, resource_availability)

            # Combine probabilities using alpha
            combined_probability = self.alpha * self_prediction + (1 - self.alpha) * partner_prediction

            # Decide to cooperate based on combined probability
            self.cooperated = random.random() < combined_probability

        return self.cooperated

    def predict_cooperation(self, observed_cooperation_rate, total_resources):
        """
        Predict the probability of cooperation under given conditions.
        Combines normalized environmental context and observed behavior.
        Returns a probability between 0 and 1.
        """
        # Normalize total_resources around mean with a defined range
        normalized_resources = max(0, min(1, (total_resources - config.MEAN_RESOURCES) / (2 * config.MEAN_RESOURCES)))

        # Weighted baseline probability to make observed behavior more impactful
        resource_weight = 0.5  # Weight given to environmental context
        behavior_weight = 1 - resource_weight  # Complementary weight for observed behavior

        baseline_probability = normalized_resources * resource_weight
        predicted_probability = (baseline_probability + (behavior_weight * observed_cooperation_rate))

        return max(0, min(1, predicted_probability))  # Ensure probabilities remain between 0 and 1


class ToMSimulation:
    def __init__(self, num_agents, steps, mean_resources, variability):
        self.num_agents = num_agents
        self.steps = steps
        self.mean_resources = mean_resources
        self.variability = variability
        self.agents = [Agent(i, random.choice([True, False])) for i in range(num_agents)]
        self.memory = {agent.id: [] for agent in self.agents}  # Centralized memory
        self.cooperation_log = {"ToM": [], "NonToM": []}  # Track cooperation rates separately

    def update_memory(self, agent_id, partner_id, action):
        if partner_id not in self.memory:
            self.memory[partner_id] = []
        self.memory[partner_id].append(action)

    def step(self):
        total_resources = max(0, random.gauss(self.mean_resources, self.variability))  # Resource availability

        tom_agents = [agent for agent in self.agents if agent.has_tom]
        nontom_agents = [agent for agent in self.agents if not agent.has_tom]

        random.shuffle(tom_agents)
        random.shuffle(nontom_agents)

        tom_pairs = [(tom_agents[i], tom_agents[i + 1]) for i in range(0, len(tom_agents), 2) if i + 1 < len(tom_agents)]
        nontom_pairs = [(nontom_agents[i], nontom_agents[i + 1]) for i in range(0, len(nontom_agents), 2) if i + 1 < len(nontom_agents)]

        total_allocation = 0
        for agent1, agent2 in tom_pairs + nontom_pairs:
            agent1_cooperates = agent1.decide_cooperation(self.memory, agent2.id, total_resources)
            agent2_cooperates = agent2.decide_cooperation(self.memory, agent1.id, total_resources)

            self.update_memory(agent1.id, agent2.id, agent2_cooperates)
            self.update_memory(agent2.id, agent1.id, agent1_cooperates)

            allocation = min(2, total_resources - total_allocation) if agent1_cooperates and agent2_cooperates else \
                min(1, total_resources - total_allocation) if not agent1_cooperates and not agent2_cooperates else \
                min(4, total_resources - total_allocation)

            agent1.resources += allocation
            agent2.resources += allocation
            total_allocation += allocation * 2

            if total_allocation >= total_resources:
                break

        # Log cooperation rates for this step
        tom_cooperation = [agent.cooperated for agent in tom_agents]
        nontom_cooperation = [agent.cooperated for agent in nontom_agents]

        self.cooperation_log["ToM"].append(sum(tom_cooperation) / len(tom_cooperation) if tom_cooperation else 0)
        self.cooperation_log["NonToM"].append(sum(nontom_cooperation) / len(nontom_cooperation) if nontom_cooperation else 0)

    def run(self):
        results = {"ToM": [], "NonToM": [], "ToM_Cooperation": [], "NonToM_Cooperation": []}

        for step in range(self.steps):
            self.step()

            tom_agents = [a.resources for a in self.agents if a.has_tom]
            nontom_agents = [a.resources for a in self.agents if not a.has_tom]

            avg_tom = sum(tom_agents) / len(tom_agents) if tom_agents else 0
            avg_nontom = sum(nontom_agents) / len(nontom_agents) if nontom_agents else 0

            results["ToM"].append(avg_tom)
            results["NonToM"].append(avg_nontom)
            results["ToM_Cooperation"].append(self.cooperation_log["ToM"][-1])
            results["NonToM_Cooperation"].append(self.cooperation_log["NonToM"][-1])

        return results
