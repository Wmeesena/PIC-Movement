% Date June 17, 2025 
% DOC x Columbia IEOR


# PIC-Movement
Optimize PIC movement


This repository contains two Jupyter notebooks: `PIC-movement.ipynb` and `movement-example-generating.ipynb`.


## `movement-example-generating.ipynb`

This folder generates a synthetic housing information and configuration. Running this would generate a synthetic input in `\input` folder.



## `PIC-movement.ipynb`

This file will run an optimization problem to minimize the weighted sum between the number of housing units in use and the number of PIC movements. Before running this, you need to change the location of the input in this notebook. Then, this will generate an output in the `output` folder. 



# PIC‑Movement

Optimising the placement and transfer of **People In Custody (PIC)** across housing units
*Columbia IEORx DOC — June 17 2025*

---

## Overview

Efficiently assigning PIC to housing units reduces overcrowding, limits unnecessary transfers, and saves operating costs.
This repo ships two Jupyter notebooks that let you **(1)** generate a synthetic dataset and **(2)** solve a mixed‑integer optimisation model balancing

* **units opened** vs.
* **PIC movements**.

---

## Repository layout

```
PIC-Movement/
├── notebooks/
│   ├── movement-example-generating.ipynb   # create toy housing dataset
│   └── PIC-movement.ipynb                  # build & solve optimisation model
├── input/                                  # place real or synthetic data here
├── output/                                 # results (excel) are written here
└── README.md
```

---



## Notebook guide

| Notebook                                | Purpose                                                                                                                                                    | Key outputs                                         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **`movement-example-generating.ipynb`** | Generate a toy dataset of housing units, capacities, feasible housing type, and PIC attributes.                                                                                | CSV files in `input/DATE/`                               |
| **`PIC-movement.ipynb`**                | Builds a MILP that minimises  $\text{units used} + \text{WEIGHT_MOVEMENT_HOUSE}\cdot \text{PIC moves}$. Reads data from `input/`, solves with PuLP (CBC), and writes results. | `output/_DATE_/result/output_moves.xlsx` |

### Configuration

Open the first cell of **`PIC-movement.ipynb`** and edit

```python
INPUT_DIR  = "input/"
OUTPUT_DIR = "output/"
ALPHA = 1.0      # weight on number of units
BETA  = 10.0     # weight on number of movements
```

---

## Example results

Running with defaults produces:

* `output/solution.csv` — table of PIC‑to‑unit assignments
* `output/assignment_plot.png` — heat‑map of unit utilisation

(Screenshot placeholder → replace with your own image.)

---

