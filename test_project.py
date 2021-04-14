import pytest
import AP_groepsopdracht


def test_script():
    script = AP_groepsopdracht.add_labels_numbers('mi.txt')
    name_list = ['JACK', 'ETHAN']
    location_list = ['     INT. THE HOUSE',
                     '     EXT. VIRGINIA TWO LANE HIGHWAY - DAY']
    script_keys = list(script.keys())

    assert type(script) is dict
    assert AP_groepsopdracht.add_labels_numbers(name_list) == {1: 'CJACK',
           2: 'CETHAN'}
    assert AP_groepsopdracht.add_labels_numbers(location_list) == {1:
           'N     INT. THE HOUSE', 2: 'N     EXT. VIRGINIA TWO LANE HIGHWAY - DAY'}
    assert 5 in script_keys


def test_subs():
    subs = AP_groepsopdracht.make_subs_dict('mi.srt')
    assert '\n' not in subs

def test_percentage():
    script = AP_groepsopdracht.add_labels_numbers('mi.txt')
    subs = AP_groepsopdracht.make_subs_dict('mi.srt')
    percentage = AP_groepsopdracht.percentage_matching(script, subs)
    assert type(percentage) is float
