import re
data1 = open('Pydata 1.txt')
list_of_sum = []
count = 0
total = 0

for line in data1:
    line.split()
    y = re.findall('[0-9]+',line)
    count = count + len(y)
    y = map(int,y) # map function is used for converting the list of datatypes.
                    #In this case I changed list strings into list of int.  
    
    if y!=[]:                      #if y(list of the numbers) are not empty

        list_of_sum.append(sum(y))  #appending or putting or adding the sum of each single line list

        total = sum(list_of_sum)    # its the grand total of all numbers

        print '\nBefore ->', y ,'\nAfter ->', list_of_sum,'\ntotal SUM is :',total ,', Total numbers = ', count
        
print'The Average :',float(total)/float(count)
