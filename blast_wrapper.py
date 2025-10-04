# Automatic BLAST Wrapper: Reads FASTA, runs BLAST, saves results in SQLite

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import sqlite3

# --------- 1. Load query sequence ---------
fasta_file = "sample_data.fasta"  # Path to your FASTA file
record = SeqIO.read(fasta_file, "fasta")
sequence_id = record.id
sequence = str(record.seq)

# --------- 2. Connect / Create database ---------
conn = sqlite3.connect("blast_results.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS blast_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_id TEXT,
        subject_id TEXT,
        description TEXT,
        e_value REAL,
        score REAL,
        alignment TEXT
    )
''')

# --------- 3. Run BLAST automatically ---------
print("Running BLAST search... This may take some time depending on NCBI server.")
result_handle = NCBIWWW.qblast("blastn", "nt", sequence)  # blastn for nucleotide

# --------- 4. Parse BLAST XML results ---------
blast_records = NCBIXML.read(result_handle)

for alignment in blast_records.alignments:
    for hsp in alignment.hsps:
        cursor.execute('''
            INSERT INTO blast_results (query_id, subject_id, description, e_value, score, alignment)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            sequence_id,
            alignment.hit_id,
            alignment.hit_def,
            hsp.expect,
            hsp.score,
            hsp.query + "\n" + hsp.match + "\n" + hsp.sbjct
        ))

# --------- 5. Commit and close ---------
conn.commit()
conn.close()
print("BLAST search completed! Results saved in blast_results.db")
