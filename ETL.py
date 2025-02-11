import json
import csv

def write_to_file(filename, data, headers):
    """Helper function to write data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

def process_large_json(json_file):
    """Processes a large JSON file and writes the structured data into multiple text files."""
    orchestras = set()
    programs = []
    concerts = []
    works = []
    persons = set()
    soloist_work_person = []
    
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
        for program in data.get("programs", []):
            orchestra_id = program["orchestra"].replace(" ", "_").lower()
            orchestras.add((orchestra_id, program["orchestra"]))
            
            program_id = program["programID"]
            programs.append((program_id, program["season"], orchestra_id))
            
            for concert in program.get("concerts", []):
                concert_id = f"{program_id}_{concert['Date']}"
                concerts.append((concert_id, concert['eventType'], concert['Date'], concert['Venue'], concert['Location'], concert['Time'], program_id))
            
            for work in program.get("works", []):
                work_id = work["ID"]
                works.append((work_id, work.get("workTitle", ""), work.get("composerName", ""), work.get("conductorName", ""), concert_id))
                
                for soloist in work.get("soloists", []):
                    soloist_id = soloist["soloistName"].replace(" ", "_").lower()
                    persons.add((soloist_id, soloist["soloistName"]))
                    soloist_work_person.append((soloist_id, work_id))
    
    # Write to files
    write_to_file("orchestra.txt", orchestras, ["orchestraID", "orchestraName"])
    write_to_file("program.txt", programs, ["programID", "season", "orchestraID"])
    write_to_file("concert.txt", concerts, ["concertID", "eventType", "date", "venue", "location", "time", "programID"])
    write_to_file("works.txt", works, ["workID", "workTitle", "composerName", "conductorID", "concertID"])
    write_to_file("person.txt", persons, ["personID", "name"])
    write_to_file("soloist_work_person.txt", soloist_work_person, ["soloistID", "workID"])
    
    print("Data processing complete. Files generated successfully.")

# Example usage:
json_file_path = "D:\\ITI\\bosta-casestudy\\casestudy\\src\\raw_nyc_phil.json"
process_large_json(json_file_path)