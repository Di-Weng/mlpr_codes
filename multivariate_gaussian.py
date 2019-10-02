# -*- coding: utf-8 -*-
"""
-------------------------------
   Time    : 2019/10/02 2:13 AM
   Author  : diw
   Email   : di.W@hotmail.com
   File    : multivariate_gaussian.py
   Desc:
-------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
N = int(1e4);
D = 2
X = np.random.randn(N,2)

#original
plt.title('original X')
plt.plot(X[:, 0], X[:, 1], '.')
plt.axis('square')
plt.show()

# print(X)
a_list = np.linspace(0,1,10)
temp_count = 0

fig_1 = plt.figure(figsize=[9,9])
fig_1.suptitle('Transforming X')
for a in a_list:
    A = np.asarray([[1,0],[a,1-a]])
    X_trans= np.asarray([list(A.dot(current_X)) for  current_X in X])
    ax = plt.subplot(3,4,1+temp_count)
    plt.plot(X_trans[:, 0], X_trans[:, 1], '.')

    ax.set_title('a: %.2f'%a)
    plt.axis('square')
    temp_count+=1

plt.show()