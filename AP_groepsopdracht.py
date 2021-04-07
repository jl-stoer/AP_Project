# AP_groepsopdracht.py
# for elke regel in script
# elke regel in subs: zit line subs in line script? (niet hoofdlettergevoelig / leestekengevoelig?)
# als ie in script zit: stop hem in dictionary, previous-line ook in dict (timestamp)
# to do: manier vinden om subs niet leestekengevoelig te matchen
# to do: matchen met D lines (na merge)
# lines van subs meerdere keren gematcht
# to do: summarize differences

import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Matches script with subtitles')
    parser.add_argument('-scr', '--script', required=True,
                        help='A file which contains the script of a movie')
    parser.add_argument('-sub', '--subtitles', required=True,
                        help='A file which contains the corresponding subtitles of the added script')
    args = parser.parse_args()

    with open(args.script, 'r') as script_file:
        script_file = script_file.readlines()
    with open(args.subtitles, 'r', encoding='cp1252') as subs:
        subs = subs.readlines()
    
    number_dict = make_script_dict(script_file)
    subs_dict = make_subs_dict(subs)
    final_dict = subs_align(number_dict, subs_dict)
    
    json_output = json.dumps(final_dict, indent = 3)  
    print(json_output) 


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
        if line != '\n' and '-->' not in line and line.rstrip().isnumeric() is False:
            if prev_line != '\n' and '-->' not in prev_line and line.rstrip().isnumeric() is False:
                subs_dict[timestamp.rstrip()] = prev_line + " " + line.rstrip()
            else:
                subs_dict[timestamp.rstrip()] = line.rstrip()
        prev_line = line.rstrip()
    return subs_dict


def subs_align(dictionary, subs):
    '''match lines of the subtitles with script lines and
    add them to the dictionary along with their timestamps'''
    # memory inefficiency used_subs & ervoor zorgen dat timestamps oplopend
    # gematcht worden, daarna alles naar main dict doen
    new_dictionary = {}
    used_subs = []
    for number in dictionary:
        for key in subs:
            if subs[key].lower() in dictionary[number].lower() and subs[key] not in used_subs:
                new_dictionary[number] = [dictionary[number], key, subs[key]]
                used_subs += subs[key]
    return new_dictionary


if __name__ == "__main__":
    main()
