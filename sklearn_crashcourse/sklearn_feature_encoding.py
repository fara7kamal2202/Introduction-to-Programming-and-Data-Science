from sklearn.datasets import fetch_openml
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import pandas as pd


data = fetch_openml('car', as_frame=True).frame
columns_to_encode = ['lug_boot', 'safety']

encoder = OrdinalEncoder(
    categories=[['small', 'med', 'big'],
                ['low', 'med', 'high']
                ]
)
data[columns_to_encode] = encoder.fit_transform(data[columns_to_encode])
#___________________________________________________________________________

data = fetch_openml('adult', as_frame=True).frame
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_values = encoder.fit_transform(data[['occupation', 'race']])
new_cols = encoder.get_feature_names_out(['occupation', 'race'])
df_encoded = pd.DataFrame(encoded_values, columns=new_cols, index=data.index)
data_final = pd.concat([data.drop(columns= ['occupation', 'race']), df_encoded], axis=1)

print(data_final)