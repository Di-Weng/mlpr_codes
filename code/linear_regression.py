# -*- coding: utf-8 -*-
"""
-------------------------------
   Time    : 2019/9/29 12:34 PM
   Author  : diw
   Email   : di.W@hotmail.com
   File    : linear_regression.py
   Desc:    Linear regression with basis function !
-------------------------------
"""
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

N = 100
D = 8
model = Pipeline([('poly', PolynomialFeatures(degree=D,interaction_only=True)),
                  ('linear', LinearRegression(fit_intercept=True))])
# fit to an order-3 polynomial data
X = np.random.rand(N,D)
Y = np.random.random(N)
model = model.fit(X, Y)
print(model.named_steps['linear'].coef_)
print(len(model.named_steps['linear'].coef_))
print(float(1/(len(model.named_steps['linear'].coef_)-1)))
