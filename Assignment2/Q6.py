def find_country_index(countries: list[str], target: str) -> str:
    try:
        return str(countries.index(target))
    except ValueError:
        return "Not Found in List"


if __name__ == "__main__":
    print("Question 6: Country search")
    countries_input = input("Enter countries separated by commas: ").strip()
    countries = [country.strip() for country in countries_input.split(",") if country.strip()]
    if not countries:
        print("No countries provided.")
    else:
        target = input("Enter the country to search: ").strip()
        result = find_country_index(countries, target)
        print(f"Search result: {result}")
