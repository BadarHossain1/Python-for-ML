!pip install pandas
# Install pandas

import pandas as pd

df = pd.read_csv('/content/pizza_types.csv', encoding='latin-1') #import data from excel by copying path

df.head() #prints the excel table data

!ls #Print all the files in the colab