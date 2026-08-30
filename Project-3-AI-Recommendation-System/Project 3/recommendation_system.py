import time

# Width used to center the console headings.
SCREEN_WIDTH = 68

# This program recommends only from 30 selected Hollywood movies.
MOVIES = [
    # Action movies
    {
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "mood": "intense",
        "year": 2015
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "mood": "dark",
        "year": 2008
    },
    {
        "title": "John Wick",
        "genre": "Action",
        "mood": "intense",
        "year": 2014
    },
    {
        "title": "Mission: Impossible - Fallout",
        "genre": "Action",
        "mood": "adventurous",
        "year": 2018
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "genre": "Action",
        "mood": "uplifting",
        "year": 2018
    },

    # Comedy movies
    {
        "title": "The Grand Budapest Hotel",
        "genre": "Comedy",
        "mood": "funny",
        "year": 2014
    },
    {
        "title": "The Nice Guys",
        "genre": "Comedy",
        "mood": "funny",
        "year": 2016
    },
    {
        "title": "Paddington 2",
        "genre": "Comedy",
        "mood": "uplifting",
        "year": 2017
    },
    {
        "title": "The Intern",
        "genre": "Comedy",
        "mood": "inspiring",
        "year": 2015
    },
    {
        "title": "Knives Out",
        "genre": "Comedy",
        "mood": "mind-bending",
        "year": 2019
    },

    # Drama movies
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "mood": "inspiring",
        "year": 1994
    },
    {
        "title": "Parasite",
        "genre": "Drama",
        "mood": "dark",
        "year": 2019
    },
    {
        "title": "Whiplash",
        "genre": "Drama",
        "mood": "intense",
        "year": 2014
    },
    {
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "mood": "emotional",
        "year": 2006
    },
    {
        "title": "Little Women",
        "genre": "Drama",
        "mood": "uplifting",
        "year": 2019
    },

    # Horror movies
    {
        "title": "Get Out",
        "genre": "Horror",
        "mood": "mind-bending",
        "year": 2017
    },
    {
        "title": "A Quiet Place",
        "genre": "Horror",
        "mood": "intense",
        "year": 2018
    },
    {
        "title": "The Conjuring",
        "genre": "Horror",
        "mood": "dark",
        "year": 2013
    },
    {
        "title": "Hereditary",
        "genre": "Horror",
        "mood": "emotional",
        "year": 2018
    },
    {
        "title": "Train to Busan",
        "genre": "Horror",
        "mood": "adventurous",
        "year": 2016
    },

    # Romance movies
    {
        "title": "Pride and Prejudice",
        "genre": "Romance",
        "mood": "emotional",
        "year": 2005
    },
    {
        "title": "La La Land",
        "genre": "Romance",
        "mood": "uplifting",
        "year": 2016
    },
    {
        "title": "About Time",
        "genre": "Romance",
        "mood": "funny",
        "year": 2013
    },
    {
        "title": "Before Sunrise",
        "genre": "Romance",
        "mood": "emotional",
        "year": 1995
    },
    {
        "title": "The Big Sick",
        "genre": "Romance",
        "mood": "funny",
        "year": 2017
    },

    # Science Fiction movies
    {
        "title": "Interstellar",
        "genre": "Science Fiction",
        "mood": "mind-bending",
        "year": 2014
    },
    {
        "title": "Arrival",
        "genre": "Science Fiction",
        "mood": "emotional",
        "year": 2016
    },
    {
        "title": "The Matrix",
        "genre": "Science Fiction",
        "mood": "intense",
        "year": 1999
    },
    {
        "title": "Blade Runner 2049",
        "genre": "Science Fiction",
        "mood": "dark",
        "year": 2017
    },
    {
        "title": "Everything Everywhere All at Once",
        "genre": "Science Fiction",
        "mood": "funny",
        "year": 2022
    }
]

GENRES = [
    "Action",
    "Comedy",
    "Drama",
    "Horror",
    "Romance",
    "Science Fiction"
]

MOODS = [
    "adventurous",
    "dark",
    "emotional",
    "funny",
    "inspiring",
    "intense",
    "mind-bending",
    "uplifting"
]


def show_welcome_message():
    print("=" * SCREEN_WIDTH)
    print("WELCOME TO MOVIEMATCH".center(SCREEN_WIDTH))
    print("Hollywood Movie Recommendation System".center(SCREEN_WIDTH))
    print("30 Selected Movies | 6 Genres".center(SCREEN_WIDTH))
    print("=" * SCREEN_WIDTH)


def choose_genre():
    print("\nAvailable Genres:")

    for number, genre in enumerate(GENRES, start=1):
        print(f"{number}. {genre}")

    choice = input("\nEnter your preferred genre number: ").strip()

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(GENRES):
            return GENRES[choice - 1]

    return None


def choose_mood():
    print("\nAvailable Moods:")

    for number, mood in enumerate(MOODS, start=1):
        print(f"{number}. {mood}")

    choice = input("\nEnter your preferred mood number: ").strip()

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(MOODS):
            return MOODS[choice - 1]

    return None


# Genre has more importance than mood in the recommendation score.
def calculate_match_score(movie, selected_genre, selected_mood):
    score = 0

    if movie["genre"] == selected_genre:
        score += 75

    if movie["mood"] == selected_mood:
        score += 25

    return score


def get_recommendations(selected_genre, selected_mood):
    recommendations = []

    for movie in MOVIES:
        score = calculate_match_score(
            movie,
            selected_genre,
            selected_mood
        )

        movie_result = {
            "movie": movie,
            "score": score
        }

        recommendations.append(movie_result)

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations[:5]


def get_reason(movie, selected_genre, selected_mood):
    genre_matches = movie["genre"] == selected_genre
    mood_matches = movie["mood"] == selected_mood

    if genre_matches and mood_matches:
        return "Matches both your selected genre and mood."

    if genre_matches:
        return "Matches your selected genre."

    if mood_matches:
        return "Matches your selected mood."

    return "Included as a lower-ranked movie from the dataset."


def show_recommendations(recommendations, selected_genre, selected_mood):
    print("\n" + "=" * SCREEN_WIDTH)
    print("YOUR TOP 5 MOVIE RECOMMENDATIONS".center(SCREEN_WIDTH))
    print("=" * SCREEN_WIDTH)

    for number, item in enumerate(recommendations, start=1):
        movie = item["movie"]
        score = item["score"]
        reason = get_reason(movie, selected_genre, selected_mood)

        print(f"\n{number}. {movie['title']} ({movie['year']})")
        print(f"   Genre: {movie['genre']}")
        print(f"   Mood: {movie['mood'].title()}")
        print(f"   Match Score: {score}%")
        print(f"   Reason: {reason}")

        # Pause between results for a smoother user experience.
        if number < len(recommendations):
            time.sleep(0.8)


def search_again():
    while True:
        choice = input(
            "\nWould you like to search for new movies? (yes/no): "
        ).strip().lower()

        if choice == "yes" or choice == "y":
            return True

        if choice == "no" or choice == "n":
            return False

        print("Please enter yes or no.")


def main():
    show_welcome_message()

    while True:
        selected_genre = choose_genre()

        if selected_genre is None:
            print("\nInvalid genre selection. Please try again.")
            continue

        selected_mood = choose_mood()

        if selected_mood is None:
            print("\nInvalid mood selection. Please try again.")
            continue

        print("\nAnalysing your preferences...")
        time.sleep(0.8)

        recommendations = get_recommendations(
            selected_genre,
            selected_mood
        )

        show_recommendations(
            recommendations,
            selected_genre,
            selected_mood
        )

        if not search_again():
            break

    print("\n" + "=" * SCREEN_WIDTH)
    print("Thank you for using MovieMatch!".center(SCREEN_WIDTH))
    print("=" * SCREEN_WIDTH)


if __name__ == "__main__":
    main()