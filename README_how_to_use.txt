{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #how to run this script \
\
This script runs using a python library called \'93sys\'94 allowing you to use this script on the command line \
\
Here is the command to run it on linux: \
python perturbation_script.py sys.argv[1] sys.argv[2]\
\
Within the script itself, the perturbation file with sample data is the sys.argv[1] variable and the gene name ID file is the sys.argv[2] variable  \
These just means that you are passing two arguments to the python script in the form of these two files. This way, if you update the files or have new ones, simply change the name of the files on the command line you use to call the python script and you will get the perturbation results you want. \
\
Right now, this is creating files that contain the genes that are one standard deviation above and on standard deviation below the mean for each sample. \
The results are placed into files denoted \'93name of sample.high\'94 and \'93name of sample.low\'94 the \'93.high\'94 files contain the genes for that sample that are one standard deviation above the mean and the \'93.low\'94 files contain the genes for that sample that are one standard deviation below the mean. \
\
These outputs have been manually checked for accuracy. \
\
I am working on the part that converts the gene names to entrez IDs, I have a hiccup that is making the conversion not accurate and duplicating results. }