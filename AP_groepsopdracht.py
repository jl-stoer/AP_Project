# AP_groepsopdracht.py
# to do: matchen met D lines (na merge)
# to do: summarize differences

import argparse
import json
from difflib import SequenceMatcher


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

    json_output = json.dumps(final_dict, indent=3)
    print(json_output)
    print('The percentage of matching dialogue in the script and subtitles is: {0}%'.format(percentage_matching(number_dict, subs_dict)))


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
    '''make a dictionary of a subs file, using its timestamps as keys'''
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
    new_dictionary = {}
    prev_time = 0
    for number in dictionary:
        for key in subs:
            key.replace('<i>', '')
            key.replace('</i>', '')
            time = int(key[0:8].replace(':', ''))
            if subs[key].lower() in dictionary[number].lower() and time > prev_time:
                new_dictionary[number] = [dictionary[number], key, subs[key]]
                prev_time = time
    return new_dictionary


def percentage_matching(dictionary, subs):
    '''check what percentage of dialogue matches between
    the script and the subtitles'''
    script_dialogue = dictionary #alle zinnen die gelabeld zijn als D
    subs_dialogue = subs.values()
    matching_percentage = 0#SequenceMatcher(None, dictionary, subs).ratio()
    return matching_percentage


if __name__ == "__main__":
    main()
