## Sean Beaulieu
## beaul116

#Part 1: get_data_list
#==============================0============
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    l1 = []
    l2 = []
    try:
        fp = open(fname)
        for line in fp:
            l2 = line.split(',')
            l3 = ','.join(l2)
            l1.append(l3)
        fp.close()
    except FileNotFoundError:
        return -1   
    return l1



#Part 2: hw8_index
#==========================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#==========================================


def hw8_index(row1_str):     

    #Hint: You may use list.index(), but must prevent an error if the
    #'hw8 Grade' column is not present

    l1 = row1_str.split(',')
    try:
        index = l1.index('hw8 Grade')    
    except ValueError:
        return -1
    return index



#Part 3: alter_grade
#==========================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#==========================================


def alter_grade(row_str,idx):
    #Hint: Use .split and .join
    l1 = row_str.split(',')
    l1[idx] = '40'
    string1 = ','.join(l1)
    return string1



#Part 4: haxx
#==========================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file doesn't exist
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):

    #Hints:
    #   Use get_data_list to read in the rows from the file
    #   Use hw8_index to determine which column you need to change
    #   Write back each row unchanged, unless it contains your
    #   full name, exactly as it appears on Canvas
    #   If it does contain your name, use alter_grade to create an
    #   altered row string to write to the file instead
    #   Be sure to close the file
    try:
        fp = open(fname)
        l1 = get_data_list(fname)
        first_line = fp.readline()
        if hw8_index(first_line) != -1:
            index = hw8_index(first_line)
            
            for line in l1:
                
                if "Sean Beaulieu" in line:
                    line = alter_grade(line,index)
                    
                
        else:
            return False
    except FileNotFoundError:
        return False
    fp.close()
    return True
            
