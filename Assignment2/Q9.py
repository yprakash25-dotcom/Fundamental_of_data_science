def collect_movie_details() -> dict[str, dict[str, str]]:
    movies: dict[str, dict[str, str]] = {}
    print("Enter details for 3 movies")
    for idx in range(1, 4):
        title = input(f"Movie {idx} title: ").strip()
        director = input(f"Movie {idx} director: ").strip()
        year = input(f"Movie {idx} release year: ").strip()
        rating = input(f"Movie {idx} rating: ").strip()
        movies[title] = {
            "Director": director,
            "Release Year": year,
            "Rating": rating,
        }
        print()
    return movies


def display_movies(movies: dict[str, dict[str, str]]) -> None:
    print("\nMovie details:")
    for title, details in movies.items():
        print(f"Title        : {title}")
        print(f"Director     : {details['Director']}")
        print(f"Release Year : {details['Release Year']}")
        print(f"Rating       : {details['Rating']}")
        print("-" * 30)


if __name__ == "__main__":
    movies = collect_movie_details()
    display_movies(movies)
