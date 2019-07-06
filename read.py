import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import StringIO, BytesIO
import base64

def get_graph_url(plt):
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    graph_url = base64.b64encode(img.getvalue()).decode()
    return graph_url
'''
ATTRIBUTE 3 : CHEST PAIN TYPE
'''
def draw_chest_pain_type(df):
    attributes = [1,2,3,4]
    d = generate_dictionary(df, attributes, 'chest_pain_type')
    fig = plot_dictionary(d, 'chest pain type',attributes)
    return get_graph_url(fig)
'''
ATTRIBUTE 4: Resting Blood Pressure (NOT Discrete one)
'''
def draw_resting_blood_pressure(df):
    colors = {'F': 'yellow','M' : 'green'}
    df = df[['age', 'sex', 'resting_blood_pressure']]
    df = clean_df(df)
    x = df['age']
    y = df['resting_blood_pressure']
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y,c = df.sex.map(colors))
    plt.xlabel('Age',family='Arial')
    plt.ylabel('Blood Pressure', family='Arial')
    plt.title("Resting blood pressure observation", family='Arial')
    plt.tight_layout()
    url = get_graph_url(plt)
    plt.close()
    return url
'''
ATTRIBUTE 5:Serum Cholestoral
'''
def draw_serum_cholestoral(df):
    dff = df[['age','sex','serum_cholesterol']]
    dff = clean_df(dff)
    male = dff[dff['sex']=='M']
    female = dff[dff['sex']=='F']
    plt.figure(figsize=(10, 5))
    plt.scatter(male['age'],male['serum_cholesterol'],color = 'blue',s = 10,alpha = 0.9)
    plt.scatter(female['age'],female['serum_cholesterol'],color = 'red',s = 10,alpha = 0.9)
    plt.xlabel('Age', family='Arial')
    plt.ylabel('Number of Serum Cholestoral', family='Arial')
    plt.title("Serum Cholestoral Observation", family='Arial')
    plt.tight_layout()
    url = get_graph_url(plt)
    plt.close()
    return url
'''
ATTRIBUTE 6: Fasting Blood Sugar
'''
def draw_fasting_blood_sugar(df):
    attributes = [0,1]
    d = generate_dictionary(df,attributes,'fasting_blood_sugar')
    fig = plot_dictionary(d,'Fasting Blood Sugar',attributes)
    return get_graph_url(fig)

'''
ATTRIBUTE 7: Resting Electrocardiographic results
'''
def draw_RER(df):
    attributes = [0,1,2]
    d = generate_dictionary(df, attributes, 'resting_electrocardio_results')
    fig = plot_dictionary(d, 'Resting Electrocardiographic Results',attributes)
    return get_graph_url(fig)

'''
ATTRIBUTE 8: maximum heart rate achieved
'''
def draw_Mhra(df):
    colors = {'F': 'yellow','M' : 'green'}
    df = df[['age', 'sex', 'maximum_heart_rate']]
    df = clean_df(df)
    x = df['age']
    y = df['maximum_heart_rate']
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y,c = df.sex.map(colors))
    plt.xlabel('Age', family='Arial')
    plt.ylabel('Maximum Heart Rate', family='Arial')
    plt.title("Maximum Heart Rate Achieved", family='Arial')
    plt.tight_layout()
    url = get_graph_url(plt)
    plt.close()
    return url
'''
ATTRIBUTE 9: Exercise Induced Angina
'''
def draw_exercise_induced_angina(df):
    attributes = [0,1]
    d = generate_dictionary(df,attributes,'exercise_induced_angina')
    fig = plot_dictionary(d, 'Exercise Induced Angina',attributes)
    return get_graph_url(fig)
'''
ATTRIBUTE 10: ST Depresssion
'''
def draw_ST_Depression(df):
    attributes = [1,2,3,4]
    d = generate_dictionary_ST(df, attributes, 'st_depression')
    fig = plot_dictionary(d, 'ST Depression',attributes)
    return get_graph_url(fig)
'''
ATTRIBUTE 11: Slope of peak exercise ST Segment
'''
def draw_slope_exercise_ST_segment(df):
    attributes = [1,2,3]
    d = generate_dictionary(df, attributes, 'slope_peak')
    fig = plot_dictionary(d, 'Slope of the Peak Exercise ST Segment',attributes)
    return get_graph_url(fig)
'''
ATTRIBUTE 12: Slope of peak exercise ST Segment
'''
def draw_major_vessels(df):
    attributes = [0,1,2,3]
    d = generate_dictionary(df, attributes, 'major_vessels')
    fig = plot_dictionary(d, 'Number of Major Vessels',attributes)
    return get_graph_url(fig)
'''
ATTRIBUTE 13: Slope of peak exercise ST Segment
'''
def draw_thal(df):
    attributes = [3,6,7]
    d = generate_dictionary(df, attributes, 'thalassemia')
    fig = plot_dictionary(d, 'Thal(Thalassemia)',attributes)
    return get_graph_url(fig)
'''
HELPER FUNCTIONS
'''
def index_to_char(index, num):
    if num == 1:
        a = {1: 'male_1',
             2: 'male_2',
             3: 'male_3',
             4: 'male_4'
             }
    elif num == 2:
        a = {1: 'female_1',
             2: 'female_2',
             3: 'female_3',
             4: 'female_4'
             }
    return a[index]
def generate_dictionary(df, attributes, name):
    df = df[['age', 'sex', name]]
    df = clean_df(df)
    # segregate the age groups into four segments
    d = {'male_1': [], 'female_1': [], 'male_2': [], 'female_2': [], 'male_3': [], 'female_3': [], 'male_4': [], 'female_4': []}

    for i in attributes:
        df_specific = df[df[name] == i]
        df_specific['category'] = np.digitize(df_specific.age, bins=[0, 18, 30, 60, 100])
        counts = df_specific.groupby(['category', 'sex']).age.count().unstack()
        counts.fillna(0, inplace=True)
        categories = [1,2,3,4]#four age groups
        for index, row in counts.iterrows():#index = age group. row = corresponding sex counts
            if index != 0:
                if 'M' in row:
                    d[index_to_char(index, 1)].append(row['M'])
                elif('M' not in row):
                    d[index_to_char(i, 1)].append(0)
                if 'F' in row:
                    d[index_to_char(index, 2)].append(row['F'])
                elif('F' not in row):
                    d[index_to_char(i, 2)].append(0)
                categories.remove(index)
        for i in categories:
            d[index_to_char(i, 1)].append(0)
            d[index_to_char(i, 2)].append(0)
    return d
def generate_dictionary_ST(df, attributes, name):
    df = df[['age', 'sex', name]]
    df['st_group'] = np.digitize(df[name], bins=[0, 2, 4, 6, 8])
    df = clean_df(df)
    # segregate the age groups into four segments
    d = {'male_1': [], 'female_1': [], 'male_2': [], 'female_2': [], 'male_3': [], 'female_3': [], 'male_4': [], 'female_4': []}

    for i in attributes:
        df_specific = df[df['st_group'] == i]
        df_specific['category'] = np.digitize(df_specific.age, bins=[0, 18, 30, 60, 100])
        counts = df_specific.groupby(['category', 'sex']).age.count().unstack()
        counts.fillna(0, inplace=True)
        categories = [1,2,3,4]
        for index, row in counts.iterrows():
            if index != 0:
                if 'M' in row:
                    d[index_to_char(index, 1)].append(row['M'])
                elif('M' not in row):
                    d[index_to_char(i, 1)].append(0)
                if 'F' in row:
                    d[index_to_char(index, 2)].append(row['F'])
                elif('F' not in row):
                    d[index_to_char(i, 2)].append(0)
                categories.remove(index)
        for i in categories:
            d[index_to_char(i, 1)].append(0)
            d[index_to_char(i, 2)].append(0)
    return d
def plot_dictionary(d, name,attributes):
    # Plot the image
    plt.style.use('ggplot')
    dff = pd.DataFrame(data=d)
    fig, ax = plt.subplots(figsize=(10,5))
    dff[['male_1', 'female_1']].plot.bar(stacked=True, width=0.2, position=-0.5, edgecolor = 'white', colormap="bwr", ax=ax, alpha=0.7)
    dff[['male_2', 'female_2']].plot.bar(stacked=True, width=0.2, position=-1.5, edgecolor = 'white', colormap="bwr", ax=ax, alpha=0.7)
    dff[['male_3', 'female_3']].plot.bar(stacked=True, width=0.2, position=-2.5, edgecolor = 'white', colormap="bwr", ax=ax, alpha=0.7)
    dff[['male_4', 'female_4']].plot.bar(stacked=True, width=0.2, position=-3.5, edgecolor = 'white', colormap="bwr", ax=ax, alpha=0.7)
    ax.set_xlabel(name, family='Arial')
    ax.set_ylabel('Frequency', family='Arial')
    arr = ['0-18','18-30','30-60','60-100','']
    plt.xticks(np.arange(0,4,0.2),['']+arr*len(attributes),rotation=60)
    for i, j in enumerate(np.arange(ax.get_xlim()[0] + ((ax.get_xlim()[1] - ax.get_xlim()[0]) / len(attributes)) / 2, \
        ax.get_xlim()[1], (ax.get_xlim()[1] - ax.get_xlim()[0]) / len(attributes))):
        plt.text(j,ax.get_ylim()[1]- 2,f'Type {i + 1}', fontsize=12, family='serif', color= 'black', alpha=0.8)
    ax.legend(['Male', 'Female'],loc='upper left', fontsize=8)
    plt.tight_layout()
    plt.close()
    return fig

def read_data():
    df = pd.read_csv('processed.cleveland.data', header=None)
    df.columns = ['age','sex','chest_pain_type','resting_blood_pressure','serum_cholesterol','fasting_blood_sugar','resting_electrocardio_results'\
                    ,'maximum_heart_rate','exercise_induced_angina','st_depression','slope_peak','major_vessels','thalassemia','target']
    df.loc[df.target != 0, 'target'] = 1
    return df

def clean_df(df, stringify_gender = True):
    # Remove any non-numeric cells
    df = df[~(df == '?').any(axis = 1)].drop_duplicates().copy()
    #convert string type data to float
    for i in df.columns:
        if df[i].dtypes != float and df[i].dtypes != int:
            df[i] = pd.to_numeric(df[i],errors='coerce')
    if stringify_gender:
        df['sex'].replace([0.0, 1.0], ['F', 'M'], inplace=True)
    return df

def get_graph_url(plt):
    img = BytesIO()
    plt.savefig(img, format='png', dpi=150)
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(graph_url)

