import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy.sparse as scs # sparse matrix construction 
import scipy.linalg as scl # linear algebra algorithms
import scipy.optimize as sco # for minimization use
import matplotlib.pylab as plt # for visualization

import time
import cvxpy as cp

from constraint import fixed_constraints, clue_constraint


def solver(quiz):
    A0 = fixed_constraints()
    A1 = clue_constraint(quiz)

    # Formulate the matrix A and vector B (B is all ones).
    A = scs.vstack((A0,A1))
    A = A.toarray()
    B = np.ones(A.shape[0])

    try:
        x = cp.Variable(A.shape[1])
        prob = cp.Problem(cp.Minimize(cp.norm(x, 1)),
                         [A@x == B, x>=0, x<=1])
        prob.solve(verbose=False)
        x = x.value
    except:
        x = np.zeros(A.shape[1])
        
    z = np.reshape(x, (81, 9))

    ans =  np.array([np.argmax(d)+1 for d in z])
    return ''.join([str(c) for c in ans]) 