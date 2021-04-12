#import AP_groepsopdracht
import labels 
import pytest
import AP_groepsopdracht

class Test_project:

    def test_number(self):
        script = AP_groepsopdracht.make_script_dict('mi.txt')
        script_keys = list(script.keys())
        assert 5 in script_keys    #kijkt of 5 in keys zit 
        assert type(script) is dict    #kijkt of data uiteindelijk een dictionary is 
    
    def test_labels(self):
        labels_dict = labels.add_labels('mi.txt')
        values_list = list(labels_dict.values())
        #for line in values_list: 
         #   if line.startswith("C"):              hier wilde ik dus testen of een line start met "C" als JACK in de line staat, maar dat lukt dus niet
          #      assert line
        #if "JACK" in values_list:      
            #assert line.startswith("C")
        
        assert type(labels_dict) is dict  #kijkt hier dus ook weer of data uiteindelijk dictionary is
        

