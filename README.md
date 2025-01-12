# HTW Longest Word Search

## Intention

The purpose of this repository is to find the longest word in a given text efficiently. This project aims to compare different algorithms and their performance in terms of time complexity.

## Analysis of Findings

After running multiple tests with various approaches, we observed the following results:

| Used technology | Average Time 1x dataset | Av. T. 4x dataset | Av. T. 8x dataset
|---|---|---|---|
| Pyspark_First | 22.83 s | 87.63 s |  |
| Pyspark_New | 23.63 s |  |  |
| Python Script | 7.74 s |  |  |

| Used technology | Taken Time 1x dataset | T. 4x dataset | T. 8x dataset
|---|---|---|---|
| Pyspark_First | 19.6s, 26.8s, 22.1s | 81s, 92.5s, 89.4s | 99.4s, 97.8s, 97.4s |
| Pyspark_New | 22.7s, 22.4s, 25.8s | 88.9s, 91.7s, 89.3s | 92.6s, 97.1s, 96s |
| Python Script | 9.72s, 6.62s, 6.88s | 34.39s, 33.18s, 31.01s | 30.68s, 31.44s, 33.22s |

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## How to Run

You can use the code of this repository in multiple ways:

- Run via Notebook
- Run as script

Adjust the root_path according to your setup