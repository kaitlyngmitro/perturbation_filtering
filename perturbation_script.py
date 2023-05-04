###########################################################
#perturbation_conversion_python
#
#Purpose: The purpose of this code is to take a perturbation file of gene names and assigned perturbation
# values and filter it to the genes that are one standard deviation above and one standard deviation below
# the given mean for that sample. The script creates files containing these genes named based on the
# sample they are located in. The files are denoted "sample_name.high" and "sample_name.low" to denote the
# genes that are one standard deviation higher and lower than the mean, respectively, for each sample. The
#script then uses a dictionary to convert these gene names to Entrez ID names from NCBI gene names.
#
#Author: Kaitlyn Gmitro <kgmitro@g.clemson.edu>
#
#First write: 04/13/2023
#
#Last visit: 05/3/2022
#
#This software is protected under the GPU version 3 license
###########################################################

#importing libraries
import pandas as pd
import sys

#user defined variables
perturbationfile = sys.argv[1] #'normal.perturbations.samples_AKT_UP_MTOR_DN.txt' #make this = sys.argv[1] when in final script #file that contains the perturbation file results
genenames = sys.argv[2] #'Gene_Names_and_IDs.txt' #make this = sys.argv[2] when in final script #file that contains the NCBI and Entrez IDs

#1 - Load perturbation file
perturbations = pd.read_table(perturbationfile)

#working to put into dictionary:
#https://cmdlinetips.com/2021/04/convert-two-column-values-from-pandas-dataframe-to-a-dictionary/
convert_gene_names = pd.read_table(genenames)

#2-For each column (sample) in file, find mean and standard deviation
#3-For each column, print genes that are above and below one standard deviation from the mean to a new file
newline = '\n'
gene_names = (perturbations[perturbations.columns[0]].values.tolist()) #defining gene names, column 1
col_index = -1 #setting column index at the first column
# looping over columns
for col in perturbations:
    col_index += 1 #telling the loop to read all the data in all columns in the file
    if col.startswith('TCGA'): #only looking at the columns that start with the data we are interested in
        column_ready = (perturbations[col][:-1]) #reading all rows in the desired columns
        #2-For each column (sample) in file, find mean and standard deviation
        mean_col = column_ready.mean() #taking mean for column pulled out
        stdev_col = column_ready.std() #taking standard deviation for column pulled out

        #3-For each column, print genes that are above and below one standard deviation from the mean to a new file
        row_index = 0 #defining row_index
        file_h_name = col + ".high" #placing results of genes that are one standard dev higher than mean in column_name.high
        file_l_name = col + ".low" #placing results of genes that are one standard dev lower than mean in column_name.low
        file_high = open(file_h_name, "w") #results will be written in column_name.high.txt
        file_low = open(file_l_name, "w") #results will be written in column_name.low.txt
        #loop through each column list
        for cell in column_ready:
            if (cell > (mean_col + stdev_col)): #if the row value is one standard deviation higher
                #continue
                #print(cell)

                #part I am working on to make it into entrez IDs:
                #entrez_ID = translate_ID(gene_names[row_index])
                #file_high.write(entrez_ID + newline) #future step

                file_high.write(gene_names[row_index] + newline) #write to the file the gene result
                print(gene_names[row_index], cell)
            elif (cell < (mean_col - stdev_col)): #if the row value is one standard deviation lower
                #continue
                #print(cell)

                #part I am working on to make it into entrez IDs:
                #file_low.write(entrez_ID + newline)

                file_low.write(gene_names[row_index] + newline) #write to the file the gene result
                print(gene_names[row_index], cell)
            row_index += 1
        file_high.close() #closing the high file
        file_low.close() #closing the low file
    else:
        continue

#4-Convert gene names to Entrez IDs
 #Gene_Names_and_IDs.txt has gene names and Entrez IDs
 #Entrez IDs are named ‘NCBI gene (formerly Entrezgene) ID’ in file
#5-API call to ToppFun for functional enrichment analysis
 #Website with ToppFun API —> https://toppgene.cchmc.org/API/enrich
#6-Return enrichment results
#
