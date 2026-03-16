# 🎬 AI Movie Recommendation System

A smart movie recommendation engine built using **Machine Learning and Natural Language Processing techniques**.

This system analyzes movie genres and recommends similar movies using **TF-IDF vectorization and cosine similarity**.

Instead of random suggestions, the AI understands genre relationships and suggests the most relevant movies.

---

# 🚀 Features

✔ AI-based movie recommendations  
✔ Smart movie search system  
✔ Content-based recommendation engine  
✔ TF-IDF feature extraction  
✔ Cosine similarity scoring  
✔ Visualization of movie genres  
✔ Interactive movie recommendation interface

---

# 🧠 How the AI Works

The recommendation pipeline follows these steps:

1. Load movie dataset (MovieLens dataset)
2. Extract genre information from movies
3. Convert genres into numerical vectors using **TF-IDF**
4. Compute similarity between movies using **cosine similarity**
5. Rank movies based on similarity score
6. Recommend the most similar movies

This technique is known as **Content-Based Filtering**.

---

# 📊 Dataset

Dataset used: **MovieLens Latest Small Dataset**

Dataset contains:

Total movies: **9742**

Columns used:

movieId  
title  
genres  

Dataset source:

https://grouplens.org/datasets/movielens/

---

# 🔍 Movie Search Feature

Users can search for movies even if they don't know the exact title.

Example:

```
search_movie("toy")
```

Output:

```
Toy Story (1995)
Toy Story 2 (1999)
Toy Story 3 (2010)
```

---

# 🎥 Movie Recommendation Example

Input:

```
recommend_movies("Toy Story (1995)")
```

Output:

```
Toy Story 2 (1999)
A Bug's Life (1998)
Monsters Inc. (2001)
Aladdin (1992)
The Lion King (1994)
```

---

# 📈 Genre Distribution Visualization

The project also analyzes the dataset to find the most common movie genres.

![Genre Distribution](genre_distribution.png)

---

# 📁 Project Structure

```
movie-recommendation-system
│
├ movies.csv
├ recommendation_model.ipynb
├ genre_distribution.png
├ recommendation_chart.png
├ requirements.txt
└ README.md
```

---

# ⚙️ Technologies Used

Python  
Pandas  
NumPy  
Scikit-Learn  
Matplotlib  
Jupyter Notebook  

---

# 🛠 Installation

Clone the repository

```
git clone https://github.com/henil-modi/movie-recommendation-system.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the notebook

```
recommendation_model.ipynb
```

---

# 💡 Future Improvements

Hybrid recommendation system  
User rating-based recommendations  
Web interface using Streamlit  
Integration with movie APIs  
Deep learning recommendation models

---

# 👨‍💻 Author

Henil Modi  
