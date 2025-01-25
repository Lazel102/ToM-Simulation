import matplotlib.pyplot as plt

def plot_results(results,model):
    plt.figure(figsize=(10, 6))
    plt.plot(results["ToM"], label="ToM Agents")
    plt.plot(results["NonToM"], label="Non-ToM Agents")
    plt.xlabel("Steps")
    plt.ylabel("Average Resources")
    plt.title("Resource Accumulation Over Time with {model} Model")
    plt.legend()
    plt.show()

def plot_relative_difference(results,model):

    relative_difference = [
        (results["ToM"][i] - results["NonToM"][i]) / results["NonToM"][i]
        if results["NonToM"][i] != 0 else 0
        for i in range(len(results["ToM"]))
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(relative_difference, label="Relative Difference (ToM vs Non-ToM)")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # Baseline
    plt.xlabel("Steps")
    plt.ylabel("Relative Difference")
    plt.title(f"Relative Resource Difference: ToM vs Non-ToM with {model} Model")
    plt.legend()
    plt.show()