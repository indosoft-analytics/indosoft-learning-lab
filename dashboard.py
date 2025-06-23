import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page config (must be first Streamlit command)
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# Sample data function with proper frequency
@st.cache_data
def load_data():
    data = {
        'region': ['North']*12 + ['South']*12 + ['East']*12 + ['West']*12,
        'month': pd.date_range(start='2023-01-01', periods=12, freq='ME').tolist()*4,
        'sales': (np.random.normal(10000, 2000, 48)).astype(int),
        'product': ['A','B','C','D']*12
    }
    return pd.DataFrame(data)

try:
    df = load_data()
    
    # Sidebar filters
    st.sidebar.header('Filters')
    region = st.sidebar.selectbox('Region', df['region'].unique())

    # Filter data
    filtered_df = df[df['region'] == region]

    # Create dashboard
    st.title('Sales Dashboard')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Monthly Sales')
        fig1 = px.line(filtered_df, x='month', y='sales')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader('Product Breakdown')
        fig2 = px.pie(filtered_df, values='sales', names='product')
        st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
