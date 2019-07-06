import pandas as pd
import numpy as np
import read as rd
import feature_selection as fs
import statistics as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

results={}

def load_data(subset):
    df1_clean = rd.read_data()
    df1_clean = rd.clean_df(df1_clean,False)
    labels = df1_clean.loc[:,['target']].values
    df1_clean = df1_clean.loc[:,subset].astype(float).astype(int)
    data = df1_clean.loc[:,subset].astype(float).astype(int)
    query = ''
    for s in range(len(subset)-1):
        query = query + "data['" + subset[s] + "'].values,"
    query = query + "data['" + subset[-1] + "'].values"
    data = np.stack((eval(query)), axis=-1)
    return data,labels,df1_clean

def log_reg(data, labels, inputs=False):
    logmodel = LogisticRegression(multi_class='multinomial',solver='lbfgs',C=1,max_iter=8888888888888)
    if(inputs):
        logmodel.fit(data,labels.ravel())
        inputs = list(map(int, inputs))
        pred = logmodel.predict([inputs])
        return pred
    scores = cross_val_score(logmodel, data, labels.ravel(), cv=10, scoring='accuracy')
    return scores

def accuracy_selection(rankings):
    global results
    for i in range(2,len(rankings)):
        data,labels,df = load_data(rankings[:i])
        results[i] = st.mean(log_reg(data, labels))
    results_values = [results[i] for i in results]
    results_keys = [k for k in results]
    df_result = pd.DataFrame({'accuracy':results_values},index=results_keys)
    plt.style.use('ggplot')
    plt.figure()
    df_result.plot()
    plt.tight_layout()
    url = rd.get_graph_url(plt)
    return url

def predict(rankings,inputs):
    index = len(results)
    input_use=[]
    sorted_list = [(k, results[k]) for k in sorted(results, key=results.get, reverse=True)]   
    index = sorted_list[0][0]
    for j in rankings[0:index]:
        input_use.append(inputs[j])
    data,labels,df = load_data(rankings[:index])
    predictition = log_reg(data, labels,input_use)
    return predictition







