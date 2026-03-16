# 🎬 AI Movie Recommendation System

An intelligent Movie Recommendation System built using **Machine Learning and Natural Language Processing techniques**.  
This project analyzes movie genres and recommends similar movies using **TF-IDF Vectorization** and **Cosine Similarity**.

The system is implemented both as a **Machine Learning notebook** and a **Streamlit web application**, allowing users to interact with the recommendation engine through a simple interface.

---

# 🚀 Features

✔ AI-based movie recommendation engine  
✔ Smart movie search functionality  
✔ Content-based filtering algorithm  
✔ TF-IDF feature extraction from genres  
✔ Cosine similarity ranking system  
✔ Interactive Streamlit web application  
✔ Dataset visualization and analysis  

---

# 🧠 How the AI Works

The recommendation engine follows these steps:

1. Load the MovieLens dataset
2. Extract genre information from each movie
3. Convert genres into numerical vectors using **TF-IDF**
4. Compute similarity between movies using **Cosine Similarity**
5. Rank movies based on similarity score
6. Recommend the **most similar movies**

This approach is known as **Content-Based Recommendation Systems**, commonly used in platforms like **Netflix and Amazon**.

---

# 📊 Dataset

Dataset used: **MovieLens Latest Small Dataset**

Dataset details:

Total Movies: **9742**

Columns used:

movieId  
title  
genres  

Dataset source:

https://grouplens.org/datasets/movielens/

---

# 🔍 Movie Search Feature

Users can search movies even without typing the exact title.

Example:

search_movie("toy")

Output:

Toy Story (1995)  
Toy Story 2 (1999)  
Toy Story 3 (2010)

---

# 🎥 Movie Recommendation Example

Input:

recommend_movies("Toy Story (1995)")

Output:

Toy Story 2 (1999)  
A Bug's Life (1998)  
Monsters Inc. (2001)  
Aladdin (1992)  
The Lion King (1994)

The AI recommends movies with **similar genre characteristics**.

---

# 🌐 Web Application

This project also includes a **Streamlit web interface** where users can enter a movie name and receive recommendations instantly.

Example interface:

🎬 AI Movie Recommendation System  
Enter a movie name → Toy Story  

Recommended Movies:

Toy Story 2  
A Bug's Life  
Monsters Inc  
Shrek  
Finding Nemo  

---

# 📈 Dataset Visualization

The project also analyzes the dataset to visualize the **most common movie genres**.

![Genre Distribution](genre_distribution.png)

---

# 📁 Project Structure

movie-recommendation-system

movies.csv  
ratings.csv  
recommendation_model.ipynb  
app.py  
genre_distribution.png  
recommendation_chart.png  
requirements.txt  
README.md  

---

# ⚙️ Technologies Used

Python  
Pandas  
NumPy  
Scikit-Learn  
Matplotlib  
Streamlit  
Jupyter Notebook  

---

# 🛠 Installation

Clone the repository

git clone https://github.com/henil-modi/movie-recommendation-system.git

Navigate to project folder

cd movie-recommendation-system

Install required libraries

pip install -r requirements.txt

---

# ▶ Run the Web Application

Start the Streamlit app:

streamlit run app.py

The application will open automatically in your browser.

---

# 💡 Future Improvements

Hybrid recommendation system  
User rating-based recommendations  
Deep learning recommendation models  
Integration with movie APIs  
Advanced UI improvements  

---

# 👨‍💻 Author

Henil Modi  

