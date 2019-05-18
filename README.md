## Abstract
We implemented linear programming and weighted LP1, solving the weighted l1-minimization problem(WP1) by (LP1) in our code to solve the Sudoku problem. 

## Sudoku_solver
This serves as a sample sudoku solver repository for Optimization II
In the Sudoku_solver, one implements solver function. In the test.py, it is demonstrated how to call it.
Necessary parts include ``sudoku_solver.py``, ``LICENSE``, ``writeup.pdf``, ``README.md``.

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
| Dataset  |  Success Rate |
| ---    |---     |
|Small1|**24/24 = 1.00**|
|Small2|**744/1000 = 0.744**|
|Large1|**957/1000 = 0.957**|
|Large2|**1000/1000 = 1.00**|

## Inspirations
 * [A Warm Restart Strategy for Solving Sudoku by Sparse Optimization Methods](https://arxiv.org/pdf/1507.05995.pdf)
 * [](https://arxiv.org/pdf/1507.05995.pdf)
