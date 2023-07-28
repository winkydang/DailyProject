import pandas as pd

t1 = (3, 4)
source_col = 1
counterpart_col = 3
df_source_fenci = pd.DataFrame({'a':1}, index = [0])
len_counterpart_col = 12
len_source_col = 13
df_result = []
df_source = []
source_col_name = 'aa'
counterpart_col_name = 'bb'
args = t1 + (source_col, counterpart_col, df_source_fenci, len_counterpart_col, len_source_col, df_result, df_source, source_col_name, counterpart_col_name)
print(args)