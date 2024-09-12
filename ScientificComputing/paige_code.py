'''
Hi, Paige,

Here's an example of how you can
go through an nxn matrix column by column
below the main diagonal and compute the 
gauss multipliers for each entry. Note
the order of the matrix entries as they
are printed out.

Kind regards,
Vladimir Kulyukin

Gaussian multiplier at 1, 0 is 0.8356164383561644
Gaussian multiplier at 2, 0 is 1.8767123287671232
Gaussian multiplier at 3, 0 is 2.684931506849315
Gaussian multiplier at 2, 1 is 0.2606060606060606
Gaussian multiplier at 3, 1 is 0.24242424242424243
Gaussian multiplier at 3, 2 is 0.7868852459016393
'''

import numpy as np

A = np.array([[ 73., 136., 173., 112.],
              [ 61., 165., 146.,  14.],
              [137.,  43., 183.,  73.],
              [196.,  40., 144.,  31.]])

## Go through A and compute the Gaussian multipliers.
n = A.shape[0]
for c in range(n):
    for r in range(c+1, n):
        if A[r][c] == 0:
           continue
        else:
           ## This is the Gaussian multiplier
           m = A[r][c]/A[c][c]
           print('Gaussian multiplier at {}, {} is {}'.format(r,c, m))
