# AP_groepsopdracht.py

import sys

def main():
    '''not the final main'''
    script_file = open(sys.argv[1], 'r').readlines()
    with open(sys.argv[2], 'r', encoding='utf8') as subs_file:
        subs = subs_file
    number_dict = make_dict(script_file)


def make_dict(script_file):
    '''make a numbered dictionary with lines of the script'''
    dictionary = {}
    x = 0
    for line in script_file:
        if line != '\n':
            dictionary[x] = line 
            x += 1 
    return(dictionary)


def subs_align(dictionary, subs):
    ''' UNFINISHED align lines of the subtitles with script lines'''
    for x in dictionary:
        for line in subs:
            if dictionary[x] == line:
                dictionary[x] = [dictionary[x],line]
    return dictionary


if __name__ == "__main__":
    main()
