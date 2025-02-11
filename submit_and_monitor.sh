#!/bin/bash

PYTHON_SCRIPT="ETL.py"  
JSON_FILE="./src/raw_nyc_phil.json"  
OUTPUT_FILES=("./trg/orchestra.txt" "./trg/program.txt" "./trg/concert.txt" "./trg/works.txt" "./trg/person.txt" "./trg/soloist_work_person.txt")
MAX_RETRIES=3
RETRY_DELAY=10

check_output_files() {
    for file in "${OUTPUT_FILES[@]}"; do
        if [[ ! -f "$file" ]]; then
            return 1  
        fi
    done
    return 0  
}

attempt=1
while (( attempt <= MAX_RETRIES )); do
    echo "Attempt $attempt: Running the Python script..."
    python3 "$PYTHON_SCRIPT"

    if check_output_files; then
        echo "Job completed successfully. All files are created."
        exit 0
    else
        echo "Job failed. Some files are missing."
    fi

    if (( attempt < MAX_RETRIES )); then
        echo "Retrying in $RETRY_DELAY seconds..."
        sleep $RETRY_DELAY
    fi

    ((attempt++))
done

echo "Job failed after $MAX_RETRIES attempts. Please check the script."
exit 1
