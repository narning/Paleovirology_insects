for i in ./*_*/
do
    cd $i
    echo $i
    for j in *_blast.out
    do
            echo "/home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect/blast_xml_output_parser.py -xml $j -length 100"
            /home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect/blast_xml_output_parser.py -xml $j -length 100
    done
    cd /home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect
done
