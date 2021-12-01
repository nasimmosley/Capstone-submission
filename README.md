## SARIMA Time Series: Modeling to Predict Baby Name Popularity


#### EXECUTIVE SUMMARY
The baby name popularity predictor project was borne of the anxiety of soon-to-be-parents in making the first decision of countless in the lives of their children.  The project sought to use time series modeling to predict the future popularity of a specific name, based on data acquired from the US Social Security Administration.  The dataset was procured from dataworld.com and is linked below in the data sources section.  The data includes information for registered names from 1880 to 2020 of at least five counts per year.  The goal of the project was to produce a time series model that would accurately predict the trend line of popularity (in count of name) for popular names through 2036.  The final model selected was a SARIMA model that had a lower mean absolute error than the baseline projection of last known count in roughly 50 percent of the sample set.  The model accurately predicted changes in trend patterns using a test size of 30 percent (depending on when the name first showed in the dataset) for the most popular names--defined as male names that had more than 993 mentions in one year for at least 10 years and female names that had at least 825 mentions in one year for at least 10 years from 1920 to 2020.


A scrub of the data revealed that the model struggled to accurately predict dramatic changes in trends in the test sample--for example, the name "Theodore" saw a dramatic upward trend circa 2020, reversing decades of continuous slow trend downward.  The SARIMA model was unable to capture the change as it never saw any indication that the pattern would shift.  This illuminates the significant hazard of trying to use models to predict the popularity of baby names with no other exogenous information.  The popularity of baby names is notoriously fickle--just as one name dramatically rises in popularity, in just a few years--the name reaches its zenith and usually begins a downward trajectory.  No clear singular reason is apparent for a name's popularity--beloved television characters may catapult a formerly unpopular name, or likewise a hit song or book character may capture the zeitgeist.  

Recommendations for further analysis would be to 

#### TABLE OF CONTENTS
[Data Sources](#data-sources)<br>
[Data Dictionary](#data-dictionary)<br>
[Other Sources](#sources)<br>

#### 1. DATA SOURCES

This project used the following dataset:<br>
<a href = "https://data.world/nkrishnaswami/us-ssa-baby-names-national"> [Original SSA (National) Names Dataset]</a><br>

The jupyter notebook used to clean the data can be accessed via the link below<br>
<a href = "https://git.generalassemb.ly/nasimmosley/brandnewsubmissions/blob/master/Projects/Final%20Capstone%20Baby%20Names/2.%20Cleaning.ipynb">     [Cleaning Code]</a><br>

The jupyter notebook used to preprocess the data and conduct EDA can be accessed via the link below<br>
<a href = "https://git.generalassemb.ly/nasimmosley/brandnewsubmissions/blob/master/Projects/Final%20Capstone%20Baby%20Names/3.%20EDA.ipynb">[EDA and Preprocessing]</a><br>

The notebooks used to conduct modeling and forecasting can be accessed via the link below<br>
<a href= "https://git.generalassemb.ly/nasimmosley/brandnewsubmissions/tree/master/Projects/Final%20Capstone%20Baby%20Names/4.%20Models">[Modeling and Forecasting]</a><br>

The final pickled datasets with forecasted predictions can be accessed via the link below<br>
<a href = "https://git.generalassemb.ly/nasimmosley/brandnewsubmissions/tree/master/Projects/Final%20Capstone%20Baby%20Names/5.%20Final%20Data">[Final_data_pickled]</a><br>

The streamlit file used for the baby prediction app can be accessed via the link below<br>
[Streamlit Baby App](finalbabyapp.py)

**************************************************************************************************************
#### DATA DICTIONARY

*The final dataset uses the following data dictionary:*


(NEED TO FILL THIS IN)


### CONCLUSIONS AND RECOMMENDATIONS# Capstone
# Baby-Capstone
