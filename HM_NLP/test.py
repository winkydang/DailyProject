# import matplotlib.pyplot as plt
#
# # Set the fivethirtyeight style
# plt.style.use('fivethirtyeight')
#
# # Your code to create and display the plot goes here
# plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.title('Title of the Plot')
# plt.show()


# import matplotlib
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
#
# # Set the font that supports Chinese characters (e.g., SimHei)
# # matplotlib.rcParams['font.family'] = 'SimHei'
# # matplotlib.rcParams['font.family'] = 'NotoSerifSC'
#
# # Assuming train_data is a pandas DataFrame with a column named 'label'
#
# # Set the style (optional, for aesthetics)
# sns.set_style("whitegrid")
#
# train_data = pd.read_csv(filepath_or_buffer='./cn_data/train.tsv', sep='\t')
#
# # Create the count plot
# sns.countplot(x='label', data=train_data)
# # sns.countplot(x=[0, 3, 3, 3, 9], data=train_data)
#
# font = FontProperties(fname=r'/Users/pc/Library/Fonts/NotoSerifSC-ExtraLight.otf', size=12)
#
# # Add labels and title to the plot
# plt.xlabel('Label')
# plt.ylabel('总和', fontproperties=font)
# plt.title('Distribution of Labels')
#
# # Show the plot
# plt.show()
#


