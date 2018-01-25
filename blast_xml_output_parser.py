#!/usr/bin/env python

import argparse
from Bio.Blast import NCBIXML


def read_in_xml( xml_inf):
    
    with open( xml_inf) as xml:
        with open( "{}_parsed_cutoff_{}nt.out".format( xml_inf.split(".out")[ 0], args.length) , "w+") as outf:
            hit_no = 0
            
            xml_parse = NCBIXML.parse( xml)
            
            List_of_hits_to_sort = []
            
            for entry in xml_parse:
                
                for alignment in entry.alignments:
                    
                    for hsp in alignment.hsps:
                        length = hsp.identities
                       
                        if length > 100:
                            output_string = ""
                            output_string +=  "alignment_length\t{}\n".format( length)
                            output_string +=  "alignment_evalue\t{}\n".format( hsp.expect)
                            output_string +=  "alignment_score\t{}\n".format( hsp.score)
                            output_string +=  "query\t{}\n".format( entry.query)
                            output_string +=  "query_pos\t{}\t{}\n".format( hsp.query_start, hsp.query_end)
                            output_string +=  "hsp\n"
                            output_string +=  "{}\n{}\n{}\n".format( hsp.query, hsp.match, hsp.sbjct)
                            output_string +=  "match\t{}\n".format( alignment.title)
                            output_string +=  "query_pos\t{}\t{}\n".format( hsp.sbjct_start, hsp.sbjct_end)
                            output_string +=  "#\n"
                            List_of_hits_to_sort.append((length , output_string))

            for hit in sorted( List_of_hits_to_sort, reverse = True):
                hit_no += 1
                outf.write( "hit_number\t{}\n".format( hit_no))
                outf.write( hit[ 1])

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Parse the xml blast output for EVE detection')
    parser.add_argument('-xml', type=str, help='xml blast output (outfmt 5)')
    parser.add_argument('-length', type=str, help='minimum matched nucleotides in alignment')
    args = parser.parse_args()
    xml_inf = args.xml
    
    read_in_xml( xml_inf    )
