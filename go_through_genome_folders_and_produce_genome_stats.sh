for i in ./*_*/
do
    cd $i
#     echo $i
    currentdir=$(basename `pwd`)
    echo -n "$currentdir    " 
    
    if [ -f ./*.fa ]; then
        for j in *.fa
        do
            rename 's/\.(?=[^.]*\.)/_/g' '$j'
            echo -n "$j    " 
            /home/nick/uni/tools/bbmap/stats.sh $j format=6 | tail -n +2 
        done
    fi
    
    if [ -f ./*.fna ]; then
        for k in *.fna
        do
            rename 's/\.(?=[^.]*\.)/_/g' '$k'
            echo -n "$k    " 
            /home/nick/uni/tools/bbmap/stats.sh $k format=6 | tail -n +2 
        done
    fi
    
    cd /home/nick/uni/rotation_paleovirology_2018/dataset_collection/insect
done
