# Project 3 — MovieMatch Recommendation System 🎬

## Overview

MovieMatch is a Python-based movie recommendation system developed as part of my DecodeLabs Artificial Intelligence Internship.

The system recommends movies based on two user preferences:

- Preferred Genre
- Preferred Mood

It uses a simple weighted matching approach to calculate a recommendation score for each movie and then displays the top 5 matching movies.

## How It Works

The system contains a dataset of 30 selected Hollywood movies.

Each movie has:

- Title
- Genre
- Mood
- Release Year

The user first selects a genre and then selects a mood.

The system then compares these preferences with every movie in the dataset.

### Recommendation Scoring

Genre matching has a higher weight than mood matching.

- Genre match = **75 points**
- Mood match = **25 points**

Therefore, a movie matching both the selected genre and mood can receive a maximum score of:

**100%**

The movies are then sorted according to their match score and the top 5 recommendations are displayed.

## Example

If the user selects:

**Genre:** Science Fiction  
**Mood:** Mind-bending

The system checks all 30 movies and calculates their scores.

For example:

- Interstellar → Genre + Mood match → **100%**
- The Matrix → Genre match → **75%**
- Arrival → Genre match → **75%**

The system then ranks the movies and displays the top 5 recommendations.

## Features

- 30-movie dataset
- 6 movie genres
- 8 different moods
- Genre-based preference matching
- Mood-based preference matching
- Weighted recommendation scoring
- Top 5 movie recommendations
- Match explanation for each recommendation
- Input validation
- Option to search for new recommendations
- Interactive console interface

## Recommendation Logic

The recommendation score is calculated using the following logic:

```text
Start with score = 0

If movie genre matches selected genre:
    Add 75 points

If movie mood matches selected mood:
    Add 25 points

Final score = Genre score + Mood score
