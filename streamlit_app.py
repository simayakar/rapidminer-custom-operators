import streamlit as st
import pandas as pd

import streamlit_antd_components as sac

sac.menu([
    sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
    sac.MenuItem('products', icon='box-fill', children=[
        sac.MenuItem('apple', icon='apple'),
        sac.MenuItem('other', icon='git', description='other items', children=[
            sac.MenuItem('google', icon='google', description='item description'),
            sac.MenuItem('gitlab', icon='gitlab'),
            sac.MenuItem('wechat', icon='wechat'),
        ]),
    ]),
    sac.MenuItem('disabled', disabled=True),
    sac.MenuItem(type='divider'),
    sac.MenuItem('link', type='group', children=[
        sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
        sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
    ]),
], index=2, size='sm', color='red', open_all=True)

st.title("RapidMiner Custom Operators :gear:")

st.divider()

st.header("Python Operators")

df = pd.DataFrame(
    {
     'Operator Name': ["Python Transform", 
     "Python Execute", "Python Learner", "Python Forecast"]}
)

st.write(df)


st.header('Operator Info')

option = st.selectbox(
     'Select an operator',
     ('Python Execute', 'Python Transform', 'Python Forecast', 'Python Learner'))

if option == 'Python Execute':
    st.write("This operator enables users to run Python scripts within a RapidMiner process. It allows for the seamless integration of Python functions and libraries into RapidMiner workflows, passing input data from RapidMiner to Python and returning processed results back to RapidMiner.")
elif option == 'Python Transform':
    st.write("This operator is used to transform data using a custom Python script. It is particularly useful for performing complex transformations or feature engineering that may not be available in RapidMiner's native toolset, while still keeping the process within the RapidMiner environment.")
elif option == 'Python Learner':
    st.write("The Python Learner operator lets you create machine learning models in Python, using popular libraries such as scikit-learn. Once the model is trained, it can be applied within RapidMiner for predictions, evaluations, and performance assessments, combining Python’s flexibility with RapidMiner's data handling capabilities.")
elif option == 'Python Forecast':
    st.write("This operator is designed for time series forecasting using Python libraries. It allows users to build and apply forecasting models in Python and integrate the results with other RapidMiner processes for further analysis or reporting.")