from model import ToMSimulation
from visualization import plot_results, plot_relative_difference, visualize_aggregated_results
import config
def run_one_simulation():
    # Parameters
    model = "complex with environmental complexity"
    NUM_AGENTS = 50
    STEPS = 100

    # Run the simulation
    simulation = ToMSimulation(num_agents=NUM_AGENTS, steps=STEPS)
    results = simulation.run()

    # Visualize results
    plot_results(results,model)
    plot_relative_difference(results,model)

def run_multiple_simulations():
    aggregated_results = {
        "ToM": [],
        "NonToM": [],
        "Variability": [],
        "ToM_Cooperation": [],
        "NonToM_Cooperation": [],
    }

    for variability in config.VARIABILITY_LEVELS:
        tom_means = []
        nontom_means = []
        tom_cooperation_rates = []
        nontom_cooperation_rates = []

        for _ in range(config.SIMULATIONS_PER_LEVEL):
            simulation = ToMSimulation(
                num_agents=config.NUM_AGENTS,
                steps=config.STEPS,
                mean_resources=config.MEAN_RESOURCES,
                variability=variability,
            )
            results = simulation.run()

            # Record final average resources
            tom_means.append(results["ToM"][-1])
            nontom_means.append(results["NonToM"][-1])

            # Record final average cooperation rates
            tom_cooperation_rates.append(results["ToM_Cooperation"][-1])
            nontom_cooperation_rates.append(results["NonToM_Cooperation"][-1])

        # Aggregate results for this variability level
        aggregated_results["ToM"].append(sum(tom_means) / len(tom_means))
        aggregated_results["NonToM"].append(sum(nontom_means) / len(nontom_means))
        aggregated_results["ToM_Cooperation"].append(sum(tom_cooperation_rates) / len(tom_cooperation_rates))
        aggregated_results["NonToM_Cooperation"].append(sum(nontom_cooperation_rates) / len(nontom_cooperation_rates))
        aggregated_results["Variability"].append(variability)

    return aggregated_results


if __name__ == "__main__":
    aggregated_results = run_multiple_simulations()
    visualize_aggregated_results(aggregated_results)