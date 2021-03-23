#!/bin/bash

gnome-terminal\
	 --tab\
	   -e 'conda activate aiffel'\
	   -e 'jupyter notebook --NotebookApp.token=test-secret --NotebookApp.allow_origin='https://aiffelstaticprd.blob.core.windows.net' --no-browser'\
	 #--tab\
	 #  -e 'conda activate aiffel'\
	 #  -e 'cd ~'\
	 #  -e 'jupyter lab'

echo "Ta da!"
