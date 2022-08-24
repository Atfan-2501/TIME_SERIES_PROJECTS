import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import pickle

st.set_page_config(page_title='Walmart_sales_prediction', layout= "wide")

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html = True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


image = Image.open("Walmart.png")
st.image(image, output_format= "png", width=(400))

prophet_pred = pickle.load(open("xgboost_pred.pickle", "rb"))
xg_boost_pred = pickle.load(open("prophet_pred.pickle", "rb"))

stores_list = prophet_pred["Store_Id"].unique()
dept_list = prophet_pred["Dept_Id"].unique()
model_list = ["fbProphet", "xgBoost", "Both"]

col1, col2, col3 = st.columns(3)

with col1:
    store_id = st.selectbox(
    'Enter the store id', stores_list,  
    )

with col2:
    sku_id = st.selectbox(
    'Enter the sku id/ dept id', dept_list
    )
with col3:
    model = st.selectbox(
    'Enter the model to be used for forecast', model_list)

prophet_df = prophet_pred[(prophet_pred["Store_Id"]== store_id) & (prophet_pred["Dept_Id"]== sku_id)]
xgboost_df = xg_boost_pred[(xg_boost_pred["Store_Id"]== store_id) & (xg_boost_pred["Dept_Id"]== sku_id)]

if st.button("Forecast"):    
    if model == "fbProphet":
        with col1:
            st.text("fbProphet")
            st.dataframe(prophet_df)
        with col2:
            st.text("Plot")
            fig = plt.figure(figsize = (10, 10))
            ax = plt.axes()
            ax.set_facecolor('snow')
            sns.lineplot(x = "Date", y = "Weekly_Sales",data = prophet_df)
            plt.legend(["fbProphet", "xgBoost"], fontsize = "large")
            plt.xticks(rotation = 90)
            st.pyplot(fig)
    elif model == "xgBoost":
        with col1:
            st.text("xgBoost")
            st.dataframe(xgboost_df)
        with col2:
            st.text("Plot")
            fig = plt.figure(figsize = (10, 10))
            ax = plt.axes()
            ax.set_facecolor('snow')
            sns.lineplot(x = "Date", y = "Weekly_Sales",data = xgboost_df)
            plt.legend(["fbProphet", "xgBoost"], fontsize = "large")
            plt.xticks(rotation = 90)
            st.pyplot(fig)
    else:
        with col1:
            st.text("fbProphet")
            st.dataframe(prophet_df)
        with col2:
            st.text("xgBoost")
            st.dataframe(xgboost_df)
        with col3:
            st.text("Plot")
            fig = plt.figure(figsize = (10, 10))
            ax = plt.axes()
            ax.set_facecolor('snow')
            sns.lineplot(x = "Date", y = "Weekly_Sales",data = prophet_df)
            sns.lineplot(x = "Date", y = "Weekly_Sales",data = xgboost_df)
            plt.legend(["fbProphet", "xgBoost"], fontsize = "large")
            plt.xticks(rotation = 90)
            st.pyplot(fig)