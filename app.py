import streamlit as st
import pandas as pd
import pickle
import pandas._libs.internals
import requests
with open('movies_dict_pkl','rb') as f:
     movie_list=pickle.load(f)
with open('open.pkl','rb') as k:
     details=pickle.load(k)
with open('similarity.pkl','rb') as g:
     similarity=pickle.load(g)

movie_data=pd.DataFrame(movie_list)
# similarity=pickle.load(open('similarity.pkl','rb'))
# details=pickle.load(open('open.pkl','rb'))
# pandas._libs.internals._unpickle_block = lambda x: x





def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recomendation(movie):
    movie_index=movie_data[movie_data['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movie_names = []
    recommended_movie_posters = []
    dir=[]
    cast=[]
    genres=[]
    overview=[]
    for i in movie_list:
        movie_id = movie_data.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movie_data.iloc[i[0]].title)
        dir.append(details['director'].iloc[i[0]])
        cast.append(details['cast'].iloc[i[0]])
        genres.append(details['genres'].iloc[i[0]])
        overview.append(details['overview'].iloc[i[0]])


    
    

    return recommended_movie_names,recommended_movie_posters,dir,cast, genres,overview


st.title('Movie Recomendation system')


selected_movie_name = st.selectbox("movie list",movie_data['title'].values)

st.write("You selected:", selected_movie_name )


# st.button("Recommend")
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters,dir = recomendation(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
        


#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#         st.text(dir[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#         st.text(dir[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#         st.text(dir[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#         st.text(dir[4])




if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,dir,cast,genres,overview = recomendation(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    for movie in recommended_movie_names:
        
            st.header(movie)
            st.image(recommended_movie_posters[recommended_movie_names.index(movie)])
            st.write(overview[recommended_movie_names.index(movie)])
            st.write("Director",dir[recommended_movie_names.index(movie)])
            st.write("Cast",cast[recommended_movie_names.index(movie)])
            st.write("Genres",genres[recommended_movie_names.index(movie)])
            st.divider()
        
        
        



        
