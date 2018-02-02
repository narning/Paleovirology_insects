base_dir=$(pwd)
for i in *_*
do
    cd $i
    currentdir=$(basename `pwd`)
    echo $currentdir
#     gunzip *cds*
    sed "s/^>/>${currentdir} /g" *.fna > ${currentdir}_with_speciesnameinheader_cds.fa
    cd $base_dir
done
