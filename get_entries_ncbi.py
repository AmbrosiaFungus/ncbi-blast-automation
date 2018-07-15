#This file should get the data from NCBi and performs a blast

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML



#read in our sequences

with open("sample.fasta", "r") as fasta_file:
    sequences = fasta_file.read()
    fasta_file.close()

# blast the sequences
result_handle = NCBIWWW.qblast("blastn", "nt", sequences.format("fasta"))

#what are the blast results

blast_records = NCBIXML.parse(result_handle)


#that prints all results, but I want just the top 10 hits. Fix that.

for blast_record in blast_records:

    for description in blast_record.descriptions:
         print(description.title)
















#save_file = open("out.xml", "w")

#save_file.write(result_handle.read())

#save_file.close()

#result_handle.close()
