import os 
import re 
import math 

import json
import re


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import glob

class DocOperator:

    doc_path = 'Journal_Paper'
    all_folder_dict = dict()
    docs_dict = dict()

    def __init__(self,doc_path):
        self.doc_path = doc_path

    
    def generateDoc(self):
        self.all_folder_dict = glob.glob(os.path.join(self.doc_path, 
        '*'))
        # print (self.all_folder_dict)

        #  read all file name to file_list array 
        for folder_name in self.all_folder_dict:
            text_files = [f for f in os.listdir(folder_name) if (f.endswith('.txt'))]
            self.docs_dict[folder_name] =  text_files
        # print(json.dumps(self.docs_dict, indent=3, sort_keys=True))

    
        

    
    def convertCsv(self):

        for journal_name , j_list in self.docs_dict.items():
            for part in j_list :
                
                filepath = journal_name + '/'+ part
                df=pd.read_csv(filepath,delimiter="\t", encoding = 'utf-16-le')
                
                # print( df.tail(1))
                print(df[:1])
                break

            break












