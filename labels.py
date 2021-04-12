# group project AP
# filter function

import sys
import re
		
def add_labels_numbers(script):
    """Make a numbered dictionary with lines of the script and adds the matching label to each line""" 
    name = re.compile( r"^[A-Z\s]+$" )
    metadata = re.compile(r"(?:^.*\\R?){10}\\z")#(r"\(a-z*\)")
    dialogue = re.compile("[^\S\r\n]{8,}")    
    dictionary = {}
    x = 0

    for line in script:
        if line != '\n':
            x += 1
            if name.match(line):
                dictionary[x] = "C" + line.rstrip()
                
            elif metadata.match(line):
                dictionary[x] = "M" + line.rstrip()
                
            elif dialogue.match(line):
                dictionary[x] = "D" + line.rstrip()
   
            elif re.search(r'\bIN\b', line):
                dictionary[x] = "N" + line.rstrip()
                
            elif  re.search(r'\bON\b', line):
                dictionary[x] = "N" + line.rstrip() 
            
            elif  re.search(r'\bINT\b', line):
                dictionary[x] = "N" + line.rstrip()
            
            elif  re.search(r'\bEXT\b', line): 
                dictionary[x] = "N" + line.rstrip()
                
            elif  re.search(r'\bAT\b', line): 
                dictionary[x] = "N" + line.rstrip()
            
            elif  re.search(r'\bBACK\b', line): 
                dictionary[x] = "N" + line.rstrip()
                
            elif  re.search(r'\bUNDER\b', line): 
                dictionary[x] = "N" + line.rstrip()
            
            else: 
                if len(line) != 0:
                    dictionary[x] = "S" + line.rstrip()
    return(dictionary)                

def main(argv):
    infilename = argv[1]
    infile = open(infilename,'r')
    script = infile.readlines()
    
    output = add_labels(script)
    print(output)
    
if __name__ == "__main__":
    main(sys.argv)