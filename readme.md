


# **NYC Philharmonic ETL Pipeline**  
##### Developed as part of a Bosta-casestudy project.

---
## **Overview**  
This project processes a large JSON dataset from the NYC Philharmonic archive, extracts meaningful information, and transforms it into structured text files. The processed data is then inserted into a MySQL database. The entire process is managed by a monitoring script that ensures reliability and retries if needed.  

## **Project Structure**  

```
📂 bosta-casestudy  
│── 📂 src  
│   └── raw_nyc_phil.json  # The raw JSON dataset  
│── 📂 trg  
│   ├── orchestra.txt  
│   ├── program.txt  
│   ├── concert.txt  
│   ├── works.txt  
│   ├── person.txt  
│   ├── soloist_work_person.txt  
│── ETL.py  # Extracts, transforms, and saves data into text files  
│── insert_to_db.py  # Reads text files and inserts data into MySQL  
│── monitor_job.sh  # Monitors and retries the job if needed  
│── README.md  # Project documentation  
```

---

## **How It Works**  

1. **Extract & Transform:**  
   - `ETL.py` reads `raw_nyc_phil.json`, extracts key information, and saves it into multiple text files in `./trg`.  
   - The extracted tables include orchestras, programs, concerts, works, and soloists.  

2. **Monitoring & Execution:**  
   - The `monitor_job.sh` script runs `ETL.py`, checks if all output files are created, and retries up to 3 times if necessary.  
   - If all files are successfully created, `insert_to_db.py` inserts the data into a MySQL database (optional).  
   - After successful execution, `./trg` is deleted if MySQL is set up.  

---

## **How to Run**  

### **Step 1: Run the Monitoring Script**  

Simply execute:  

```bash
bash monitor_job.sh
```

This script will:  
✅ Run the ETL process.  
✅ Retry on failure (up to 3 times).  
✅ Insert data into MySQL (if installed).  
✅ Clean up the `./trg` directory after successful execution.  

### **Step 2: Verify the Output**  

Check the extracted data in the `./trg` directory before it is deleted:  

```bash
ls -l ./trg
```

Each `.txt` file contains structured data extracted from the JSON file.  

---

## **Database Integration (Optional)**  

If MySQL is installed, `insert_to_db.py` will insert the extracted data into a database. Ensure:  
- MySQL is running.  
- A database is created.  
- Database credentials are configured in `insert_to_db.py`.  

After execution, the `./trg` directory will be deleted.  

---

## **Customization**  

- To modify the JSON processing logic, update `ETL.py`.  
- To change database configurations, edit `insert_to_db.py`.  
- To adjust retry logic, modify `monitor_job.sh`.  

---

## **Troubleshooting**  

| **Issue**                | **Solution**                              |  
|--------------------------|------------------------------------------|  
| Missing output files     | Ensure `ETL.py` runs properly            |  
| Script fails after retries | Check error messages in `monitor_job.sh` |  
| MySQL insertion issues  | Verify database connection & schema       |  

---
## **Data Structure**  

The JSON file contains details about NYC Philharmonic concerts, including orchestras, concerts, works performed, and soloists.  

### **Sample Record**  

```json
{
    "season": "1842-43",
    "orchestra": "New York Philharmonic",
    "concerts": [
        {
            "Date": "1842-12-07T05:00:00Z",
            "eventType": "Subscription Season",
            "Venue": "Apollo Rooms",
            "Location": "Manhattan, NY",
            "Time": "8:00PM"
        }
    ],
    "programID": "3853",
    "works": [
        {
            "workTitle": "SYMPHONY NO. 5 IN C MINOR, OP.67",
            "composerName": "Beethoven, Ludwig van",
            "conductorName": "Hill, Ureli Corelli",
            "ID": "52446*",
            "soloists": []
        },
        {
            "workTitle": "OBERON",
            "composerName": "Weber, Carl Maria Von",
            "conductorName": "Timm, Henry C.",
            "ID": "8834*4",
            "soloists": [
                {
                    "soloistName": "Otto, Antoinette",
                    "soloistRoles": "S",
                    "soloistInstrument": "Soprano"
                }
            ],
            "movement": "\"Ozean, du Ungeheuer\" (Ocean, thou mighty monster), Reiza (Scene and Aria), Act II"
        }
    ],
    "id": "38e072a7-8fc9-4f9a-8eac-3957905c0002"
}
```

### **Key Data Points**  

- `season`: The concert season.  
- `orchestra`: The orchestra name.  
- `concerts`: An array containing concert details like date, venue, location, and time.  
- `programID`: A unique ID for the program.  
- `works`: An array of musical pieces performed, with details about composers, conductors, and soloists.  
- `id`: A unique identifier for each record.  

---

## **feedback**  
Developed as part of a Bosta-casestudy project. feedback are welcome!  

---
