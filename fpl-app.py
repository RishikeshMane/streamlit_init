import pandas as pd
import numpy as np
import streamlit as st
import requests
import time
from streamlit_lottie import st_lottie 
from annotated_text import annotated_text
  
 
df = pd.read_excel("sagar_salesq4_summary.xlsx") 
  

progress_text = "Loading App in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
   


tab1, tab2, tab3 = st.tabs(["Category", "Marketing-Group", "Brand"])


with tab1:
    st.header("Category")
    values = ["Select", 500, 1000, 2000, 4000, 5000]
    default_ix = values.index(500)
    col1, col2 = st.columns(2)
    with col1:
        if values == "Select":
            st.warning("Choose the integers from the list in the dropdown")
        else:
            option = st.selectbox("Select the Range below ⤵️", values, index=default_ix)
        # print(int(option))
        df_sin = df[:option]

    with col2:
        Category = list(df_sin["Category"].drop_duplicates())
        Category_choice = st.selectbox(
            "Select the Category below ⤵️", Category, index=default_ix
        )
        
    st.sidebar.title("UnruffledFeathers")
    df_DATA1 = df_sin[df_sin["Category"].isin([Category_choice])]


    st.dataframe(df_DATA1, use_container_width=True)

    placeholder = st.empty()

    quantity_data = df_DATA1["Total_Quantity"]
    mr_data = df_DATA1["Marketing Group"].drop_duplicates()
    quantity_calculation = df_DATA1["Total_Quantity"]
    amount_calculation = df_DATA1["Total_Amount"]

    amount_mean = df_DATA1["Total_Amount"].mean()
    linchart_data = pd.DataFrame(df_DATA1["Size"], df_DATA1["Total_Amount"])

    length_quantitiy = sum(quantity_calculation)
    amount_calculation = sum(amount_calculation)


    mr_data = list(mr_data.drop_duplicates())


    values_default = [0]
    default_ix_none = values_default.index(0)
    st.dataframe(mr_data, use_container_width=True)
    len_mr_data = len(mr_data)
    import time

    with placeholder.container():
        with st.spinner("Loading Data"):
            time.sleep(2)
            # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(
            label="Total quantity calculated",
            value=length_quantitiy,
        )
        kpi2.metric(label="Sum Amount calculated", value=amount_calculation)
        kpi3.metric(label="Amount Mean value", value=amount_mean)


    st.bar_chart(df_DATA1, x="Size", y="Total_Amount")









with tab2:
    st.header("Marketing-Group")
    values = ["Select", 500, 1000, 2000, 4000, 5000]
    default_ix = values.index(500)
    col1, col2  = st.columns(2)
    with col1:
        if values == "Select":
            st.warning("Choose the integers from the list in the dropdown")
        else:
            option = st.selectbox("Select the Range below ⤵️", values, index=default_ix,key='02')
        # print(int(option))
        df_sin = df[:option]

    with col2:
        Category = list(df_sin["Category"].drop_duplicates())
        Category_choice = st.selectbox(
            "Select the Category below ⤵️", Category, index=default_ix,key='03'
        )

    
    df_DATA1 = df_sin[df_sin["Category"].isin([Category_choice])]
    uniqure_mr_group    = df_DATA1.sort_values(["Marketing Group","Brand"])
    uniqure_mr_group01   = uniqure_mr_group["Marketing Group"].drop_duplicates()
    unique_brand        = uniqure_mr_group["Brand"].drop_duplicates()
    
    
    #print("list is",uniqure_mr_group01)
    mr_data_mt = list(uniqure_mr_group01.drop_duplicates())
    Mr_01_choice = st.selectbox(
            "Select the Marketing Group below - ", mr_data_mt,key='04'
        )
    
    
    uniqure_mr_group = uniqure_mr_group[uniqure_mr_group["Marketing Group"].isin([Mr_01_choice])]
    st.dataframe(uniqure_mr_group, use_container_width=True)
    placeholder = st.empty()


    quantity_calculation = uniqure_mr_group["Total_Quantity"]
    amount_calculation = uniqure_mr_group["Total_Amount"]

    amount_mean = df_DATA1["Total_Amount"].mean()
    linchart_data = pd.DataFrame(df_DATA1["Size"], df_DATA1["Total_Amount"])

    length_quantitiy = sum(quantity_calculation)
    amount_calculation = sum(amount_calculation)
    values_default = [0]
    default_ix_none = values_default.index(0)
    len_mr_data = len(mr_data)
    
    import time

    with placeholder.container():
        with st.spinner("Loading Data"):
            time.sleep(2)
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(
            label="Total quantity calculated",
            value=length_quantitiy,
        )
        kpi2.metric(label="Sum of Amount calculated", value=amount_calculation)
        kpi3.metric(label="Amount Mean value", value=amount_mean)


    st.bar_chart(uniqure_mr_group, x="Size", y="Total_Amount")


with tab3:
    st.header("Brand")
