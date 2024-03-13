import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from matplotlib.ticker import MultipleLocator
import numpy as np

def draw_plot():
    # Read data from file

    df=pd.read_csv('epa-sea-level.csv')

    # Making calculations

    years_max=df['Year'].max()
    years_pr_max=2050
    
    years=df['Year'].to_numpy()
    years_prognosis=np.linspace(years_max+1,years_pr_max,years_pr_max-years_max).astype(int)
    years_2000=np.hstack((years[years>=2000],years_prognosis))
    years_full=np.hstack((years,years_prognosis))

    res_general = st.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    res_prognosis=st.linregress(df[df['Year']>=2000]['Year'],df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])

    y_min=df['CSIRO Adjusted Sea Level'].min()-1
    y_current=df['CSIRO Adjusted Sea Level'].max()+1
    y_max=years_pr_max*res_prognosis.slope+res_prognosis.intercept+1

    # Create scatter plot
    fig,ax=plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],color='steelblue',marker=".",label='original data')

    # Create first line of best fit

    ax.plot(years_full,years_full*res_general.slope+res_general.intercept,'r', label='fitted line')
    # Create second line of best fit
    ax.plot(years_2000,years_2000*res_prognosis.slope+res_prognosis.intercept,'r--', label='fitted line (after 2000)')

    # Add labels and title
    ax.set(xlabel='Year',ylabel='Sea Level (inches)',title='Rise in Sea Level',xlim=(1875,2050), ylim=(y_min,y_max))
    ax.xaxis.set_major_locator(MultipleLocator(25))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(True, linestyle='-.')
    ax.tick_params(labelrotation=90)
    ax.legend(loc='lower right')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()