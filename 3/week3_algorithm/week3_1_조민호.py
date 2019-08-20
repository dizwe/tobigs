#%%
import pandas as pd
df = pd.read_csv('./example1.csv')

#%%
# IQ 결측치 있는 행의 비율 R
R = (len(df['IQ'])-df['IQ'].str.isnumeric().sum())/len(df['IQ'])*100
# df['IQ'].str.isnumeric()

#%%
# 결측치 채워넣기(성별에 대한 IQ 평균 일의 자리에서 내림)
# 괄호를 해줘야 한다. 그리고 이상하게 Object 타입을 리턴해서 to numeric 해줘야 한다
# oeject 인 상태에서 그대로 mean 해주면 주소값의 평균이 나온다
# df.loc[df['Gender']=='M' & df['IQ'].str.isnumeric()]
man_mean = pd.to_numeric(df.loc[(df['Gender']=='M') & (df['IQ'].str.isnumeric()),'IQ']).mean()
woman_mean = pd.to_numeric(df.loc[(df['Gender']=='F') & (df['IQ'].str.isnumeric()),'IQ']).mean()
# int로 내림하기
df.loc[(df['IQ'].str.isnumeric()!=True)&(df['Gender']=='M'),'IQ'] = int(man_mean)
df.loc[(df['IQ'].str.isnumeric()!=True)&(df['Gender']=='F'),'IQ'] = int(woman_mean)

#%%
# 예측값을 만든다.
# 남자의 IQ 는 키(cm) – 70 로 수렴하고, 여자의 IQ 는 키(cm) – 60 으로 수렴한다.
df.loc[df['Gender']=='M','expect'] = df.loc[df['Gender']=='M','Height']-70
df.loc[df['Gender']=='F','expect'] = df.loc[df['Gender']=='F','Height']-60
# df['remain']-/len(df)

# 평균 오차 구하기
# 다 수로 안되어있어서 to_nemeric 해줘야 함
df['remain'] = abs(df['expect'] - pd.to_numeric(df['IQ']))
E = df['remain'].sum()/len(df)

#%%
male_filtered = df.loc[(df['Gender']=='M')&(df['Height']>=168)&(df['Height']<=172),:]
female_filtered = df.loc[(df['Gender']=='F')&(df['Height']>=158)&(df['Height']<=162),:]
H = (len(male_filtered)+len(female_filtered))/len(df)*100

#%% 
#결과 출력
print(int(R), int(E), int(H))
if R<=25 and E<=5 and H<=50:
    print('GodDaeWoong')
else:
    print('GodHyeIn')
#%%


#%%
