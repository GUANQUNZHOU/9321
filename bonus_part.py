import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import read as rd
from read import get_graph_url
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def bonus_cluserting():
    df1_clean = rd.read_data()
    features = list(df1_clean.columns.values)
    df1_clean = rd.clean_df(df1_clean,False)
    labels = df1_clean.loc[:,['target']].values
    features = features[2:-1]
    data = df1_clean.loc[:,features].astype(float).astype(int)
    #DO KMeans to obtain new labels
    points = data.values
    kmeans = KMeans(n_clusters=2)
    km =kmeans.fit(points)
    labels = pd.DataFrame(km.labels_)
    labels.columns = ['labels']
    #as we have 11/13 features, drawing a 11-D graph is impossible
    #so I used PCA to reduce dimentionality to 2 and draw the graph
    points_std = StandardScaler().fit_transform(points)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(points_std)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, labels], axis = 1)
    fig, ax = plt.subplots()
    colors = {1: 'red',0 : 'blue'}
    finalDf.plot.scatter(x = 'principal component 1',y = 'principal component 2',c = finalDf.labels.map(colors))
    red_patch = mpatches.Patch(color='red', label='Class One')
    blue_patch = mpatches.Patch(color='blue', label='Class Two')
    plt.legend(handles=[red_patch,blue_patch])


    return get_graph_url(plt)




