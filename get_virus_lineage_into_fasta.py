import sys


virus_lineage_dict = {}

with open( sys.argv[ 1]) as virus_db:
    for i, line in enumerate( virus_db, 0):
        
        if i == 0:
            continue
        
        else:
            linesplit = line.split("\t")
            virus_name = linesplit[ 1].replace( " ","_")
            virus_lineage = linesplit[ 2].replace(";","|").replace("| ","|").replace(" ","_")
            virus_lineage_dict[ virus_name] = virus_lineage

with open( sys.argv[ 2].split(".fa")[ 0] + "_pluslineage_filter_less_150nt.fa", "w+") as outf:
    with open( sys.argv[ 2]) as fasta:
        fasta_handle = fasta.read()
        fasta_handle = fasta_handle.split( ">")[ 1:]
        fasta_handle = [ x.split( "\n", 1) for x in fasta_handle]
        
        for entry in fasta_handle:
            
            if len(entry) > 1:
                header = entry[ 0]
                header = header.split(" ")
                species = header[ 0].split("_")[ 1: ]
                species = "_".join( species)
                
                if species in virus_lineage_dict:
                    header[0] = header[0] + " " +  virus_lineage_dict[ species]
                else:
                    header[0] = header[0] + " " + "lineage_not_in_virus_host_db"
                
                header = ">" + " ".join( header)
                sequence = entry[ 1].replace( "\n", "")
                if len( sequence) >= 150:
                    outf.write( header + "\n" + sequence + "\n")
