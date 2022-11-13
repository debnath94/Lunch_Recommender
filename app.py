import streamlit as st
import pandas as pd
import pickle
def recommend(food):
    food_index = foods[foods['Lunch'] == food].index[0]
    distances = similarity[food_index]
    foods_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_foods = []
    for i in foods_list:
        recommended_foods.append(foods.iloc[i[0]].Lunch)
        return recommended_foods

foods_pikl = pickle.load(open('food_list1.pkl', 'rb'))
foods = pd. DataFrame(foods_pikl)
similarity = pickle. load(open('food_similarity1.pkl', 'rb'))


st. title('Lunch Recommender System')
selected_Food_name = st.selectbox(
'What kind of food you like?',
foods['Lunch']. values)

if st.button('Recommended'):
    recommendations = recommend(selected_Food_name)
    for i in recommendations:
        st. write(i)









