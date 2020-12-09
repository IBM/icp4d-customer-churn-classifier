#!/bin/bash

echo "Tweaking the CSS in the notebook to work with public github viewer."

cat TradingCustomerChurnClassifierSparkML.ipynb | sed -e 's#/data/jupyter2/.*/nbextensions/brunel_ext/brunel.2.3.css#https://brunelvis.org/js/brunel.2.3.css#g' | sed -e 's#/data/jupyter2/.*/nbextensions/brunel_ext/sumoselect.css#https://brunelvis.org/js/sumoselect.css#g'| sed -e 's#/data/jupyter2/.*/nbextensions/brunel_ext/brunel.2.3.min#//brunelvis.org/js/brunel.2.3.min#g' | sed -e 's#/data/jupyter2/.*/nbextensions/brunel_ext/brunel.controls.2.3.min#//brunelvis.org/js/brunel.controls.2.3.min#g' > fixed.ipynb

echo "Saved as 'fixed.ipynb' for you to diff, copy, push..."
