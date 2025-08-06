echo "downloading toupcam sdk"
curl -L# https://www.touptekphotonics.com/software/toupcamsdk.20250722.zip -o toupcamsdk.zip
unzip toupcamsdk.zip -d toupcamsdk

mkdir -p toupcam/lib

echo "copying files into local target dir"
cp toupcamsdk/python/toupcam.py toupcam/toupcam.py
cp -r toupcamsdk/linux/{arm64,x86,x64,udev} toupcam/lib/

rm -rf toupcamsdk
rm toupcamsdk.zip

echo "import * from .toupcam" > toupcam/__init__.py

