import matplotlib.pyplot as plt
import config

def plot_results(results, model, num_agents, steps, mean_resources, variability):
    plt.figure(figsize=(10, 6))
    plt.plot(results["ToM"], label="ToM Agents")
    plt.plot(results["NonToM"], label="Non-ToM Agents")
    plt.xlabel("Steps")
    plt.ylabel("Average Resources")
    plt.title(
        f"Resource Accumulation Over Time\nModel: {model}\nAgents: {num_agents}, Steps: {steps}, "
        f"Mean Resources: {mean_resources}, Variability: {variability}"
    )
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_relative_difference(results, model, num_agents, steps, mean_resources, variability):
    relative_difference = [
        (results["ToM"][i] - results["NonToM"][i]) / results["NonToM"][i]
        if results["NonToM"][i] != 0 else 0
        for i in range(len(results["ToM"]))
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(relative_difference, label="Relative Difference (ToM vs Non-ToM)")
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)  # Baseline
    plt.xlabel("Steps")
    plt.ylabel("Relative Difference")
    plt.title(
        f"Relative Resource Difference: ToM vs Non-ToM\nModel: {model}\nAgents: {num_agents}, Steps: {steps}, "
        f"Mean Resources: {mean_resources}, Variability: {variability}"
    )
    plt.legend()
    plt.tight_layout()
    plt.show()


def visualize_aggregated_results(aggregated_results):
    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_results["Variability"], aggregated_results["ToM"], label="ToM Agents")
    plt.plot(aggregated_results["Variability"], aggregated_results["NonToM"], label="Non-ToM Agents")
    plt.xlabel("Environmental Variability")
    plt.ylabel("Average Resources")
    plt.title(
        f"Impact of Environmental Variability on Resource Accumulation\nModel: {config.MODEL}\nAgents: {config.NUM_AGENTS}, Steps: {config.STEPS}, "
        f"Mean Resources: {config.MEAN_RESOURCES}, Simulations/Level: {config.SIMULATIONS_PER_LEVEL}"
    )
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_results["Variability"], aggregated_results["ToM_Cooperation"], label="ToM Agents - Cooperation")
    plt.plot(aggregated_results["Variability"], aggregated_results["NonToM_Cooperation"], label="Non-ToM Agents - Cooperation")
    plt.xlabel("Environmental Variability")
    plt.ylabel("Average Cooperation Rate")
    plt.title(
        f"Impact of Environmental Variability on Cooperation Rates\nModel: {config.MODEL}\nAgents: {config.NUM_AGENTS}, Steps: {config.STEPS}, "
        f"Mean Resources: {config.MEAN_RESOURCES}, Simulations/Level: {config.SIMULATIONS_PER_LEVEL}"
    )
    plt.legend()
    plt.tight_layout()
    plt.show()

