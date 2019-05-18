## Introduction

## (SSS) Sample Sudoku Solver
This serves as a sample sudoku solver repository for Optimization II.

Necessary parts include ``sudoku_solver.py``, ``LICENSE``, ``writeup.pdf``, ``README.md``.

## Sudoku_solver
In the Sudoku_solver, one implements solver function. In the test.py, it is demonstrated how to call it.

## Datasets
`small1.csv`
`samll2.csv`
`large1.csv`
`large2.csv`

## Requirements
First run
```
pip install -r requirements.txt
```

if your working environment is jupyter-notebook, then run
```
!pip install -r requirements.txt
```

## Run the test
Suppose the data are stored in the same directory, then you can call

```
python test.py small2.csv
```

otherwise simply call

```
python test.py directory_to_data
```

## Results


## Inspirations
 * [A Warm Restart Strategy for Solving Sudoku by Sparse Optimization Methods](https://arxiv.org/pdf/1507.05995.pdf)
