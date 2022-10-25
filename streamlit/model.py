import warnings
warnings.filterwarnings('ignore')
import numpy as np
from nzpyida.ae import NZFunGroupedApply
import sklearn as sk
from connection import *







if idadb.exists_table("properties"):
        idadb.drop_table("properties")



code_house_prediction_model = """def house_prediction_model(self,df):
                import numpy as np
                import pandas as pd
                
                import sklearn
        
                
                from sklearn.model_selection import cross_val_score
                from sklearn.model_selection import train_test_split
                from sklearn.linear_model import LinearRegression
                from sklearn.ensemble import GradientBoostingRegressor
                # from xgboost import XGBRegressor
                from sklearn.preprocessing import LabelEncoder
                from sklearn.metrics import r2_score,mean_squared_error
                
            
                
                data = df.copy()
                                
                data = data.drop(axis =1 , columns = ['URL','REGION_URL','IMAGE_URL'])
                
                
                #Replacing the null values in numerical columns
                null_columns = ['LAT','LONG']
                for i in null_columns:
                    col_mean = np.mean(data[i])
                    data[i] = data[i].fillna(col_mean)
                    
                #Replacing the null values in categorical columns
                
                data['LAUNDRY_OPTIONS'].value_counts()
                data.loc[data['LAUNDRY_OPTIONS']=='','LAUNDRY_OPTIONS'] = 'w/d in unit'
                
                data['PARKING_OPTIONS'].value_counts()
                data.loc[data['PARKING_OPTIONS']=='','PARKING_OPTIONS'] = 'off-street parking'
                
                
                # #Outliers handling
                
                columns_with_outliers = ['PRICE','SQFEET','BEDS','BATHS']
                for i in columns_with_outliers:
                    column = data[i]
                    first = column.quantile(0.05)
                    third = column.quantile(0.90)
                    iqr = third - first
                    upper_limit = third + 1.5 * iqr
                    lower_limit = first - 1.5 * iqr
                    column.mask(column > upper_limit, upper_limit, inplace=True)
                    column.mask(column < lower_limit, lower_limit, inplace=True)
                
              
               
        
                encoder={}
                categorical_columns_list = []
                for i in data.columns:
                    if data[i].dtype == 'object':
                        categorical_columns_list.append(i)
                        encoder[i] = LabelEncoder()
                        encoder[i].fit(list(data[i].values))
                        data[i] = encoder[i].transform(list(data[i].values))

                

                
                #Splitting into training and testing dataset
                
                y = data['PRICE']
                X = data.drop(columns=['PRICE'],axis=1)
                
                X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20 , train_size = 0.80, random_state=100)
                
        


                
                #Gradient Boosting Regression
                from sklearn.ensemble import GradientBoostingRegressor
                
                gbr = GradientBoostingRegressor()
                gbr.fit(X_train, y_train)


                y_pred_gbr= gbr.predict(X_test)
                print(y_pred_gbr)

                r2_score = gbr.score(X_test,y_test)
                print(r2_score)

                
                
                from sklearn.model_selection import cross_val_score
                cv_scores = np.sqrt(-cross_val_score(gbr, X, y,scoring='neg_mean_squared_error',cv=2))
                final_score = (np.mean(cv_scores/y.max()))

                
                predictions = X_test.copy()
                
                for column in categorical_columns_list:   
                    predictions[column] = encoder[column].inverse_transform(list(predictions[column].values))

                

                predictions['PRICE_PREDICTED'] = y_pred_gbr
                predictions['ACCURACY'] = r2_score


                def print_output(x):
                    row = [x['ID'],x['REGION'],
                   x['TYPE'],
                    x['SQFEET'],x['BEDS'],
                    x['BATHS'],x['CATS_ALLOWED'],x['DOGS_ALLOWED'],x['SMOKING_ALLOWED'],
                    x['WHEELCHAIR_ACCESS'],x['ELECTRIC_VEHICLE_CHARGE'],
                    x['COMES_FURNISHED'],x['LAUNDRY_OPTIONS'],x['PARKING_OPTIONS'],x['LAT'],x['LONG'],x['PRICE_PREDICTED'],x['ACCURACY']]
                    self.output(row)
                predictions.apply(print_output, axis=1)
                
            
                
                    
"""



output_signature = {'ID':'int64','REGION':'str','TYPE':'str',
    'SQFEET':'double','BEDS':'float','BATHS':'float','CATS_ALLOWED':'int','DOGS_ALLOWED':'int',
'SMOKING_ALLOWED':'int','WHEELCHAIR_ACCESS':'int','ELECTRIC_VEHICLE_CHARGE'	: 'int','COMES_FURNISHED':'int',
'LAUNDRY_OPTIONS':'str','PARKING_OPTIONS':'str','lat':'float','lon':'float','PRICE_PREDICTED':'double','accuracy':'double'
    }


nz_fun_grouped_apply = NZFunGroupedApply(df=idadf, code_str=code_house_prediction_model, index='REGION',fun_name ="house_prediction_model", output_table='properties',output_signature=output_signature)
result_idadf = nz_fun_grouped_apply.get_result()
result = result_idadf.as_dataframe()
print(result)

