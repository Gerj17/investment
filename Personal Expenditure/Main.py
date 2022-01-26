doc_name = input("Document Name: ")

with open(str(doc_name),"r") as doc:
    for line in doc:
        with open("main_doc.txt","a") as d2:
            if line.isspace():
                #print('true')
                pass
            else:
                print(line)
                d2.write(line.strip())
        
import write_to_csv