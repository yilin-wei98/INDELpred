"""
@author: Yilin Wei
@Date: 2023/10/08
@Project: INDELpred
@Desc: 适用于最终脚本的训练模型

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

# x_train,y_train=load_data('../data2023/train_AF0_230928.pkl')
x_train,y_train=load_data('../data2023/train_2024-01-12.pkl')


# x_train = x_train.drop(['exac_syn_z', 'exac_mis_z',
#        'exac_lof_z', 'exac_pLI', 'exac_cnv_z',
#        'RVIS_pop_maf_0_05', 'p_RVIS_pop_maf_0_05',
#         'OE-ratio_ExAC_v2', 'p_OE-ratio_ExAC_v2', 'alternative-RVIS_maf_0_0025',
#        'alternative-p_RVIS_maf_0_0025'], axis=1)


# x_train.rename(columns={'gnomad_genome_controls_AF_popmax': 'AF'}, inplace=True)
# x_train = x_train.drop(['Func','ExonicFunc'], axis=1)

# 2023.11.1
# x_train = x_train.drop(['stopless','ncRNA','intergenic','stream'], axis=1)

from sklearn.ensemble import GradientBoostingClassifier
clf=GradientBoostingClassifier(learning_rate=0.15, min_impurity_decrease=0,
                           min_samples_leaf=0.01, min_weight_fraction_leaf=0,
                           random_state=123, subsample=1)
clf.fit(x_train,y_train)

save_data(clf,f'../data2023/INDELpred_model_{loca}.pkl')