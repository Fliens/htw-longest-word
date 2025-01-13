# HTW Longest Word Search

## Intention

The purpose of this repository is to find the longest word in a given text efficiently. This project aims to compare different algorithms and their performance in terms of time complexity.

## Analysis of Findings

After running multiple tests with various approaches, we observed the following results:

| Used technology | Taken Time 1x dataset | T. 4x dataset (500 MB) | T. 8x dataset (1 GB) |
|---|---|---|---|
| Pyspark_First | 19.6s, 26.8s, 22.1s<br>AVG: 22.83s | 81s, 92.5s, 89.4s<br>AVG: 87.63s | 201.7s, 179.1s, 157.4s<br>AVG: 179.4s |
| Pyspark_New | 22.7s, 22.4s, 25.8s<br>AVG: 23.63s | 88.9s, 91.7s, 89.3s<br>AVG: 89.97s | 160.5s, 157.4s, 150.1s<br>AVG: 156s |
| Python Script | 9.72s, 6.62s, 6.88s<br>AVG: 7.74s | 34.39s, 33.18s, 31.01s<br>AVG: 32.86s | 76.92s, 60.24s, 59.89s<br>AVG: 65.68s |

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