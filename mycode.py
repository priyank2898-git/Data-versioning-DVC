import pandas as pd 
import os

#create a dictionary for data fra,e
data={ 'Name':['Akash','Neeraj','Preetam'],
        'Age':[20,30,40],
        'City':['Faridabad','Noida','New delhi']
}

#craete a Dataframe
df=pd.DataFrame(data)

#new row
new_data1={"Name":"kirti","Age":30,"City":"Ayodhya"}
df.loc[len(df.index)] = new_data1

#new row
#new_data2={"Name":"preeti","Age":24,"City":"Lucknow"}
#df.loc[len(df.index)] = new_data2

#storing data
data_dir='data'
os.makedirs('data',exist_ok=True)

file_path=os.path.join(data_dir,'Sample_data.csv')

#saving the file
df.to_csv(file_path,index=False)

print(f'The file has been saved to {file_path}')