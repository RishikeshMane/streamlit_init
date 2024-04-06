import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns

st.title("Unruffledfeathers")
df = pd.read_excel("sagar_salesq4_summary.xlsx")


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
        print(int(option))
        df_sin = df[:option]

    with col2:
        Category = list(df_sin["Category"].drop_duplicates())
        Category_choice = st.selectbox(
            "Select the Category below ⤵️", Category, index=default_ix
        )


# MarketingGroup = list(df_sin['Marketing Group'].drop_duplicates())
    st.sidebar.markdown("### Data Filters")
    df_DATA1 = df_sin[df_sin["Category"].isin([Category_choice])]


    st.dataframe(df_DATA1, use_container_width=True)

    placeholder = st.empty()

    quantity_data = df_DATA1["Total_Quantity"]
    mr_data = df_DATA1["Marketing Group"].drop_duplicates()
    quantity_calculation = df_DATA1["Total_Quantity"]
    amount_calculation = df_DATA1["Total_Amount"]

    amount_mean = df_DATA1["Total_Amount"].mean()


    # linchart_data     = df_DATA1['']

    linchart_data = pd.DataFrame(df_DATA1["Size"], df_DATA1["Total_Amount"])

    length_quantitiy = sum(quantity_calculation)
    amount_calculation = sum(amount_calculation)


    mr_data = list(mr_data.drop_duplicates())


    values_default = [0]
    default_ix_none = values_default.index(0)
    # teams_choice = st.selectbox("Select the MarketingGroup below", mr_data,index=default_ix_none)


    st.dataframe(mr_data, use_container_width=True)


    # st.title(length_quantitiy)
    # st.title(amount_calculation)


    len_mr_data = len(mr_data)
    import time

    with placeholder.container():
        with st.spinner("Loading Data"):
            time.sleep(2)
            # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs

        kpi1.metric(
            label="Total quantity calculated",
            value=length_quantitiy,
            # delta=round(len_mr_data) - 10,
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
        print(int(option))
        df_sin = df[:option]

    with col2:
        Category = list(df_sin["Category"].drop_duplicates())
        Category_choice = st.selectbox(
            "Select the Category below ⤵️", Category, index=default_ix,key='03'
        )


    # MarketingGroup = list(df_sin['Marketing Group'].drop_duplicates())
    #st.sidebar.markdown("### Data Filters")
    


    #implementing parsing on Marketing group
    mrgroup = list(df_sin["Marketing Group"].drop_duplicates())
    Category_choice = st.selectbox(
            "Select the Category below ⤵️", mrgroup, index=default_ix,key='01'
        )
    
    
    
    
    
    
    
    
    df_DATA1 = df_sin[df_sin["Category"].isin([Category_choice])]
    st.dataframe(df_DATA1, use_container_width=True)

    placeholder = st.empty()

    quantity_data = df_DATA1["Total_Quantity"]
    mr_data = df_DATA1["Marketing Group"].drop_duplicates()
    quantity_calculation = df_DATA1["Total_Quantity"]
    amount_calculation = df_DATA1["Total_Amount"]

    amount_mean = df_DATA1["Total_Amount"].mean()


    # linchart_data     = df_DATA1['']

    linchart_data = pd.DataFrame(df_DATA1["Size"], df_DATA1["Total_Amount"])

    length_quantitiy = sum(quantity_calculation)
    amount_calculation = sum(amount_calculation)


    mr_data = list(mr_data.drop_duplicates())


    values_default = [0]
    default_ix_none = values_default.index(0)
    # teams_choice = st.selectbox("Select the MarketingGroup below", mr_data,index=default_ix_none)


    st.dataframe(mr_data, use_container_width=True)


    # st.title(length_quantitiy)
    # st.title(amount_calculation)


    len_mr_data = len(mr_data)
    import time

    with placeholder.container():
        with st.spinner("Loading Data"):
            time.sleep(2)
            # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs

        kpi1.metric(
            label="Total quantity calculated",
            value=length_quantitiy,
            # delta=round(len_mr_data) - 10,
        )

        kpi2.metric(label="Sum Amount calculated", value=amount_calculation)

        kpi3.metric(label="Amount Mean value", value=amount_mean)


    st.bar_chart(df_DATA1, x="Size", y="Total_Amount")


with tab3:
    st.header("Brand")
