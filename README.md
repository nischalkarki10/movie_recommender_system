#  Movie Recommendation System

A content-based movie recommendation system that recommends movies based on their similarity to a selected movie.

The project uses feature-based similarity to identify movies with similar characteristics and provides an interactive Streamlit interface for generating recommendations.

---

##  Overview

Recommendation systems are widely used to help users discover relevant content from large collections of items.

This project implements a **content-based movie recommendation system** that recommends movies similar to a movie selected by the user.

Instead of relying on ratings from other users, the system determines similarity between movies based on their available content-related features.

The trained similarity matrix is used to efficiently retrieve the most similar movies, while the Streamlit application provides an interactive interface for users to explore recommendations.

---

##  Objectives

The main objectives of this project are:

- Build a content-based movie recommendation system.
- Represent movies using relevant features.
- Measure similarity between movies.
- Generate the top 5 recommendations for a selected movie.
- Develop an interactive web interface using Streamlit.
- Retrieve movie posters dynamically using the TMDb API.
- Separate model preparation from the recommendation interface.

---

##  Recommendation Approach

The system follows a content-based recommendation approach.

The general workflow is:

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Representation
      ↓
Movie Feature Vectors
      ↓
Similarity Calculation
      ↓
Similarity Matrix
      ↓
User Selects a Movie
      ↓
Find Similar Movies
      ↓
Return Top 5 Recommendations