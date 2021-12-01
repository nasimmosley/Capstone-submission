import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from streamlit.elements.dataframe_selector import DataFrameSelectorMixin
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import base64


#set the layout
st.set_page_config(layout = "wide", page_title="Baby Name Predictor", page_icon=":baby:")
header = st.container()
data = st.container()
fun = st.container()
#set figsize globally
plt.rcParams["figure.figsize"] = (15, 15)

col1, col2 = st.columns(2)
image = Image.open('images/crawlingbaby.gif')

#create header
with header:

    st.markdown("<h1 style='text-align: center; color: green;'>Baby Name Popularity Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'> <i>'Tigers die and leave their skins; people die and leave their names.'</i></h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: right; color: blue;'><i> -- Japanese Proverb </i></h3>", unsafe_allow_html=True)
    st.write('\n')



#import the data
males = pd.read_pickle("5. Final Data/final_data_males.pkl", 'infer')
    
females = pd.read_pickle("5. Final Data/final_data_females.pkl", 'infer')

with data:

    col1, col2 = st.columns(2)
    with col1:
        sorted_df = males.sort_values(by="name", ascending=True)
        name_options = sorted_df["name"].unique().tolist()

        name_selected = st.multiselect("Which male names would you like to see?", name_options)
        mask_names = males["name"].isin(name_selected)
        df = males[mask_names]
        df_1920 = df["1920":"2037"]

        fig = px.line(df_1920, x=df_1920.index, y="count", color="name", title = 'Model Predictions until 2036')
        fig.add_vline(x="2021", line_width = 3, line_dash = "dash", line_color="green") 
        fig.add_vrect(x0="2021", x1="2037", annotation_text="prediction", annotation_position="bottom left",
              annotation=dict(font_size=20, font_family="Times New Roman"),
              fillcolor="green", opacity=0.25, line_width=0)
        fig.update_layout(width = 700, height=600, xaxis = dict(title = 'year', showticklabels=True))
        st.plotly_chart(fig)


        def get_info(names):
        
            my_info_list=[]
            for name in names:
                df = males[males['name']==name]
                Z=df["1920":"2037"]
                num = df['count'].max()
                t_year=df['count'].idxmax().year
                lowercase = name.lower()
                url = "https://babynames.com/name/"
                final_url = url + lowercase
                if t_year < 2021:
                    x = f'The name {name} reached its peak of {int(num)} in {t_year}.'
                else:
                    x = f'The name {name} is predicted to reach its peak of {int(num)} in {t_year}.' 
                
                my_info_list.append(x)
            return my_info_list
        
        info = get_info(name_selected)
        df=pd.DataFrame(info, columns=["More Information on Names Selected"])
        df.index = [""] *len(df)
    
        st.table(df)
        
    
        st.markdown('##')
        st.markdown('##')
       

    
        
    

st.markdown('##')
st.markdown('##')
st.markdown('##')
st.markdown('##')

with col2:
        sorted_df = females.sort_values(by="name", ascending=True)
        name_options = sorted_df["name"].unique().tolist()

        name_selected = st.multiselect("Which female names would you like to see?", name_options)
        mask_names = females["name"].isin(name_selected)
        df = females[mask_names]
        df_1920 = df["1920":"2037"]

        fig = px.line(df_1920, x=df_1920.index, y="count", color="name", title = 'Model Predictions until 2036')
        fig.add_vline(x="2021", line_width = 3, line_dash = "dash", line_color="green") 
        fig.add_vrect(x0="2021", x1="2037", annotation_text="prediction", annotation_position="bottom left",
              annotation=dict(font_size=20, font_family="Times New Roman"),
              fillcolor="green", opacity=0.25, line_width=0)
        fig.update_layout(width = 700, height=600, xaxis = dict(title = 'year', showticklabels=True))
        st.plotly_chart(fig)


        def get_info(names):
            my_info_dict ={}
            my_info_list=[]
            for name in names:
                df = females[females['name']==name]
                Z=df["1920":"2037"]
                num = df['count'].max()
                t_year=df['count'].idxmax().year
                lowercase = name.lower()
                url = "https://babynames.com/name/"
                final_url = url + lowercase
                if t_year < 2021:
                    x = f'The name {name} reached its peak of {int(num)} in {t_year}.'
                else:
                    x = f'The name {name} is predicted to reach its peak of {int(num)} in {t_year}.' 
                my_info_list.append(x)
            return my_info_list
        
        info = get_info(name_selected)
        df=pd.DataFrame(info, columns=["More Information on Names Selected"])
        df.index = [""] *len(df)
    
        st.table(df)
            

with st.sidebar:
  

    st.image(image, width=100, use_column_width=True)
    st.markdown('##')
    st.markdown('##')
   
    st.sidebar.title("About the Baby Name Popularity Predictor")
    st.sidebar.subheader("The Genesis")
    st.write("The Baby Name Popularity Predictor is a project born of the anxiety of soon-to-be parents in making the first decision of countless in the lives of their children.  For some, the anxiety can turn to frustration as they realize that their child will be one of several with the same name in their classroom and generation.  The baby name predictor is an attempt to assist parents--or just the curious--in examining the past trend of a name and its potential future popularity.")
    st.markdown('##')
    st.sidebar.subheader("The Data Source")
    st.write("The data used for this predictor comes from the U.S. Social Security Administration's database of registered names from 1880 to 2020. A link to the data is below:")
    st.markdown("""<a href="https://data.world/nkrishnaswami/us-ssa-baby-names-national">US SSA Baby Names (national) </a>""", unsafe_allow_html=True)
    st.write("The data included names that had at least 5 registered social security numbers for that year and required a gender designation at the time of registration.")
    st.sidebar.subheader("About the Model")
    st.write("The model used to predict the popularity trend of the names was a SARIMA prediction model.  The model was tested on the most popular names in the dataset--identified as male names that occurred at least 993 times in one year for at least 10 years between 1920-2020 and 825 times for female names in one year for at least 10 years between 1920 and 2020. The SARIMA model performed better on roughly 50-55 percent of the test set in accurately predicting the popularity trend. The final predictions in this app include 1224 names of the most popular names in the database.")

with fun:
    st.markdown("<h1 style='text-align: center; color: green;'>But I Want a Unique Name!</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: blue;'> Have a name you like but want to make it unique? Want to find a unique compromise for two names?</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: blue;'> Give us one or two names you are considering, and we will give you several unique combination options!</h6>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)   
    
    with col1:

        str1 = st.text_input("My choice for a name", value ="")
        str2 = st.text_input("My other choice for a name", value = "")
    
        def make_new_names(str1, str2):
            big_names_list =[]
            big_st = str1.lower() + str2.lower()
            vowels = ""
            for char in big_st:
                if char in "aeiouAEIOU":
                    vowels += char
            result_string =""
            for char in big_st:
                if char in "aeiouAEIOU":
                    result_string += vowels[-1]
                    vowels = vowels[:-1]
                else:
                    result_string += char
            big_names_list.append(result_string.capitalize())
            conson = ""
            for char in big_st:
                if char in "bcdfgjhklmnpqrstvwxyz":
                    conson += char
            con_string =""
            for char in big_st:
                if char in "bcdfgjhklmnpqrstvwxyz":
                    con_string += conson[-1]
                    conson = conson[:-1]
                else:
                    con_string += char
            big_names_list.append(con_string.capitalize())
        
            vowels_for_con = ""
            for char in big_st:
                if char in "aeiouAEIOU":
                    vowels_for_con += char
            result_of_constring =""
            for char in big_st:
                if char in "aeiouAEIOU":
                    result_of_constring += vowels_for_con[-1]
                    vowels_for_con = vowels_for_con[:-1]
                else:
                    result_of_constring += char
            conson_more = ""
            for char in result_of_constring:
                if char in "bcdfghjklmnpqrstvwxyz":
                    conson_more += char
            final_string =""
            for char in result_of_constring:
                if char in "bcdfghjklmnpqrstvwxyz":
                    final_string += conson_more[-1]
                    conson_more = conson_more[:-1]
                else:
                    final_string += char
            big_names_list.append(final_string.capitalize())
            big_st_combo = str2.lower() + str1.lower()
            vowels = ""
            for char in big_st_combo:
                if char in "aeiouAEIOU":
                    vowels += char
            result_string =""
            for char in big_st_combo:
                if char in "aeiouAEIOU":
                    result_string += vowels[-1]
                    vowels = vowels[:-1]
                else:
                    result_string += char
            big_names_list.append(result_string.capitalize())
            conson = ""
            for char in big_st_combo:
                if char in "bcdfghjklmnpqrstvwxyz":
                    conson += char
            con_string =""
            for char in big_st_combo:
                if char in "bcdfghjklmnpqrstvwxyz":
                    con_string += conson[-1]
                    conson = conson[:-1]
                else:
                    con_string += char
            big_names_list.append(con_string.capitalize())
        
            vowels_for_con = ""
            for char in big_st_combo:
                if char in "aeiouAEIOU":
                    vowels_for_con += char
            result_of_constring =""
            for char in big_st_combo:
                if char in "aeiouAEIOU":
                    result_of_constring += vowels_for_con[-1]
                    vowels_for_con = vowels_for_con[:-1]
                else:
                    result_of_constring += char
            conson_more = ""
            for char in result_of_constring:
                if char in "bcdfghjklmnpqrstvwxyz":
                    conson_more += char
            final_string =""
            for char in result_of_constring:
                if char in "bcdfghjklmnpqrstvwxyz":
                    final_string += conson_more[-1]
                    conson_more = conson_more[:-1]
                else:
                    final_string += char
            big_names_list.append(final_string.capitalize())
        
            return sorted(set(big_names_list))

        y=make_new_names(str1, str2)
        df = pd.DataFrame(y, columns=["Potential Names"])
        df.index = [""] * len(df)
    
        st.subheader("The options for a unique name with my choices are:")
        st.table(df)
  
    image2 = Image.open('images/funny-baby-reaction.gif')

    with col2:
        st.markdown('##')
        st.image(image2, width=100, use_column_width=True)
    