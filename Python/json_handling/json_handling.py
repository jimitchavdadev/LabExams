import os
import json
from collections import defaultdict

def read_covid_data(directory):
    """Read all JSON files from the specified directory and its subdirectories."""
    covid_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    covid_data.append(json.load(f))
    return covid_data

def calculate_statistics(covid_data):
    """Calculate total confirmed cases, deaths, recovered cases, and active cases for each country."""
    stats = defaultdict(lambda: {'confirmed_cases': 0, 'deaths': 0, 'recovered': 0})

    for record in covid_data:
        country = record['country']
        stats[country]['confirmed_cases'] += record['confirmed_cases']['total']
        stats[country]['deaths'] += record['deaths']['total']
        stats[country]['recovered'] += record['recovered']['total']

    # Calculate active cases
    for country, data in stats.items():
        data['active_cases'] = data['confirmed_cases'] - (data['deaths'] + data['recovered'])

    return stats

def main():
    # Step 1: Read COVID-19 data
    covid_directory = 'covid_data'  # Specify the directory containing JSON files
    covid_data = read_covid_data(covid_directory)

    # Step 2: Calculate statistics
    country_stats = calculate_statistics(covid_data)

    # Step 3: Determine top 5 countries with highest and lowest confirmed cases
    sorted_countries = sorted(country_stats.items(), key=lambda x: x[1]['confirmed_cases'])
    top_5_highest = sorted_countries[-5:]  # Last 5 items are the highest
    top_5_lowest = sorted_countries[:5]     # First 5 items are the lowest

    print("\nTop 5 Countries with Highest Confirmed Cases:")
    for country, data in top_5_highest:
        print(f"{country}: {data['confirmed_cases']} confirmed cases")

    print("\nTop 5 Countries with Lowest Confirmed Cases:")
    for country, data in top_5_lowest:
        print(f"{country}: {data['confirmed_cases']} confirmed cases")

    # Step 4: Generate a summary report in JSON format
    summary_report = {country: data for country, data in country_stats.items()}
    
    with open('covid19_summary.json', 'w') as json_file:
        json.dump(summary_report, json_file, indent=4)

    print("\nSummary report has been saved to 'covid19_summary.json'.")

if __name__ == "__main__":
    main()