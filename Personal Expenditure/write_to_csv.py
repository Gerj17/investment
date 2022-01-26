# Write Main_doc data to Csv
with open("main_doc.txt","r" ) as md:
    date = [] # used to temperatily hold the date to fill in 
    for line in md:
        #if line[:-3
       with open('Gerard Expenditure.csv','a') as t:
            # t.write(f'date , description , value \n')
            # Determine if a line file is a date or information line
            
            try:
                var = line[:2] # get first two items in line 
                var1 = int(line[:2]) # convert to int if in line is date 
                #print(f'date ---------> {var}')
                ##t.write(f'{line},')
                #date.clear()
                date.append(line)
            except ValueError:
                #print(f'information --> {var}')
                info_list = line.split('$')
                t.write(f'{date[-1].strip()},{info_list[0]},{info_list[1]} \n')
                # Write information to CSV 
                print(f'{date[-1].strip()},{info_list[0]},{info_list[1]} \n')


#TODO Add safety to ensure there are no dulicates 
# TODO clean code 
        
        