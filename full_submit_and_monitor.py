#!/bin/bash

PYTHON_ETL_SCRIPT="ETL.py"
PYTHON_DB_SCRIPT="insert_to_db.py"
JSON_FILE="./src/raw_nyc_phil.json"
OUTPUT_FILES=("./trg/orchestra.txt" "./trg/program.txt" "./trg/concert.txt" "./trg/works.txt" "./trg/person.txt" "./trg/soloist_work_person.txt")
TRG_DIR="./trg"
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
    echo "Attempt $attempt: Running the ETL Python script..."
    python3 "$PYTHON_ETL_SCRIPT"

    if check_output_files; then
        echo "ETL Job completed successfully. All files are created."
        
        echo "Running database insertion script..."
        python3 "$PYTHON_DB_SCRIPT"

        if [[ $? -eq 0 ]]; then
            echo "Database insertion completed successfully."

            if [ -d "$TRG_DIR" ]; then
                rm -rf "$TRG_DIR"
                echo "Deleted $TRG_DIR and its contents."
            else
                echo "$TRG_DIR not found. Skipping deletion."
            fi
            
            echo "Job finished successfully."
            exit 0
        else
            echo "Database insertion failed. Retrying..."
        fi
    else
        echo "ETL Job failed. Some files are missing."
    fi

    if (( attempt < MAX_RETRIES )); then
        echo "Retrying in $RETRY_DELAY seconds..."
        sleep $RETRY_DELAY
    fi

    ((attempt++))
done

echo "Job failed after $MAX_RETRIES attempts. Please check the script."
exit 1
