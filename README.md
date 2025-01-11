# HTW Longest Word Search

## Intention

The purpose of this repository is to find the longest word in a given text efficiently. This project aims to compare different algorithms and their performance in terms of time complexity.

## Analysis of Findings

After running multiple tests with various approaches, we observed the following results:

| Used technology | Average Time normal data set | Average Time dublicated data set (3 times)
|---|---|
| Pyspark_Basic | 20.3 s | 1m 21.4 s
| Pyspark_New | 28 s | 1m 35.7 s
| Python Script | 9.72 s | 40.5 s

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