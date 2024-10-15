import streamlit as st

st.header("Custom Operators")
if st.button("한국어"):
    st.subheader("1. 데이터 클리닝 (영어)")
    st.write("**작업**")
    st.write("- 사용자가 인터페이스에서 선택한 데이터 클리닝 기능을 기반으로, 지정된 텍스트 데이터 열에 대한 클리닝 작업을 자동으로 수행함")
    st.write("**오퍼레이터**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- 데이터셋 텍스트 데이터 열")
    st.write("**Ouput Type**")
    st.write("- 데이터셋 + ’cleaned’ 열 추가")
    
    with st.popover("Show the working flow of the operator"):
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
    
    with st.popover("Show the working flow of the operator"):
        st.image('images/dc_kor_flow.png')

    st.divider()

    st.subheader("3. KoNLPy Tokenization")







else:
    st.subheader("1. Data Cleaning (English)")
    st.write("**Work**")
    st.write("- Automatically perform cleaning operations on the specified text data column based on the data cleaning functions selected by the user in the interface.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- DataFrame Text Column")
    st.write("**Ouput Type**")
    st.write("- DataFrame Updated with a column 'cleaned'")

    with st.popover("Show the working flow of the operator"):
        st.image('images/dc_eng_flow.png')

    st.divider()

    st.subheader("2. Data Cleaning (Korean)")
    st.write("**Work**")
    st.write("- Automatically perform cleaning operations on the specified text data column based on the data cleaning functions selected by the user in the interface.")
    st.write("**Operator Used**")
    st.write("- Python Transformer")
    st.write("**Input Type**")
    st.write("- DataFrame Text Column")
    st.write("**Ouput Type**")
    st.write("- DataFrame Updated with a column 'cleaned'")

    with st.popover("Show the working flow of the operator"):
        st.image('images/dc_kor_flow.png')

    st.divider()
    
    st.subheader("3. KoNLPy Tokenization")
    st.markdown("- Komoran Tokenizer")
    st.markdown("- Hannanum Tokenizer")
    st.markdown("- Kkma Tokenizer")
    st.markdown("- Okt Tokenizer")

    option = st.selectbox(
     'Select a tokenizer',
     ('Komoran Tokenizer', 'Hannanum Tokenizer', 'Kkma Tokenizer', 'Okt Tokenizer'))
    
    if option == 'Komoran Tokenizer':
        st.write("***Functions***")
        st.markdown("- morphs \n- pos \n- nouns")
    elif option == 'Hannanum Tokenizer':
        st.write("***Functions***")
        st.markdown("- morphs \n- pos \n- nouns \n- analyze")
    elif option == 'Kkma Tokenizer':
        st.write("***Functions***")
        st.markdown("- morphs \n- pos \n- nouns \n- sentences")
    elif option == 'Okt Tokenizer':
        st.write("***Functions***")
        st.markdown("- morphs \n- pos \n- nouns \n- phrases \n- normalize")


    @st.container("siimmmm")
    def vote(item):
        st.write(f"{item}")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Select a tokenizer")
        if st.button("Komoran Tokenizer"):
            vote("Komoran Tokenizer")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"





