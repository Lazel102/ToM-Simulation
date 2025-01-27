# ToM-Simulation

## Overview

This project explores the evolution of theory of mind (ToM) using an agent-based modeling approach. The primary aim is to investigate how environmental variability and social complexity influence the development of ToM as an adaptive trait, guided by concepts such as adaptive plasticity, biological markets, and life history trade-offs.

The simulation models agents with varying cognitive capacities interacting in dynamic environments, focusing on conditions where ToM provides an evolutionary advantage.

## Motivation

Theory of mind is widely regarded as a cornerstone of advanced cognition, yet its evolution remains uneven across species. This project aims to test the hypothesis that ToM evolves in response to:

High environmental variability, which selects for flexible and predictive behaviors.
Social complexity, where cooperation, reputation management, and deception offer significant advantages.
By modeling these pressures computationally, the project seeks to address gaps in understanding the interplay between ecological and social drivers of ToM.

## Key Features

- Agent-Based Modeling: Built using Python and the Mesa library.
- Dynamic Environments: Simulates resource availability, social interactions, and environmental variability.
- Behavioral Rules: Agents with and without ToM capabilities to compare evolutionary success under different conditions.
- Data Analysis: Collect and analyze simulation data to evaluate the hypothesis.

## Getting Started

### 1. Clone the Repository
```console
git clone <repository-url>
cd ToM-Simulation
```
### 2. Set Up a Virtual Environment
```console
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```console
pip install -r requirements.txt
```
### 4. Run the Simulation
Navigate to the src/ folder and execute the main simulation script:
```console
python main.py
```

## Dependencies

- Python 3.8+
- Mesa
- Matplotlib
- Pandas

Install all dependencies via:

```console
pip install -r requirements.txt
```
## Plan

- Implement adaptive plasticity and environmental variability in agent decision-making.
- Simulate social complexity using biological markets and reputation dynamics.
- Analyze results to identify conditions favoring the evolution of ToM.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments
This project has its root in the course Human behavior, Cultures, and Societies taught by [Nicolas Baumard](https://cognition.ens.fr/fr/member/613/nicolas-baumard), [Jean-Baptiste André](https://cognition.ens.fr/fr/member/1948/jean-baptiste-andre)  &  [Marius Mercier](https://esc.dec.ens.fr/fr/membres-de-lequipe-esc-10877).
It is inspired by the work of:

- Daniel Nettle (2006) on adaptive plasticity and environmental variability.
- Pat Barclay (2016) on biological markets and social complexity.
- Kaplan et al. (2000) on life history trade-offs in evolutionary development.
