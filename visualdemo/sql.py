import streamlit as st
import pandas as pd
from PIL import Image
import time
img= Image.open("mix.png")
st.image(img,width=300)
st.markdown("<h1 style='text-align: center; color: Black;'>SQL QUERY ELABORATOR</h1>", unsafe_allow_html=True)
text=st.text_area("Enter the Query here :")
sub=st.button("Submit")
if sub and text.startswith("calculate_patient_risk",17,46) :
    my_bar=st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete+1)
    st.subheader("Technical and Functional Documents")
    files = open('q2k.txt',"r")
    if files:
        for line in files:
            st.write(line)
        st.subheader("Flow chart")
        img1 = Image.open("22fc.png")
        st.image(img1, width=500)
        st.subheader("ER diagram")
        img2 = Image.open("22er.png")
        st.image(img2, width=500)
elif sub and text.startswith("calculate_and_report_commissions",17,49):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    st.subheader("Technical and Functional Documents :")
    file1=open('q1k.txt',"r")
    if file1:
        for line in file1:
            st.write(line)
        st.subheader("Flow chart")
        img3 = Image.open("11fc.png")
        st.image(img3, width=500)
        st.subheader("ER diagram")
        img4 = Image.open("11er.png")
        st.image(img4, width=500)
elif sub and text.startswith("CompanyDB",4,13):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    st.subheader("Technical and Functional Documents")
    file2=open('q3k.txt',"r")
    if file2:
        for line in file2:
            st.write(line)
        st.subheader("Flow chart")
        img5 = Image.open("33fc.png")
        st.image(img5, width=500)
        st.subheader("ER diagram")
        img6 = Image.open("33er.png")
        st.image(img6, width=500)













