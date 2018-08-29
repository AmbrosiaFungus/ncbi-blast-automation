from Bio.Blast import NCBIWWW
from datetime import datetime
startTime = datetime.now()

with open("sample.fasta", "r") as fasta_file:
    sequences = fasta_file.read()
    fasta_file.close()

    result_handle = NCBIWWW.qblast("blastn", "nt", sequences)
    save_result = open("blast_result.xml", "w")
    save_result.write(result_handle.read())
    save_result.close()
    result_handle.close()

print(datetime.now() - startTime)
