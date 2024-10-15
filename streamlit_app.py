import streamlit as st
import pandas as pd

import streamlit_antd_components as sac


st.title("RapidMiner Custom Operators :gear:")

st.divider()

st.header("Rapidminer Python Operators")

st.markdown("- Python Transform")
st.markdown("- Python Execute")
st.markdown("- Python Learner")
st.markdown("- Python Forecast")

st.header('Operator Info')

option = st.selectbox(
     'Select an operator',
     ('Python Execute', 'Python Transform', 'Python Forecast', 'Python Learner'))

if option == 'Python Execute':
    if st.button("한국어"):
        st.markdown("- Python 코드를 실행하여 데이터 전처리, 분석 등을 수행")
        st.markdown("- Pandas, NumPy 등 라이브러리를 활용 가능")
        st.markdown("- Python에서 처리한 데이터를 RapidMiner로 반환")
    else:
        st.write("- This operator enables users to run Python scripts within a RapidMiner process. It allows for the seamless integration of Python functions and libraries into RapidMiner workflows, passing input data from RapidMiner to Python and returning processed results back to RapidMiner.")
elif option == 'Python Transform':
    if st.button("한국어"):
        st.markdown("- Python 코드를 사용해 데이터를 변환")
        st.markdown("- 텍스트 벡터화 및 사용자 정의 변환 작업에 적합")
        st.markdown("- Python 기반 모델을 RapidMiner 프로세스에서 사용할 수 있음")
    else:
        st.write("- This operator is used to transform data using a custom Python script. It is particularly useful for performing complex transformations or feature engineering that may not be available in RapidMiner's native toolset, while still keeping the process within the RapidMiner environment.")
elif option == 'Python Learner':
    if st.button("한국어"):
        st.markdown("- 머신러닝 알고리즘으로 데이터 학습 및 모델 생성")
        st.markdown("- Python Transformer를 통해 사용자 정의 모델 학습 가능")
    else:
        st.write("- The Python Learner operator lets you create machine learning models in Python, using popular libraries such as scikit-learn. Once the model is trained, it can be applied within RapidMiner for predictions, evaluations, and performance assessments, combining Python’s flexibility with RapidMiner's data handling capabilities.")
elif option == 'Python Forecast':
    if st.button("한국어"):
        st.markdown("- 시계열 데이터를 예측")
        st.markdown("- Python에서 예측 모델을 학습해 RapidMiner에서 사용 가능")
    else:
        st.write("- This operator is designed for time series forecasting using Python libraries. It allows users to build and apply forecasting models in Python and integrate the results with other RapidMiner processes for further analysis or reporting.")

