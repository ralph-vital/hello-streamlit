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

tab1, tab2, tab3 = st.tabs(["Turbeculosis", "Malaria", "Child Mortality"])
tab1.title('Tuberculosis Indicators for Haiti')
tab2.title('Malaria Indicators for Haiti')
tab3.title('Child Mortality Indicators for Haiti')

text1 = """
       # Context
       Haiti is the poorest nation in the Western Hemisphere and has the highest rate of tuberculosis (TB) in the region, with an estimated incidence of 200 per 100,000 population in the beginning of 2000. Despite all the efforst from the goverment and NGO, Haiti still suffers 140 TB cases per 100,000 residents, or 40 times the rate in the United State. This dashbord display a list of indicators and their evolution from 2010 to 2022.
        """

text2 = """
An endemic-epidemic disease, malaria is beginning to take on alarming proportions in Haiti. According to a document titled 'Epidemiological Profile' published by the Ministry of Public Health and Population (MSPP), with the help of PAHO/WHO, malaria was the 10th leading cause of death among men in 1997-1998. Although it no longer ranked among the top ten causes of death in 1999, the number of identified cases continues to increase
      
      """

text3 = """"
    Although Haiti's infant mortality rate, defined as 'the number of deaths of children under one year of age per number of live births,' is significantly higher than the global average, it has greatly decreased in recent decades. In 2000, it was 74.4 deaths per 1,000 births. However, Haiti lags significantly behind compared to other countries in the Americas. Thoses graphes show the evolution of cetain indicators thought out the years.

     """

tab1.markdown(text1)

tab1.divider()

tab2.markdown(text2)
tab2.divider()


tab3.markdown(text3)
tab3 .divider()
# dataframe healt h data
health_df = pd.read_csv(
    './haiti_health/tuberculosis_indicators_hti.csv', header=0,  skiprows=[1,])

malaria_df = pd.read_csv(
    './haiti_health/malaria_indicators_hti.csv', header=0,  skiprows=[1,])

child_df = pd.read_csv(
    './haiti_health/child_mortality_indicators_hti.csv', header=0,  skiprows=[1,])

print(child_df.head())


def get_title(df: pd.DataFrame, option) -> list:
    df = df[df['GHO (CODE)'] == option]
    title = df['GHO (DISPLAY)'].unique()[0]
    return title


def get_indicator(df: pd.DataFrame) -> list:
    all_col = df.columns
    col_pick = all_col[0]  # get first column
    code = df[col_pick].unique()  # get all the indicator
    return code


h_code = get_indicator(health_df)
h_option = tab1.selectbox(
    "Choose an indicator",
    tuple(h_code),
)

c_dim_option = tab3.selectbox(
    "Choose a dimension",
    tuple(child_df['DIMENSION (NAME)'].unique()),
)

h_title = get_title(health_df, h_option)


m_code = get_indicator(malaria_df)
m_option = tab2.selectbox(
    "Choose an indicator",
    tuple(m_code),
)
m_title = get_title(malaria_df, m_option)


c_code = get_indicator(child_df)
c_option = tab3.selectbox(
    "Choose an indicator",
    tuple(c_code),
)
c_title = get_title(child_df, c_option)


def get_figure(df: pd.DataFrame, option, title):
    code_df = df[df['GHO (CODE)'] == option]
    code_df = code_df.sort_values(by=['YEAR (DISPLAY)'])
    fig_2 = px.line(code_df, x='YEAR (DISPLAY)', y="Numeric", title=title)
    return fig_2


t_fig = get_figure(health_df, h_option, h_title)
m_fig = get_figure(malaria_df, m_option, m_title)


code_df = health_df[health_df['GHO (CODE)'] == h_option]
code_df = code_df.sort_values(by=['YEAR (DISPLAY)'])
fig_2 = px.line(code_df, x='YEAR (DISPLAY)', y="Numeric", title=h_title)

malaria_df = malaria_df[malaria_df['GHO (CODE)'] == m_option]
malaria_df = malaria_df.sort_values(by=['YEAR (DISPLAY)'])
fig_m = px.line(malaria_df, x='YEAR (DISPLAY)', y="Numeric", title=m_title)


c_df = child_df[(child_df['GHO (CODE)'] == c_option) & (
    child_df['DIMENSION (NAME)'] == c_dim_option)]
c_df = c_df.sort_values(by=['YEAR (DISPLAY)'])
c_fig = px.line(c_df, x='YEAR (DISPLAY)', y="Numeric", title=c_title)

tab1.plotly_chart(t_fig)

tab2.plotly_chart(fig_m)

tab3.plotly_chart(c_fig)
