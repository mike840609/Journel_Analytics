from DocOperator import DocOperator

def main():
    docOpe_obj = DocOperator("./Journal_Paper")
    docOpe_obj.generateDoc()
    docOpe_obj.convertCsv()



if __name__ == '__main__':
    main()