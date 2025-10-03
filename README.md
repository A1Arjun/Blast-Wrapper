BLAST Wrapper Project
Objective

This project reads a DNA or protein sequence from a FASTA file, performs an atomic BLAST search using Python (NCBI online BLAST), and saves the results in a SQLite database for easy retrieval and analysis.

Project Structure
blast_wrapper_project/
│
├── blast_wrapper.py         # Main script: runs BLAST and stores results
├── requirements.txt         # Python libraries needed
├── README.md                # Project description and instructions
├── sample_data/
│   └── query.fasta          # Sample FASTA sequence for testing
└── tests/
    └── test_blast_wrapper.py # Test script to verify functionality

Dependencies

Python 3.x
Biopython
Pandas

SQLite3 (built-in with Python)

Install dependencies with:

pip install -r requirements.txt
