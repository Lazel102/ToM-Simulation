
# Simple Model
To investigate the potential adaptive advantage of Theory of Mind (ToM) in dynamic environments, we implemented a minimal agent-based model. This model simulates resource accumulation by agents with and without ToM in an environment characterized by periodic variability.

### Agent Design
The model consists of two types of agents:
1. **ToM Agents (\( T = 1 \))**: These agents are capable of adapting their resource acquisition behavior based on environmental conditions. They perform better in favorable environments and adjust their strategy in less favorable ones.
2. **Non-ToM Agents (\( T = 0 \))**: These agents follow a fixed or random strategy, unaffected by environmental variability.

Each agent’s resources (\( R_i \)) start at zero and accumulate over time through interactions with the environment.

### Environment

The environment alternates predictably between two states:
- **\( E_{\text{high}} \)**: High resource availability.
- **\( E_{\text{low}} \)**: Low resource availability.

The environment switches states at each time step, creating a simple form of variability.

### Resource Acquisition
At each time step, agents interact with the environment to accumulate resources:
1. **ToM Agents:**
   - Gain \( b_{\text{high}} \) resources in \( E_{\text{high}} \) and \( b_{\text{low}} \) resources in \( E_{\text{low}} \), where \( b_{\text{high}} > b_{\text{low}} \).
   - Their behavior adapts to the environment’s current state.
2. **Non-ToM Agents:**
   - Gain a fixed amount \( k \), regardless of the environment’s state.
   - Their behavior is unaffected by environmental conditions.

### Simulation Dynamics
The simulation proceeds as follows:
1. At initialization, \( N \) agents are randomly assigned as either ToM (\( T = 1 \)) or non-ToM (\( T = 0 \)).
2. At each time step:
   - The environment alternates between \( E_{\text{high}} \) and \( E_{\text{low}} \).
   - Each agent interacts with the environment to acquire resources according to their type.
3. The simulation runs for \( T \) steps, tracking resource accumulation for both ToM and non-ToM agents.

### Data Analysis
We calculated:
1. The **average resource accumulation** (\( \bar{R} \)) for ToM and non-ToM agents at each time step.
2. The **relative difference** in resource accumulation:
   \[
   \text{Relative Difference} = \frac{\text{ToM Resources} - \text{Non-ToM Resources}}{\text{Non-ToM Resources}}.
   \]
   This metric highlights the proportional advantage (or disadvantage) of ToM agents relative to non-ToM agents.

### Assumptions
1. ToM agents only adapt to environmental conditions, not the behavior of other agents.
2. Non-ToM agents act independently of environmental states.
3. The environment alternates predictably between two states.

This simple model serves as a baseline for evaluating the adaptive benefits of ToM under environmental variability and provides a foundation for introducing more complex dynamics in subsequent iterations.

# Next Layer : Limited ressources and adaption of ToM behavior based on the ressources

### **Changes from the Minimal Model**

1. **Shared Resource Pool:**
   - Introduced a **limited, shared resource pool** that agents compete for, with availability alternating between high (\( R_{\text{total}} = 100 \)) and low (\( R_{\text{total}} = 50 \)) states.

2. **Adaptive ToM Behavior:**
   - ToM agents now **request fewer resources in low-resource environments** (40% of the pool) and more in high-resource environments (60% of the pool), reflecting strategic adaptation to environmental conditions.