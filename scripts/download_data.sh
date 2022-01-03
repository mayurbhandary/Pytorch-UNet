mkdir data/masks_cells 
mkdir data/imgs_cells
echo "directories created"
cd data 
if [ ! -d "./Fluo-N2DH-GOWT1" ];
then
    echo "begin download"
    curl -sS https://data.celltrackingchallenge.net/training-datasets/Fluo-N2DH-GOWT1.zip > Fluo-N2DH-GOWT1.zip &&
    unzip Fluo-N2DH-GOWT1.zip 
    rm Fluo-N2DH-GOWT1.zip &
fi
mv Fluo-N2DH-GOWT1/01/* imgs_cells/ 
mv Fluo-N2DH-GOWT1/01_GT/SEG/* masks_cells/ 

