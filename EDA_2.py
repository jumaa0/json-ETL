import json
import pandas as pd
from collections import Counter

# Load the data sample

def load_json(json_file):
    """Load and parse the JSON file."""
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
json_file_path = "./src/raw_nyc_phil.json"
data_sample = load_json(json_file_path)


# Print the structure of the data
print("=== Structure of the Data ===")
print(json.dumps(data_sample, indent=4))
print("\n")

# Extract top-level keys
print("=== Top-Level Keys ===")
print(list(data_sample.keys()))
print("\n")

# Explore the number of programs
print("=== Number of Programs ===")
print(len(data_sample["programs"]))
print("\n")

# Explore the structure of the first program
first_program = data_sample["programs"][0]
print("=== Keys in a Program ===")
print(list(first_program.keys()))
print("\n")

# Explore the number of concerts in the first program
print("=== Number of Concerts in First Program ===")
print(len(first_program["concerts"]))
print("\n")

# Explore the structure of a concert
first_concert = first_program["concerts"][0]
print("=== Keys in a Concert ===")
print(list(first_concert.keys()))
print("\n")

# Explore the number of works in the first program
print("=== Number of Works in First Program ===")
print(len(first_program["works"]))
print("\n")

# Explore the structure of a work
first_work = first_program["works"][0]
print("=== Keys in a Work ===")
print(list(first_work.keys()))
print("\n")

# Explore soloists structure in the first work
print("=== Soloists in First Work ===")
if "soloists" in first_work and first_work["soloists"]:
    print("Number of Soloists:", len(first_work["soloists"]))
    print("Keys in a Soloist Entry:", list(first_work["soloists"][0].keys()))
else:
    print("No soloists in this work.")
print("\n")

# Check unique composers
all_composers = [work['composerName'] for program in data_sample['programs'] for work in program['works'] if 'composerName' in work]
print("=== Unique Composers Count ===")
print(len(set(all_composers)))
print("\n")

# Check unique conductors
all_conductors = [work['conductorName'] for program in data_sample['programs'] for work in program['works'] if 'conductorName' in work]
print("=== Unique Conductors Count ===")
print(len(set(all_conductors)))
print("\n")