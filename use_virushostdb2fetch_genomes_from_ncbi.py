#!/usr/bin/python

#script to use the virus to host db and the assembly_summary_refseq from ncbi tofetch viral genomes from the ncbi ftp page by taxid
import sys
import subprocess

with open(sys.argv[1]) as virus2host:
    taxid_dict = {}
    
    for i, line in enumerate( virus2host, 0):
    
        if i == 0:
            continue
        else:
            linesplit = line.split("\t")
            virus_taxid = linesplit[ 0]
            taxid_dict[virus_taxid] = ""
            #print virus_taxid
            
with open(sys.argv[2]) as assembly_summary:
    counter = 0
    
    for line in assembly_summary:
    
        if line.startswith("#"):
            continue
        else:
            linesplit = line.split("\t")
            assembly_taxid = linesplit[ 5]
            
            if assembly_taxid in taxid_dict:
                counter += 1
                
                print "PROCESSING VIRAL GENOME NO {}".format( counter)
                
                virus_name = linesplit[ 7].replace(" ", "_")
                ftp_link = linesplit[ -3]
                bashCommand = "wget -P {} {}/*.fna.gz".format(  virus_name, ftp_link)
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
            
