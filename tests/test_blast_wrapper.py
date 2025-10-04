# Objective: Test that blast_wrapper.py runs and results are saved in database

import os
import sqlite3
import subprocess

def test_blast_wrapper():
    # Step 1: Remove old database if exists
    if os.path.exists("blast_results.db"):
        os.remove("blast_results.db")

    # Step 2: Run blast_wrapper.py
    subprocess.run(["python", "blast_wrapper.py"], check=True)

    # Step 3: Connect to database and check results
    conn = sqlite3.connect("blast_results.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM blast_results")
    count = cursor.fetchone()[0]

    assert count > 0, "❌ No BLAST results found in database!"

    conn.close()
    print("✅ Test passed: BLAST ran and results saved successfully.")

if __name__ == "__main__":
    test_blast_wrapper()
