import json
import pandas as pd
import os
from collections import Counter

def load_json(json_file):
    """Load and parse the JSON file."""
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def explore_structure(data, depth=0, parent_key="root"):
    """Recursively explores the structure of the JSON data."""
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{'  ' * depth}{parent_key} -> {key} ({type(value).__name__})")
            explore_structure(value, depth + 1, key)
    elif isinstance(data, list) and len(data) > 0:
        print(f"{'  ' * depth}{parent_key} -> List[{type(data[0]).__name__}] (Length: {len(data)})")
        explore_structure(data[0], depth + 1, parent_key + "[]")
    else:
        print(f"{'  ' * depth}{parent_key} -> {type(data).__name__}")

def analyze_programs(programs):
    """Performs data analysis on the programs."""
    print("\nAnalyzing Programs...")
    df = pd.DataFrame(programs)
    print("Columns:", df.columns.tolist())
    print("Missing Values:\n", df.isnull().sum())
    print("Unique Orchestras:", df['orchestra'].nunique())
    print("Unique Seasons:", df['season'].nunique())

def analyze_concerts(programs):
    """Analyzes concert-related data."""
    print("\nAnalyzing Concerts...")
    concerts = [concert for program in programs for concert in program.get("concerts", [])]
    df = pd.DataFrame(concerts)
    print("Columns:", df.columns.tolist())
    print("Missing Values:\n", df.isnull().sum())
    print("Unique Venues:", df['Venue'].nunique())
    print("Unique Locations:", df['Location'].nunique())

def analyze_works(programs):
    """Analyzes musical works."""
    print("\nAnalyzing Works...")
    works = [work for program in programs for work in program.get("works", [])]
    df = pd.DataFrame(works)
    print("Columns:", df.columns.tolist())
    print("Missing Values:\n", df.isnull().sum())
    print("Unique Composers:", df['composerName'].nunique())
    print("Unique Conductors:", df['conductorName'].nunique())

def analyze_soloists(programs):
    """Analyzes soloists in works."""
    print("\nAnalyzing Soloists...")
    soloists = [soloist for program in programs for work in program.get("works", []) for soloist in work.get("soloists", [])]
    df = pd.DataFrame(soloists)
    print("Columns:", df.columns.tolist())
    print("Missing Values:\n", df.isnull().sum())
    print("Unique Soloist Names:", df['soloistName'].nunique())
    print("Unique Instruments:", df['soloistInstrument'].nunique())

json_file_path = "D:\\ITI\\bosta-casestudy\\casestudy\\src\\raw_nyc_phil.json"
data = load_json(json_file_path)
    
print("\nExploring JSON Structure:\n")

explore_structure(data)
    
programs = data.get("programs", [])
analyze_programs(programs)
analyze_concerts(programs)
analyze_works(programs)
analyze_soloists(programs)






"""
# Print the structure of the data
print("=== Structure of the Data ===")
print(json.dumps(data_sample, indent=4))
print("\n")

# Extract top-level keys
print("=== Top-Level Keys ===")
print(list(data_sample.keys()))
print("\n")

# Extract nested keys in 'concerts'
print("=== Nested Keys in 'concerts' ===")
print(list(data_sample['concerts'][0].keys()))
print("\n")

# Extract nested keys in 'works'
print("=== Nested Keys in 'works' ===")
print(list(data_sample['works'][0].keys()))
print("\n")

# Extract nested keys in 'soloists'
print("=== Nested Keys in 'soloists' ===")
if data_sample['works'][0]['soloists']:
    print(list(data_sample['works'][0]['soloists'][0].keys()))
else:
    print("No soloists in this work.")
print("\n")

# Parse nested dictionaries and lists
print("=== Parsing Nested Dictionaries and Lists ===")

# Example: Extract all soloist names and their instruments
soloists_data = []
for work in data_sample['works']:
    if work['soloists']:
        for soloist in work['soloists']:
            soloists_data.append({
                'workTitle': work['workTitle'],
                'soloistName': soloist['soloistName'],
                'soloistInstrument': soloist['soloistInstrument'],
                'soloistRoles': soloist['soloistRoles']
            })

# Convert to DataFrame for better visualization
soloists_df = pd.DataFrame(soloists_data)
print("Soloists Data:")
print(soloists_df)
print("\n")

# Example: Extract all works with their composers and conductors
works_data = []
for work in data_sample['works']:
    works_data.append({
        'workTitle': work['workTitle'],
        'composerName': work['composerName'],
        'conductorName': work['conductorName']
    })

# Convert to DataFrame for better visualization
works_df = pd.DataFrame(works_data)
print("Works Data:")
print(works_df)
print("\n")

# Example: Extract concert details
concerts_data = []
for concert in data_sample['concerts']:
    concerts_data.append({
        'Date': concert['Date'],
        'eventType': concert['eventType'],
        'Venue': concert['Venue'],
        'Location': concert['Location'],
        'Time': concert['Time']
    })

# Convert to DataFrame for better visualization
concerts_df = pd.DataFrame(concerts_data)
print("Concerts Data:")
print(concerts_df)
print("\n")

# Example: Count the number of works per composer
composer_counts = Counter(work['composerName'] for work in data_sample['works'])
print("Number of Works per Composer:")
print(composer_counts)
print("\n")

# Example: Count the number of works per conductor
conductor_counts = Counter(work['conductorName'] for work in data_sample['works'])
print("Number of Works per Conductor:")
print(conductor_counts)
print("\n")
"""