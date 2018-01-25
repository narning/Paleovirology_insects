for i in *_*
do
    cd $i
    currentdir=$(basename `pwd`)
    echo $currentdir
    sed "s/^>/>${currentdir} /g" *cds*>${currentdir}_with_speciesnameinheader_cds.fa
    cd /home/nick/uni/rotation_paleovirology_2018/dataset_collection/virus
done
