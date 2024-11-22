## list comprehension
 
#lc_evens = [num for num in range(1, 101) if (num % 2 == 0) & (num % 3 == 0)]
#print(lc_evens)
 
## slow, take a lot of lines
#evens = []
#for num in range(1, 101):
    #if num % 2 == 0:
        #evens.append(num)
 
## print(evens)

import pandas as pd
import glob

path = r"/workspaces/Python-Learning/No Python Sessions/Data"

files = glob.glob(path+"/*.csv")

print(files)

dfs = {}

for f in files:
    df = pd.read_csv(f)

    key_string = f.split("/")[-1][:-17]

    dfs[key_string] = df

dfs = {key:dfs[key] for key in sorted(dfs.keys())}

left_df = dfs['b1_children_in_need']
merge_cols = list(left_df.columns[:10])

new_col_names = [f'b1_children_in_need_{col}' if (not col in merge_cols) else col for col in dfs['b1_children_in_need'].columns]
left_df = left_df.set_axis(new_col_names, axis=1)
 
for key, df in dfs.items():
    if (('headline_figures' not in key) &
        ('mid-year' not in key) &
        ('b1' not in key) &
        (key[0] != 'a')):
 
        df = df.set_axis([f'{key}_{col}' if (not col in merge_cols) else col for col in df.columns], axis=1)
       
        left_df = left_df.merge(df, how='left', on=merge_cols)

left_df.to_csv('merged_cin.csv', index=False)
