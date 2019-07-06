import pandas as pd
import numpy as np
import read as rd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib

def return_clean_df():
    df1_clean = rd.read_data()
    df1_clean = rd.clean_df(df1_clean,False)
    return df1_clean

def do_univariate():
    df1_clean = return_clean_df()
    return univariate(df1_clean)

def univariate(df1_clean):
    test = SelectKBest(score_func=chi2, k=4)
    df1_clean
    X = df1_clean.iloc[:,2:13]
    Y = df1_clean.loc[:,'target']
    fit = test.fit(X, Y)
    np.set_printoptions(precision=3)
    header = list(X)
    d = {}
    for i in range(len(fit.scores_)):
        d[fit.scores_[i]] = header[i]
    sort_result = sorted(d.items(), key=lambda d: d[0],reverse=True)
    df3 = pd.DataFrame(sort_result)
    df3.plot.bar(rot=0)

    d_sort = dict(sorted(d.items(), reverse = True))
    first_key = list(d_sort.keys())[0]
    return d_sort


