import pytest
import AP_groepsopdracht


def test_script():
    script = AP_groepsopdracht.add_labels_numbers('mi.txt')
    name_list = ['JACK', 'ETHAN']
    dialogue_list = ['     INT. THE HOUSE', '     ON THE FLOOR']
    script_keys = list(script.keys())

    assert type(script) is dict
    assert AP_groepsopdracht.add_labels_numbers(name_list) == {1: 'CJACK', 2: 'CETHAN'}
    assert AP_groepsopdracht.add_labels_numbers(dialogue_list) == {1: 'N     INT. THE HOUSE', 2: 'N     ON THE FLOOR'}
    assert 5 in script_keys


def test_subs():
    subs = AP_groepsopdracht.make_subs_dict('mi.srt')

    assert '\n' not in subs


def test_subs_align():
    script = AP_groepsopdracht.add_labels_numbers('mi.txt')
    subs = AP_groepsopdracht.make_subs_dict('mi.srt')
    subs_aligned = AP_groepsopdracht.subs_align(script, subs)
