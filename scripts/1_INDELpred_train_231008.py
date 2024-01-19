"""
@author: Yilin Wei
@Date: 2023/10/08
@Project: INDELpred
@Desc: 

"""

import sys
import pickle
import time
loca = time.strftime('%Y-%m-%d')


def save_data(data, outfile):
    with open(outfile, 'wb') as outf:
        pickle.dump(data, outf)

def load_data(infile):
    with open(infile, 'rb') as inf:
        data = pickle.load(inf)
    return data

x_train,y_train=load_data('../data2023/train_2024-01-12.pkl')

from sklearn.ensemble import GradientBoostingClassifier
clf=GradientBoostingClassifier(learning_rate=0.15, min_impurity_decrease=0,
                           min_samples_leaf=0.01, min_weight_fraction_leaf=0,
                           random_state=123, subsample=1)
clf.fit(x_train,y_train)

save_data(clf,f'../data2023/INDELpred_model_{loca}.pkl')
