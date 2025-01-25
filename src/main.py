from model import ToMSimulation
from visualization import plot_results, plot_relative_difference

# Parameters
model = "Simple"
NUM_AGENTS = 50
STEPS = 100

# Run the simulation
simulation = ToMSimulation(num_agents=NUM_AGENTS, steps=STEPS)
results = simulation.run()

# Visualize results
plot_results(results,model)
plot_relative_difference(results,model)