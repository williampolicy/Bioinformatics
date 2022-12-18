# Import necessary libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client


#@title
# Target search for coronavirus
target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)
targets

#@title
selected_target = targets.target_chembl_id[4]
selected_target

#@title
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

#@title
df = pd.DataFrame.from_dict(res)

#@title
df.head(3)




#@title
df.to_csv('bioactivity_data_raw.csv', index=False)


# Handling missing data
#@title
df2 = df[df.standard_value.notna()]
df2