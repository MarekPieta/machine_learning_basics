# -*- coding: utf-8 -*-
"""

    TOPIC: Feature Selection

"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load the iris dataset.
dataset = datasets.load_iris()

# Create a base classifier used to evaluate a subset of attributes.
model = LogisticRegression()

X_all = dataset.data
y = dataset.target

#%% See the prediction accuracy on the complete iris dataset.

fmodel = model.fit(X_all, y)

acc_all = fmodel.score(X_all, y)
print('All features accuracy = {:.3f}\n'.format(acc_all))

#%% Use Recursive Feature Elimination (RFE) to select N most relevant attributes.

n_features = 2
rfe = RFE(model, n_features)
rfe.fit(X_all, y)

# Summarize the selection of the attributes.
print('Feature ranking (using RFE):')
feature_rank = pd.DataFrame(
        np.column_stack([dataset.feature_names, rfe.ranking_, rfe.support_]),
        columns=['feature_name', 'ranking', 'support'])
print(feature_rank)
print()

#%% See the prediction accuracy on a subset of features from the iris dataset.

# Select only relevant features.
X_filt = X_all[:, rfe.support_]
model2 = LogisticRegression()
fmodel2 = model2.fit(X_filt, y)

acc_all2 = fmodel2.score(X_filt, y)
print('Selected features accuracy = {:.3f}\n'.format(acc_all2))