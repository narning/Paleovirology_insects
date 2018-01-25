for i in *_*
do
    cd $i
    echo $i
    for j in *.fa
    do
        makeblastdb -in $j -parse_seqids -dbtype nucl
    done
    cd /home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect
done
