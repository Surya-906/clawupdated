NCELL=$1
FILE=error.txt
rm -rf $FILE && touch $FILE
for ncell in $NCELL
do 
   echo "ncell = $ncell"
   python clawnew.py -Tf 1.0 -ncellx $ncell -ncelly $ncell -compute_error yes \
          -plot_freq 0 -scheme hancock -save_freq 0 -cfl 0.4 -limit mmod >log.txt
   tail -n 1 log.txt
   tail -n 1 log.txt >> $FILE
done
echo "Wrote file $FILE"