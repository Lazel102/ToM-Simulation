# Simple Model
To investigate the potential adaptive advantage of Theory of Mind (ToM) in dynamic environments, we implemented a minimal agent-based model. This model simulates resource accumulation by agents with and without ToM in an environment characterized by periodic variability.

### Agent Design
The model consists of two types of agents:
1. **ToM Agents ( T = 1 )**: Adapt their resource acquisition behavior based on environmental conditions, performing better in favorable environments.
2. **Non-ToM Agents ( T = 0 )**: Follow a fixed or random strategy, unaffected by environmental variability.

### Environment
The environment alternates predictably between two states:
- ** E_{ high }**: High resource availability.
- ** E_{ low }**: Low resource availability.

### Resource Acquisition
At each time step, agents accumulate resources:
1. **ToM Agents:** Gain resources based on adaptive strategies for high ( b_{ high }) and low ( b_{ low }) resource states.
2. **Non-ToM Agents:** Gain a fixed amount ( k ) regardless of environmental state.

### Simulation Dynamics
1. Initialize  N  agents as ToM ( T = 1 ) or non-ToM ( T = 0 ).
2. Alternate environment states ( E_{ high }  and  E_{ low }) at each time step.
3. Track resource accumulation for  T  steps.

### Data Analysis
- **Average Resource Accumulation ( ̄R ):** Measured for both agent types.
- **Relative Difference:** Proportional advantage of ToM agents compared to non-ToM agents.

### Assumptions
1. ToM agents adapt to environmental conditions, not others' behavior.
2. Non-ToM agents act independently of the environment.
3. The environment alternates predictably between two states.

# Next Layer: Limited Resources and ToM Adaptation

### Changes from the Minimal Model
1. **Shared Resource Pool:**
   - Introduced a **limited resource pool** with alternating availability ( R_{ total } = 100  in high-resource and  R_{ total } = 50  in low-resource states).

2. **Adaptive ToM Behavior:**
   - ToM agents **request fewer resources in low-resource environments** (40% of the pool) and more in high-resource environments (60% of the pool), reflecting strategic adaptation.

# Current Layer: Group-Specific Cooperation (ToM)

### Changes from the Previous Layer
1. **Group Separation:**
   - Agents are divided into two groups: ToM and non-ToM.
   - Cooperation occurs only within the same group, reflecting realistic dynamics where species with different strategies do not interact.

2. **Centralized Memory:**
   - A centralized memory tracks cooperation history for all agents.
   - ToM agents use this memory to decide whether to cooperate based on the historical behavior of their partners.

3. **Resource Allocation Based on Cooperation:**
   - Cooperation outcomes determine resource distribution:
     - Both cooperate: Each receives 2 resources.
     - Both defect: Each receives 1 resource.
     - One cooperates and the other defects: The defector gets 4 resources, while the cooperator gets 0.

This layer emphasizes the role of within-group dynamics in understanding how ToM can provide adaptive advantages, isolating the impact of cooperation strategies from inter-group competition.
