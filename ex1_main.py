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
# Here, we will retrieve only bioactivity data for 
# coronavirus 3C-like proteinase (CHEMBL3927) that are reported as 
# IC 50  values in nM (nanomolar) unit.
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


#@title
bioactivity_class = []
for i in df2.standard_value:
  if float(i) >= 10000:
    bioactivity_class.append("inactive")
  elif float(i) <= 1000:
    bioactivity_class.append("active")
  else:
    bioactivity_class.append("intermediate")


#@title
selection = ['molecule_chembl_id','canonical_smiles','standard_value']
df3 = df2[selection]
df3

#@title
bioactivity_class = pd.Series(bioactivity_class, name='bioactivity_class')
df4 = pd.concat([df3, bioactivity_class], axis=1)
df4

print('-- show result df4：\n')
print(df4)
#@title
df4.to_csv('bioactivity_data_preprocessed.csv', index=False)


