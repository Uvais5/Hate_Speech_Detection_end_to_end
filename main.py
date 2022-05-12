from copyreg import pickle
import streamlit as st 
import pickle
import numpy as np 
from sklearn.tree import DecisionTreeClassifier

st.title("Hate Speech Detection") 

speech = st.text_input('Enter any Speech for detection', '')


model = pickle.load(open('hate_speech_model.pkl',"rb")) 
cv = pickle.load(open("cv.pkl","rb"))

data = cv.transform([speech]).toarray()
pred = model.predict(data)




if st.button('Click when you ready'):
    if pred == "Offensive Language":
        st.write("offense")
        st.markdown("""<style>.big-font {font-size:100px !important;}</style>""",unsafe_allow_html=True)
        st.markdown('<p class="big-font">Offensive Language </p>', unsafe_allow_html=True)

    elif pred == "NO Hate and Offensive":
        st.write("NO Hate and Offenive")
        st.markdown("""<style>.big-font {font-size:80px !important;}</style>""", unsafe_allow_html=True)
        st.markdown('<p class="big-font">No Hate and Offense Language founded </p>', unsafe_allow_html=True)

    elif pred == "Hate Speech":
        st.write("Hate Speech")

        st.markdown("""<style>.big-font {font-size:100px !important;}</style>""", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Hate Speech </p>', unsafe_allow_html=True)
    elif pred == " ":
        st.write("NOFound ")



m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #008CBA ;
    padding: 13px 280px;
}
</style>""", unsafe_allow_html=True)


# def main():

# if __name__=='__main__':
#     main()
# rgb(200, 49, 49)
