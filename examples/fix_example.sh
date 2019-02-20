#!/bin/bash

echo "Tweaking the CSS in the notebook to work with public github viewer."

cat TradingCustomerChurnClassifierSparkML.jupyter-py36.ipynb | sed -e 's#/dsx-jupyter-py36/.*/.*/nbextensions/brunel_ext/#https://brunelvis.org/js/#g' > fixed.ipynb

echo "Saved as 'fixed.ipynb' for you to diff, copy, push..."
