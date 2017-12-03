import os 
import re 
import math 

import json
import re

class DocOperator:

    doc_path = ''
    all_folder_dict = dict

    def __init__(self,doc_path):
        self.doc_path = doc_path
    
    def generateDoc(self):

        self.doc_list = [] 
        self.all_folder_dict = dict.fromkeys(os.listdir(self.doc_path), dict({"file_list":[],"word_freq_dict":{} }))
        
        #  read all file name to file_list array 

        for folder_name in self.all_folder_dict:

            self.all_folder_dict[folder_name]["file_list"] = os.listdir(self.doc_path + '/' + folder_name)
            self.all_folder_dict[folder_name]["file_list"].sort(key=self.natural_keys)

        # convert to excel 
        



        print (json.dumps(self.all_folder_dict, indent=2))

    
    



    #  sort array by name 
    def atoi(self,text):
        return int(text) if text.isdigit() else text

    def natural_keys(self,text):
        return [ self.atoi(c) for c in re.split('(\d+)', text) ]


