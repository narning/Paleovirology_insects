query=/home/nick/uni/rotation_paleovirology_2018/dataset_collection/virus/all_cds_w_speciesheader_cd-hit_c_097_pluslineage_filter_less_80aa_header_wo_whitespace.fa

for i in ./*_*/
do
    cd $i
    echo $i
    for j in *.fa
    do
        if [ ! -f ${j}_blast.out ]; then
            echo "blastn -query $query -db $j -task 'blastn' -out ${j}_blast.out -evalue 0.0001 -outfmt 5"
            blastn -query $query -db $j -task 'blastn' -out ${j}_blast.out -evalue 0.0001 -outfmt 5
        fi
    done
    
    for k in *fna
    do
        if [ ! -f ${k}_blast.out ]; then
            echo "blastn -query $query -db $k -task 'blastn' -out ${k}_blast.out -evalue 0.0001 -outfmt 5"
            blastn -query $query -db $k -task 'blastn' -out ${k}_blast.out -evalue 0.0001 -outfmt 5
        fi
    done
    cd /home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect
done
