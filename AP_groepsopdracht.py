# AP_groepsopdracht.py
# for elke regel in script
# elke regel in subs: zit line subs in line script? (niet hoofdlettergevoelig / leestekengevoelig?)
# als ie in script zit: stop hem in dictionary, previous-line ook in dict (timestamp)
# to do: subs die op 2 lines staan op 1 line zetten, nummering en newlines weg (dictionary maken)
# to do: manier vinden om subs niet hoofdlettergevoelig / leestekengevoelig te matchen
# to do: naam matchen

import argparse


#def main():
 #   '''not the final main'''
 #   script_file = open(sys.argv[1], 'r').readlines()
  #  with open(sys.argv[2], 'r', encoding='cp1252') as subs_file:
   #     subs = subs_file.readlines()
    #number_dict = make_script_dict(script_file)
    #subs_dict = make_subs_dict(subs)
    #subs_align(number_dict, subs_dict)
    
def main():
    parser = argparse.ArgumentParser(description='Matches script with subtitles')
    parser.add_argument('-scr', '--script', required=True,
                        help='A file which contains the script of a movie')
    parser.add_argument('-sub', '--subtitles', required=True,
                        help='A file which contains the corresponding subtitles of the added script')
    args = parser.parse_args()

    with open(args.script, 'r') as script_file:
        script_file = script_file.readlines()
    with open(args.subtitles, 'r',encoding='cp1252') as subs:
        subs = subs.readlines()
    number_dict = make_script_dict(script_file)
    subs_dict = make_subs_dict(subs)
    subs_align(number_dict, subs_dict)


def make_script_dict(script_file):
    '''make a numbered dictionary with lines of the script'''
    dictionary = {}
    x = 0
    for line in script_file:
        if line != '\n':
            dictionary[x] = line.rstrip()
            x += 1 
    return(dictionary)
 
def make_subs_dict(subs):
    '''make a dictionary of a subs file, including its timestamps'''
    subs_dict = {}
    timestamp = ""
    prev_line = ""
    for line in subs:
        if '-->' in line:
            timestamp = line
        if line != '\n' and '-->' not in line and line.rstrip().isnumeric() == False:  
            if prev_line != '\n' and '-->' not in prev_line and line.rstrip().isnumeric() == False:
                subs_dict[timestamp.rstrip()] = prev_line + " " + line.rstrip() 
            else:
                subs_dict[timestamp.rstrip()] = line.rstrip()
        prev_line = line.rstrip()
    return subs_dict     

def subs_align(dictionary, subs):
    '''match lines of the subtitles with script lines and
    add them to the dictionary along with their timestamps'''
    new_dictionary = {}
    for number in dictionary:
        for key in subs:
            if subs[key].lower() in dictionary[number]:
                dictionary[number] = [dictionary[number], subs[key]]
    print(new_dictionary)            


if __name__ == "__main__":
    main()
