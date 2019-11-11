import pandas as pd
from pandas import DataFrame
'''
accident_file = pd.read_csv('accidents_2017.csv')
n = accident_file.columns
for i in n:
    m = i.split()
    if len(m)>1:
        print('"'+i+'"',end = ' ')
    else:
        print(i,end =' ')
print('')
#print(n)
r = accident_file.values
#print(r[:9])
store = []
reference  = ['la','de',"l'","d'"]
for k in range(10):
    for p in r[k]:
        if isinstance(p,int):
            print(p,end = ' ')
            continue
        elif isinstance(p,float):
            print(p,end = ' ')
            continue
        else:
            p = str(p)
            p = p.strip(' ')
            m = p.split()
            #print(m)
            if len(m) == 1:
                if p.isalpha():
                    p = p.capitalize()
                print(p,end = ' ')
                
            elif len(m)>1:
                for count in range(len(m)):
                    if m[count] in reference:
                        continue
                    elif m[count][:2] in reference and m[count][2].isupper():
                        continue
                    elif m[count][0].isalpha():
                        m[count] = m[count].capitalize()
                p = ''
                for ever in range(len(m)-1):
                    p = p+m[ever]
                    p = p+' '
                p = p+m[-1]
                print('"'+p+'"',end = ' ')
    print('')
                   
#################################
            if len(m)>1 and len(m)<4:
                #print('22',m)
                if m[0].isalpha():
                    #print('ss')
                    m[0] = string.capwords(m[0])
                    p =''
                    for h in range(len(m)-1):
                        p = p+m[h]
                        p = p+' '
                    p = p+m[-1]
                print('"'+p+'"',end = ' ')
            elif len(m) >4:
                if m[0].isalpha():
                #print('ss')
                    m[0] = string.capwords(m[0])
                    m[4] = string.capwords(m[4])
                    p =''
                    for h in range(len(m)-1):
                        p = p+m[h]
                        p = p+' '
                    p = p+m[-1]
                print('"'+p+'"',end = ' ')
                    
            elif len(m) == 1:
                if p.isalpha():
                    string.capwords(p)
                print(p,end=' ')
            elif len(m) == 4:
                print('"'+p+'"',end = ' ')


    #print(r[i])
#print(r[1])

#print(accident_file[:9])
#out = accident_file.iloc[1:9]
#print(out)

'''
#q2
accident_file = pd.read_csv('accidents_2017.csv')
accident_file_q2 = accident_file.astype(str)
#print(accident_file_q2)
y = accident_file_q2[accident_file_q2['District Name'].str.contains('Unknown')]
#print(y['District Name'])
test1 = list(y['District Name'])
#print(test1)
test2 = list(accident_file_q2['District Name'])
ret = []
for i in test2:
    if i not in test1:
        ret.append(i)
        
#print(ret)
result = accident_file[accident_file['District Name'].isin(ret)]
result_q2 = result.values
#print(result_q2)
result_columns = result.columns
#print(result_columns[0])
to_replace = {}
for uo in result_columns:
    to_replace[uo] = []
reference  = ['la','de',"l'","d'"]
for k_q2 in range(len(result_q2)):
    ur = result_q2[k_q2]#meiyihang
    for p_q2 in range(len(ur)):#p_q2shishu
        if isinstance(ur[p_q2],int):
            to_replace[result_columns[p_q2]].append(ur[p_q2])
            continue
        elif isinstance(p_q2,float):
            to_replace[result_columns[p_q2]].append(ur[p_q2])
            continue
        else:
            #print(isinstance(p_q2,str))
            ur[p_q2] = str(ur[p_q2])
            ur[p_q2] = ur[p_q2].strip(' ')
            m_q2 = ur[p_q2].split()
            if len(m_q2) == 1:
                if ur[p_q2].isalpha():
                    ur[p_q2] = ur[p_q2].capitalize()
                to_replace[result_columns[p_q2]].append(ur[p_q2])
            elif len(m_q2)>1:
                for count_q2 in range(len(m_q2)):
                    if m_q2[count_q2] in reference:
                        continue
                    elif m_q2[count_q2][:2] in reference and m_q2[count_q2][2].isupper():
                        continue
                    elif m_q2[count_q2][0].isalpha():
                        m_q2[count_q2] = m_q2[count_q2].capitalize()
                p_q2later = ''
                for ever_q2 in range(len(m_q2)-1):
                    p_q2later = p_q2later+m_q2[ever_q2]
                    p_q2later = p_q2later+' '
                p_q2later = p_q2later+m_q2[-1]
                to_replace[result_columns[p_q2]].append(p_q2later)

#print(to_replace)
dfr = DataFrame(to_replace)
dfr.to_csv('result_q2.csv',index = False)
#result.to_csv('resul_q2.csv',index = False)

'''
#q3
accident_file = pd.read_csv('accidents_2017.csv')
accident_file = accident_file.drop_duplicates()
#print(n)
r = accident_file.values
store = []
statistics = {}
store_name = []
#print(len(r))
for i in range(len(r)):
    if r[i][1] == 'Unknown':
        store.append(i)
#print(len(set(store)))
#print('ss')
for k in range(len(r)):
    if k in store:
        continue
    elif r[k][1] in store_name:
        statistics[r[k][1]] += 1
    else:
        store_name.append(r[k][1])
        statistics[r[k][1]] = 1
#print(statistics)
output_q3 = sorted(statistics.items(),key = lambda item:item[1],reverse = True)
print('"'+'District Name'+'"',end = ' ')
print('"'+'Total numbers of accidents'+'"')
#print(output_q3)
for i in output_q3:
    m = i[0].split()
    if len(m)>1:
        print('"'+i[0]+'"',end = ' ')
        print(i[1])
    else:
        print(i[0],end = ' ')
        print(i[1])

'''
'''
#q4
import json
air_file = pd.read_csv('air_stations_Nov2017.csv')
air_file_filter = air_file.ix[:9,['Station','District Name']]
sf = air_file_filter.values
#print(sf)
output_air_file = []
for i in range(len(sf)):
    a = sf[i][0]
    af = a.split()
    if len(af)>3:
        for g in range(3,len(af)):
            if af[g].isalpha():
                af[g] = af[g].capitalize()           
        #print(af)
        a = ' '.join(af)
    dic = {}
    dic['Station'] = a
    dic['District Name'] = sf[i][1]
    output_air_file.append(dic)
json_air_file = json.dumps(output_air_file)
print(json_air_file)

air_quality = pd.read_csv('air_quality_Nov2017.csv')
air_quality_file = air_quality.astype(str)
yy = air_quality_file[air_quality_file['Air Quality'].str.contains('Good')]
test_1 = list(yy['Air Quality'])
test_2 = list(air_quality_file['Air Quality'])
target = []
for w in test_2:
    if w not in test_1:
        target.append(w)
target_result = air_quality[air_quality['Air Quality'].isin(target)]
target_result_file = target_result.astype(str)
yyy = target_result_file[target_result_file['Air Quality'].str.contains('--')]
ttest1 = list(yyy['Air Quality'])
ttest2 = list(target_result_file['Air Quality'])
ttarget = []
for h in ttest2:
    if h not in ttest1:
       ttarget.append(h)
ttarget_result = target_result[target_result['Air Quality'].isin(ttarget)]
#ttarget_result.to_csv('rest_q4.csv',index = False)#kan
#print(ttarget_result)
sf_air_quality_column = ttarget_result.columns
#print(sf_air_quality_column)
for t in range(len(sf_air_quality_column)):
    a = sf_air_quality_column[t]
    m = a.split()
    if len(m)>1:
        print('"'+a+'"',end = ' ')
    else:
        print(a,end = ' ')
print('')
sf_air_quality = ttarget_result.values
for u in range(10):
    b = sf_air_quality[u]
    for i in range(len(b)):
        v = b[i]
        if isinstance(v,float):
            print(v,end = ' ')
        elif isinstance(v,int):
            print(v,end = ' ')
        elif '-' in v:
            print('"'+v+'"',end = ' ')
        elif ' ' in v:
            print('"'+v+'"',end = ' ')
        else:
            print(v,end = ' ')
    print('')

rt = ttarget_result.values
store_for_frame = []
for i in range(len(rt)):
    sf_frame = []
    qw = rt[i]
    sf_frame.append(qw[2])
    sf_frame.append(qw[3])
    store_for_frame.append(sf_frame)
#print(store_for_frame)
df1= pd.DataFrame(store_for_frame,columns=['Longitude','Latitude'])
#print(df1)
#df.to_csv('hhhhh.csv',index = False)#kan
df2 = pd.read_csv('air_stations_Nov2017.csv')
df = pd.merge(df2,df1,how='inner',on=['Longitude','Latitude'])
df.sort_index(inplace=True)
#df.to_csv('second.csv',index=False)
#print(df)
rt_second = df.values
location = {}
location_store = []
for j in range(len(rt_second)):
    qw_second = rt_second[j]
    if qw_second[1] not in location_store:
        location_store.append(qw_second[1])
        location[qw_second[1]] = qw_second[4]
    else:
        continue
#print(location)
month_con = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
store_for_district = []
for n in range(len(rt)):
    sf_district = []
    qw_dist = rt[n]
    #print(qw_dist)
    sf_district.append(location[qw_dist[2]])
    c = qw_dist[13].split()
    slid_date = c[0].split('/')
    #print(slid_date)
    sf_district.append(month_con[slid_date[1]])
    sf_district.append(int(slid_date[0]))
    slid_hour = c[1].split(':')
    sf_district.append(int(slid_hour[0]))
    store_for_district.append(sf_district)
#print(store_for_district)
dff1 = pd.DataFrame(store_for_district,columns=['District Name','Month','Day','Hour'])
#print(dff1)
#dff1.to_csv('dff.csv',index=False)
dff2 = pd.read_csv('result_q2.csv')
dff = pd.merge(dff2,dff1,how='inner',on=['District Name','Month','Day','Hour'])
dff.sort_index(inplace=True)
#print(dff)
#dff.to_csv('result_q4.csv',index=False)
column_q4 = dff.columns
row_q4 = dff.values
replace_q4 = {}
for up in column_q4:
    replace_q4[up] = []
#print(replace_q4)
reference  = ['la','de',"l'","d'"]
for k_q4 in range(len(row_q4)):
    uw = row_q4[k_q4]#meiyihang
    for p_q4 in range(len(uw)):
        if isinstance(uw[p_q4],int):
            replace_q4[column_q4[p_q4]].append(uw[p_q4])
            continue
        elif isinstance(uw[p_q4],float):
            replace_q4[column_q4[p_q4]].append(uw[p_q4])
            continue
        else:
            uw[p_q4] = str(uw[p_q4])
            uw[p_q4] = uw[p_q4].strip(' ')
            m_q4 = uw[p_q4].split()
            if len(m_q4) == 1:
                if uw[p_q4].isalpha():
                    uw[p_q4] = uw[p_q4].capitalize()
                replace_q4[column_q4[p_q4]].append(uw[p_q4])
            elif len(m_q4)>1:
                for count_q4 in range(len(m_q4)):
                    if m_q4[count_q4] in reference:
                        continue
                    elif m_q4[count_q4][:2] in reference and m_q4[count_q4][2].isupper():
                        continue
                    elif m_q4[count_q4].isalpha():
                        m_q4[count_q4] = m_q4[count_q4].capitalize()
                p_q4later = ''
                for ever_q4 in range(len(m_q4)-1):
                    p_q4later = p_q4later+m_q4[ever_q4]
                    p_q4later = p_q4later+' '
                p_q4later = p_q4later+m_q4[-1]
                replace_q4[column_q4[p_q4]].append(p_q4later)
#print(replace_q4)
drr_q4 = DataFrame(replace_q4)
drr_q4.to_csv('result_q4.csv',index=False)
'''                        
#q5
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import matplotlib.image as mpimg

location = pd.read_csv('result_q2.csv',float_precision = 'high')

location_long = location['Longitude']
location_longitude = location_long.values
#print(location_longitude)
longitude_draw = []
latitude_draw = []
for long in location_longitude:
    if long not in longitude_draw:
        longitude_draw.append(long)
location_lat = location['Latitude']
location_latitude = location_lat.values
for lat in location_latitude:
    if lat not in latitude_draw:
        latitude_draw.append(lat)
        latitude_draw = sorted(latitude_draw)
#print(longitude_draw)
#print(latitude_draw)
longitude_draw = sorted(longitude_draw)
latitude_draw = sorted(latitude_draw)
#print(longitude_draw)
#print(latitude_draw)
#print(location_longitude)

fig  = mpimg.imread('Map.png')
location_draw_long = location['Longitude']
location_draw_lat = location['Latitude']
plt.scatter(location_draw_long,location_draw_lat)
plt.xlim(longitude_draw[0],longitude_draw[-1])
plt.ylim(latitude_draw[0],latitude_draw[-1])
plt.title('Plot')
#location_plot = location_draw.plot(x = 'Longitude',y = 'Latitude',kind = 'scatter')
#location_plot.axis('off')
plt.imshow(fig)
plt.show()






