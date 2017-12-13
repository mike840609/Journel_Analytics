import os 
import re 
import math 

import json
import re

# import pandas as pd
# import numpy as np

import csv

class DocOperator:

    doc_path = 'Journal_Paper'
    all_folder_dict = dict()
    docs_dict = dict()

    def __init__(self,doc_path):
        self.doc_path = doc_path
    
    def generateDoc(self):

        self.all_folder_dict = os.listdir(self.doc_path)

        #  read all file name to file_list array 
        for folder_name in self.all_folder_dict:
            text_files = [f for f in os.listdir(self.doc_path+'/'+folder_name) if f.endswith('.txt')]
            self.docs_dict[folder_name] =  text_files

    
        print(json.dumps(self.docs_dict, indent=3, sort_keys=True))


        # data = pd.read_table("test.txt" ,delim_whitespace=True, names=('A', 'B', 'C'), dtype={'A': np.int64, 'B': np.float64, 'C': np.float64})
        # print ( data )
        # with open('test.txt', 'r') as in_file:
        #     in_reader = csv.reader(in_file, delimiter = '\t')
        #     with open("test.csv", "w") as out_csv:
        #         out_writer = csv.writer(out_csv)
        #         for row in in_reader:
        #             out_writer.writerow(row)










