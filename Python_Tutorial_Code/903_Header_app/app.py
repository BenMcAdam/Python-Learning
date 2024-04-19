import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Utilitites
def data_cleaner(df):
    '''
    Cleans 903 header and adds age column

    Arguments:
    df -> DataFrame of 903 header data to be cleaned

    returns :
    df -> DataFrame of 903 data with SEX correctly mapped and AGE column added
    '''
    # TODO map SEX to male/female
    # TODO calculate ages - change DoB to datetome
    # TODO drop excess columns
    df['SEX'] = df['SEX'].map({1:'Male',
                               2:'Female'})
    
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')
    df['AGE'] = pd.to_datetime('today').normalize() - df['DOB']
    df['AGE'] = (df['AGE'] / np.timedelta64(1, 'Y')).astype('int')

    df = df[['SEX', 'AGE', 'ETHNIC']]

    return df

# Plotting Functions
def age_bar(df):
    fig = px.histogram(df, 
                       x='SEX',
                       title = 'Breakdown by gender of 903 data',
                       labels={'SEX':'Sex of Children'})
                       #color = 'ETHNIC')
    
    return fig

def ethnicity_pie(df):
    ethnic_count = df.groupby('ETHNIC')['ETHNIC'].count().reset_index(name='count')

    fig = px.pie(ethnic_count, 
                 values='count',
                 names='ETHNIC',
                 title = 'breakdown of 903 data by ethnicity')
    
    return fig

st.title('903 header analysis tool')

upload = st.file_uploader('Please upload 903 header.csv as a .csv')

if upload:
    st.write('File successfully uploaded')

    df_upload = pd.read_csv(upload)
    df_clean = data_cleaner(df_upload)

    age_bar_fig = age_bar(df_clean)
    st.plotly_chart(age_bar_fig)

    ethnic_pie_fig = ethnicity_pie(df_clean)
    st.plotly_chart(ethnic_pie_fig)

    #st.dataframe(df_clean)

