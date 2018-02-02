import sys
from Bio import SeqIO

fasta = sys.argv[ 1]
virus_taxonomy2filter = sys.argv[ 2]

with open( fasta.split(".fa")[0] + "_w_" + virus_taxonomy2filter + "_filtered.fa", "w+") as outf:
    for seq_record in SeqIO.parse(fasta , "fasta"):
        if virus_taxonomy2filter not in seq_record.description:
            outf.write(">{}\n{}\n".format(seq_record.description, seq_record.seq))
