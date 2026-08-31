# Project 3 — AI Movie Recommendation System 🎬

## Overview

This project was developed as part of my DecodeLabs Artificial Intelligence Internship.

The project is a simple movie recommendation system called **MovieMatch**. It recommends movies based on the user's preferred genre and mood.

The system uses a scoring-based approach where genre is given more importance than mood.

## How It Works

The user selects:

- A preferred movie genre
- A preferred mood

The system then compares these preferences with a dataset of 30 selected Hollywood movies.

Each movie receives a match score:

- Genre match = 75 points
- Mood match = 25 points

The movies are then sorted according to their scores and the top 5 recommendations are displayed.

## Recommendation Workflow

```text
User selects Genre
        ↓
User selects Mood
        ↓
Compare preferences with movies
        ↓
Calculate Match Score
        ↓
Sort Movies
        ↓
Display Top 5 Recommendations
```
## Features
-> 30 selected Hollywood movies
-> 6 movie genres
-> 8 different moods
-> Genre and mood based recommendations
-> Match score calculation
-> Top 5 recommendations
-> Explanation for each recommendation
-> Option to search again
-> Input validation
-> Technologies Used
-> Python
-> Python Concepts Used
-> Lists
-> Dictionaries
-> Functions
-> Loops
-> Conditional statements
-> User input
-> Sorting
-> Lambda functions
-> Basic data processing

## What I Learned

This project helped me understand how recommendation systems can be built using simple logic and scoring techniques.

I learned how to represent structured movie data using dictionaries and lists, compare user preferences with dataset attributes, calculate scores, sort results, and present personalized recommendations.

This project also helped me understand the basic idea behind recommendation systems before moving towards more advanced machine learning approaches.

## Project Files
recommendation_system.py — Main recommendation system
1.png to 5.png — Project screenshots

## Internship
DecodeLabs Artificial Intelligence Internship — Project 3
