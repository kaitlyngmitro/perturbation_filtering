#how to run this script 

This script runs using a python library called sys allowing you to use this script on the command line 

Here is the command to run it on linux: 
python perturbation_script.py sys.argv[1] sys.argv[2]

Within the script itself, the perturbation file with sample data is the sys.argv[1] variable and the gene name ID file is the sys.argv[2] variable  
These just means that you are passing two arguments to the python script in the form of these two files. This way, if you update the files or have new ones, simply change the name of the files on the command line you use to call the python script and you will get the perturbation results you want. 

Right now, this is creating files that contain the genes that are one standard deviation above and on standard deviation below the mean for each sample. 
The results are placed into files denoted "name of sample.high" and "name of sample.low" the ".high" files contain the genes for that sample that are one standard deviation above the mean and the ".low" files contain the genes for that sample that are one standard deviation below the mean. 
