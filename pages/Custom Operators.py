import streamlit as st

st.header("Custom Operators")
if st.button("한국어", icon=":material/language:"):
    st.subheader("1. 데이터 클리닝 (영어)")
    st.write("**작업**")
    st.write("- 사용자가 인터페이스에서 선택한 데이터 클리닝 기능을 기반으로, 지정된 텍스트 데이터 열에 대한 클리닝 작업을 자동으로 수행함")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- 데이터셋 텍스트 데이터 열")
    st.write("**Ouput Type**")
    st.write("- 데이터셋 + ’cleaned’ 열 추가")
    
    #st.page_link("pages/Introduction.py", label="**Page 1**", icon="1️⃣")
    
    with st.popover("오페레이터의 흐름을 살펴보기"):
        st.image('images/dc_eng_flow.png')

    st.divider()
    st.subheader("2. 데이터 클리닝 (한국어)")
    st.write("**작업**")
    st.write("- 사용자가 인터페이스에서 선택한 데이터 클리닝 기능을 기반으로, 지정된 텍스트 데이터 열에 대한 클리닝 작업을 자동으로 수행함")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- 데이터셋 텍스트 데이터 열")
    st.write("**Ouput Type**")
    st.write("- 데이터셋 + ’cleaned’ 열 추가")
    
    with st.popover("오페레이터의 흐름을 살펴보기"):
        st.image('images/dc_kor_flow.png')

    st.divider()
    col1, col2 = st.columns([3, 1])
    col1.subheader("3. KoNLPy 토큰화")
    col1.write("**작업**")
    col1.write("- 한국어 텍스트 데이터 토큰화")
    col1.write("**오퍼레이터**")
    col1.write("- Python Transformer")
    col1.write("**Input Type**")
    col1.write("- 데이터셋 텍스트 데이터 열")
    col1.write("**Ouput Type**")
    col1.write("- 데이터셋 + ’tokens’ 열 추가")
    col2.write("")
    col2.write("**Tokenizers**")
    col2.markdown("- Komoran Tokenizer")
    col2.markdown("- Hannanum Tokenizer")
    col2.markdown("- Kkma Tokenizer")
    col2.markdown("- Okt Tokenizer")


    option = st.selectbox(
     'Select a tokenizer',
     ( 'Select a tokenizer', 'Komoran Tokenizer', 'Hannanum Tokenizer', 'Kkma Tokenizer', 'Okt Tokenizer'))
    
   
    c = st.container(border=True)
    if option == 'Select a tokenizer':
        st.write("")
    elif option == 'Komoran Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns")
        c.write("**Note:**")
        c.markdown("- 특정 이름이나 구문이 단일 토큰으로 처리되도록 하는 'userdict'라는 매개변수를 지원")
        c.markdown("- 사용자는 자신의 `.txt` 파일을 업로드하여 맞춤형 토큰화를 설정할 수 있음")
        c.image('images/komoran_flow.png')
    elif option == 'Hannanum Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- analyze")
        c.image('images/hannanum_flow.png')
    elif option == 'Kkma Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- sentences")
        c.image('images/kkma_flow.png')
    elif option == 'Okt Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- phrases \n- normalize")
        c.image('images/okt_flow.png')
    
    st.divider()
    st.subheader("4. 텍스트 전처리")
    st.write("**작업**")
    st.write("- 텍스트 데이터를 사용하여 다양한 벡터화 방식을 적용하는 사용자 정의 파이썬 변환기")
    st.write("- 토큰화된 텍스트 컬럼을 선택하여 TF-IDF, Term Frequency, Term Occurences, 또는 Binary 벡터화를 수행할 수 있음")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- 데이터셋 토큰리스트 열")
    st.write("**Ouput Type**")
    st.write("1. 데이터셋")
    st.write("2. 벡터화 결과 데이터셋")
    with st.popover("오페레이터의 흐름을 살펴보기"):
        st.image('images/processing_flow.png')
    
    st.divider()
    st.subheader("5. BERTopic")
    st.write("**작업**")
    st.write("- 토픽 모델링 작업을 자동으로 수행하며, 각 문서에 대해 토픽의 확률을 표시")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- 데이터셋 텍스트 데이터 열")
    st.write("**Ouput Type**")
    st.write("1. 각 문서에 대한 토픽과 토픽의 확률")
    st.write("2. 토픽에 대한 정보")
    with st.popover("오페레이터의 흐름을 살펴보기"):
        st.image('images/bert_flow.png')
    
    st.divider()
    st.subheader("6. Tomotopy 일관성 점수")
    st.write("**작업**")
    st.write("- Tomotopy로 생성된 토픽 모델의 일관성 점수를 계산하며, Gensim 라이브러리를 활용한다. 이 오퍼레이터는 각 토픽의 상위 단어들이 얼마나 의미적으로 관련이 있는지를 측정하여 토픽의 품질을 평가한다.")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
    
    st.divider()
    st.subheader("7. Tomotopy LDA 토픽모델링")
    st.write("**작업**")
    st.write("- 사용자가 선택한 토픽 수에 따라 Tomotopy LDA 토픽 모델링을 적용한다.")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')



else:
    st.subheader("1. Data Cleaning (English)")
    st.write("**Work**")
    st.write("- Automatically perform cleaning operations on the specified text data column based on the data cleaning functions selected by the user in the interface.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset Text Column")
    st.write("**Ouput Type**")
    st.write("- Dataset updated with a column 'cleaned'")

    with st.popover("Show the workflow of the operator"):
        st.image('images/dc_eng_flow.png')

    st.divider()

    st.subheader("2. Data Cleaning (Korean)")
    st.write("**Work**")
    st.write("- Automatically perform cleaning operations on the specified text data column based on the data cleaning functions selected by the user in the interface.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset Text Column")
    st.write("**Ouput Type**")
    st.write("- Dataset updated with a column 'cleaned'")

    with st.popover("Show the workflow of the operator"):
        st.image('images/dc_kor_flow.png')

    st.divider()

    col1, col2 = st.columns([3, 1])
    col1.subheader("3. KoNLPy Tokenization")
    col1.write("**Work**")
    col1.write("- Korean text tokenization")
    col1.write("**Operator Used**")
    col1.write("- Python Transformer")
    col1.write("**Input Type**")
    col1.write("- Dataset Text Column")
    col1.write("**Ouput Type**")
    col1.write("- Dataset updated with a column 'tokens'")
    
    col2.write("")
    col2.write("**Tokenizers**")
    col2.markdown("- Komoran Tokenizer \n-  Hannanum Tokenizer \n- Kkma Tokenizer \n- Okt Tokenizer")


    option = st.selectbox(
     'Select a tokenizer',
     ( 'Select a tokenizer', 'Komoran Tokenizer', 'Hannanum Tokenizer', 'Kkma Tokenizer', 'Okt Tokenizer'))
    
   
    c = st.container(border=True)
    if option == 'Select a tokenizer':
        st.write("")
    elif option == 'Komoran Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns")
        c.write("**Note:**")
        c.markdown("- You can specify the 'userdict' parameter to ensure that specific names or phrases are treated as single tokens.")
        c.markdown("- Users can upload their own `.txt` file to configure custom tokenization.")
        c.image('images/komoran_flow.png')
    elif option == 'Hannanum Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- analyze")
        c.image('images/hannanum_flow.png')
    elif option == 'Kkma Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- sentences")
        c.image('images/kkma_flow.png')
    elif option == 'Okt Tokenizer':
        c.write("***Functions***")
        c.markdown("- morphs \n- pos \n- nouns \n- phrases \n- normalize")
        c.image('images/okt_flow.png')
   
    st.divider()
    st.subheader("4. Text Processing")
    st.write("**Work**")
    st.write("- A custom Python transformer that applies various vectorization methods to text data.")
    st.write("- You can select a tokenized text column to perform TF-IDF, Term Frequency, Term Occurrences, or Binary vectorization.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset token list column")
    st.write("**Ouput Type**")
    st.write("1. Dataset")
    st.write("2. Vectorized dataset")
    with st.popover("Show the workflow of the operator"):
        st.image('images/processing_flow.png')
        
    st.divider()
    st.subheader("5. BERTopic")
    st.write("**Work**")
    st.write("- Automatically perform topic modeling and display the probabilities of all topics for each document.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
        
    st.divider()
    st.subheader("6. Tomotopy Coherence Score")
    st.write("**Work**")
    st.write("- Calculates the coherence scores for topic models created with Tomotopy, utilizing the Gensim library. This operator evaluates the quality of topics by measuring their coherence, which indicates how semantically related the top words in each topic are.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
        
    st.divider()
    st.subheader("7. Tomotopy LDA Topic Modeling")
    st.write("**Work**")
    st.write("- Applies Tomotopy LDA topic modeling based on the number of topics selected by the user.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
        
    st.divider()
    st.subheader("8. LightGBM")
    st.write("**Work**")
    st.write("- Applies Tomotopy LDA topic modeling based on the number of topics selected by the user.")
    st.write("**Operator Used**")
    st.write("- Python Learner")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
        
    st.divider()
    st.subheader("9. Sentiment Scores [TextBlob]")
    st.write("**Work**")
    st.write("- Applies Tomotopy LDA topic modeling based on the number of topics selected by the user.")
    st.write("**Operator Used**")
    st.write("- Python Execute")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
    
    st.divider()
    st.subheader("10. Prophet Forecasting")
    st.write("**Work**")
    st.write("- Applies Tomotopy LDA topic modeling based on the number of topics selected by the user.")
    st.write("**Operator Used**")
    st.write("- Python Forecast")
    st.write("**Input Type**")
    st.write("- Dataset text column")
    st.write("**Ouput Type**")
    st.write("1. ????????Topic and topic probabilities for each document")
    st.write("2. Topic information")
    with st.popover("Show the workflow of the operator"):
        st.image('images/bert_flow.png')
    
    







