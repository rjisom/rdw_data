import streamlit

import pandas
streamlit.title('RDW Vehicle Data')
# connect to data


# put the dafta into a dataframe
df = pandas.DataFrame(my_data)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
data_list = df[0].values.tolist()

streamlit.write('Data1: ', df2[1])
streamlit.write('Data2: ',df2[2])
streamlit.write('Data3: ',df2[3])
