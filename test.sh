currentdir=$(basename `pwd`)
echo $currentdir
sed "s/^>/>${currentdir} /g" *cds*>${currentdir}_cds.fa
