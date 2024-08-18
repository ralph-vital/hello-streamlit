from dotenv import load_dotenv
# import os
# import snowflake.connector
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
# USER = os.getenv('user'),
# PASSWORD = os.getenv('password'),
# ACCOUNT = os.getenv('account'),
# WAREHOUSE = os.getenv('warehouse'),
# DATABASE = os.getenv('database'),
# SCHEMA = os.getenv('schema'),

# conn = snowflake.connector.connect(
#    user=USER,
#    password=PASSWORD,
#    account=ACCOUNT,
#    warehouse=WAREHOUSE,
#    database=DATABASE,
#    schema=SCHEMA,
# )
st.title('Tuberculosis Indicators for Haiti')

text = """
       # Context
       Haiti is the poorest nation in the Western Hemisphere and has the highest rate of tuberculosis (TB) in the region, with an estimated incidence of 200 per 100,000 population in the beginning of 2000. Despite all the efforst from the goverment and NGO, Haiti still suffers 140 TB cases per 100,000 residents, or 40 times the rate in the United State. This dashbord display a list of indicators and their evolution from 2010 to 2022.
        """

st.markdown(text)

st.divider()

# dataframe healt h data
health_df = pd.read_csv(
    './haiti_health/tuberculosis_indicators_hti.csv', header=0,  skiprows=[1,])

# all columns
all_col = health_df.columns

col_pick = all_col[0]


code = health_df[col_pick].unique()

code_pick = list(code)[0]

option = st.selectbox(
    "Choose an indicator",
    tuple(code),
)

code_df = health_df[health_df['GHO (CODE)'] == option]

code_df = code_df.sort_values(by=['YEAR (DISPLAY)'])

title = code_df['GHO (DISPLAY)'].unique()
# st.dataframe(code_df)

fig = go.Figure(
    [go.Scatter(x=code_df['YEAR (DISPLAY)'], y=code_df['Numeric'])])

fig_2 = px.line(code_df, x='YEAR (DISPLAY)', y="Numeric", title=title[0])


fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green")

st.plotly_chart(fig_2)
