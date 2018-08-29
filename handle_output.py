from Bio.Blast import NCBIXML
import pandas as pd
from pandas.io.json import json_normalize


from Bio.Blast import NCBIWWW

with open("sample.fasta", "r") as fasta_file:
    sequences = fasta_file.read()
    fasta_file.close()

    result_handle = NCBIWWW.qblast("blastn", "nt", sequences)
    save_result = open("blast_result.xml", "w")
    save_result.write(result_handle.read())
    save_result.close()
    result_handle.close()


result = open("blast_result.xml", "r")
records = NCBIXML.parse(result)

#Create the outer list
final = []
for blast_record in records:
    dic = {}
    #print(blast_record.query)
    query_title = blast_record.query.split("|")[0]
    dic["id"] = query_title
    pairs = []
    for i in blast_record.descriptions:
        ncbi = i.title.split("|")[3]
        name = " ".join(i.title.split("|")[4].split(" ")[1:3])
        e_value = i.e
        score = i.score
        dic_pairs = {}
        # Make a dictionary containing the name and the e_value
        dic_pairs["hit"] = name
        dic_pairs["e-value"] = e_value
        dic_pairs["ncbi"] = ncbi
        dic_pairs["score"] = score
        dic_pairs["gi_number"] = i.title.split("|")[1]
        pairs.append(dic_pairs)
        #Maybe use a counter to break out of the loop
    k =[]
    for alignment in blast_record.alignments:
        new = {}
        for hsp in alignment.hsps:
            new["coverage"] = hsp.align_length / blast_record.query_length
            new["bits"] = hsp.bits
            new["percent"] = hsp.identities / hsp.align_length
            k.append(new)

    dic["pairs"] = pairs
    dic["k"] = k
    final.append(dic)
