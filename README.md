# HTW Longest Word Search

## Intention

The purpose of this repository is to find the longest word in a given text efficiently. This project aims to compare different algorithms and their performance in terms of time complexity.

## Analysis of Findings

After running multiple tests with various approaches, we observed the following results:

| Used technology | Taken Time 1x dataset | T. 4x dataset | T. 8x dataset |
|---|---|---|---|
| Pyspark_First | 19.6s, 26.8s, 22.1s<br>AVG: 22.83s | 81s, 92.5s, 89.4s<br>AVG: 87.63s | 99.4s, 97.8s, 97.4s<br>AVG: 98.2s |
| Pyspark_New | 22.7s, 22.4s, 25.8s<br>AVG: 23.63s | 88.9s, 91.7s, 89.3s<br>AVG: 89.97s | 92.6s, 97.1s, 96s<br>AVG: 95.23s |
| Python Script | 9.72s, 6.62s, 6.88s<br>AVG: 7.74s | 34.39s, 33.18s, 31.01s<br>AVG: 32.86s | 30.68s, 31.44s, 33.22s<br>AVG: 31.78s |

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## How to Run

You can use the code of this repository in multiple ways:

### Run via Notebook
Adjust the parent folder or root path in the notebook and execute all tasks

### Run as script
Adjust the ROOTPATH for your setup and execute via terminal