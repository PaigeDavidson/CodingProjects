#############################################################
# module: bin_id3_uts.py
# description: unit tests for bin_id3 class.
# bugs to vladimir kulyukin on canvas
##############################################################

import unittest
from bin_id3 import id3_node
from bin_id3 import bin_id3
from bin_id3 import PLUS, MINUS

class bin_id3_uts(unittest.TestCase):

    def test_id3_ut00(self, tn=0):
        """
        Parses csv file play_tennis.csv into examples and column names.
        Displays all examples.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        assert len(examples) == 14
        print('attribs = {}'.format(attribs))
        print('\nColumn/attribute names:')
        for i, cn in enumerate(colnames):
            print('{}) {}'.format(i+1, cn))
        print('\nExamples:')        
        for i, ex in enumerate(examples):
            print('{}) {}'.format(i+1, ex))

    def test_id3_ut01(self, tn=1):
        """
        Tests bin_id3.construct_attrib_values_from_examples().
        """
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        print('Attribute --> Values:\n')
        for k, v in avt.items():
            print('{} --> {}'.format(k, v))

    def test_id3_ut02(self, tn=2):
        """
        Tests id3_node class and constructs a decision tree manually.
        """
        print('========== UT {} ===================='.format(tn))        
        ## construction of leaves PLUS/YES and MINUS/No.
        plus_node = id3_node(PLUS)
        assert plus_node.get_label() == PLUS
        minus_node = id3_node(MINUS)
        assert minus_node.get_label() == MINUS

        ## construction of Humidity node
        humidity_node = id3_node('Humidity')
        assert humidity_node.get_label() == 'Humidity'
        humidity_node.add_child('High', minus_node)
        humidity_node.add_child('Normal', plus_node)
        assert humidity_node.get_child('High').get_label() == MINUS
        assert humidity_node.get_child('Normal').get_label() == PLUS
        assert len(humidity_node.get_children()) == 2
        bin_id3.display_id3_node(humidity_node, '')

        ## construction of Wind node
        wind_node = id3_node('Wind')
        assert wind_node.get_label() == 'Wind'
        wind_node.add_child('Strong', minus_node)
        wind_node.add_child('Weak', plus_node)
        assert wind_node.get_child('Strong').get_label() == MINUS
        assert wind_node.get_child('Weak').get_label() == PLUS
        assert len(wind_node.get_children()) == 2
        bin_id3.display_id3_node(wind_node, '')

        ## construction of Outlook node
        outlook_node = id3_node('Outlook')
        assert outlook_node.get_label() == 'Outlook'
        outlook_node.add_child('Sunny', humidity_node)
        assert outlook_node.get_child('Sunny').get_label() == 'Humidity'
        outlook_node.add_child('Overcast', plus_node)
        assert outlook_node.get_child('Overcast').get_label() == PLUS
        outlook_node.add_child('Rain', wind_node)
        assert outlook_node.get_child('Rain').get_label() == 'Wind'
        assert len(outlook_node.get_children()) == 3

        ## display the entire decsion tree rooted in Outlook.
        bin_id3.display_id3_node(outlook_node, '')

    def test_id3_ut03(self, tn=3):
        """
        - Finds the examples with Outlook=Sunny;
        - In the examples with Outlook=Sunny finds all examples with PlayTennis=Yes;
        - In the examples with Outlook=Sunny finds all examples with PlayTennis=No.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        print('\nExamples with Outlook=Sunny:')
        for i, ex in enumerate(outlook_sunny_examples):
            print('{}) {}'.format(i+1, ex))

        sunny_yes_examples = bin_id3.find_examples_given_attrib_val(outlook_sunny_examples, 'PlayTennis', 'Yes')
        assert len(sunny_yes_examples) == 2
        print('\nExamples with Outlook=Sunny and PlayTennis=Yes:')
        for i, ex in enumerate(sunny_yes_examples):
            print('{}) {}'.format(i+1, ex))

        sunny_no_examples = bin_id3.find_examples_given_attrib_val(outlook_sunny_examples, 'PlayTennis', 'No')
        assert len(sunny_no_examples) == 3

        print('\nExamples with Outlook=Sunny and PlayTennis=No:')
        for i, ex in enumerate(sunny_no_examples):
            print('{}) {}'.format(i+1, ex))

    ### ============================= Problem 1 UTs ====================================

    def test_id3_ut04(self, tn=4):
        """
        Tests bin_id3.proportion(). What proporition of examples has PlayTennis=Yes.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        attrib     = 'PlayTennis'
        attrib_val = 'Yes'
        p = bin_id3.proportion(examples, attrib, attrib_val)
        print('Proportion({}, {}) = {}'.format(attrib, attrib_val, p))
        gt  = 9.0/14
        err = 0.0001
        assert abs(p - gt) <= err

    def test_id3_ut05(self, tn=5):
        """
        Tests bin_id3.proportion(). What proporition of examples has Humidity=High.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        attrib     = 'Humidity'
        attrib_val = 'High'
        p = bin_id3.proportion(examples, attrib, attrib_val)
        print('Proportion({}, {}) = {}'.format(attrib, attrib_val, p))
        gt  = 7.0/14
        err = 0.0001
        assert abs(p - gt) <= err

    def test_id3_ut06(self, tn=6):
        """
        Finds entropy of the original examples with respect to target_attribute PlayTennis.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H = bin_id3.entropy(examples, 'PlayTennis', avt)
        ## ground truth value for Entropy
        gH = 0.9402859586706309
        err = 1.0e-3
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err

    def test_id3_ut07(self, tn=7):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
        Compute Entropy(S) w/ respect to PlayTennis;
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H   = bin_id3.entropy(outlook_sunny_examples, 'PlayTennis', avt)
        gH  = 0.9709505944546686
        err = 1.0e-3
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err

    def test_id3_ut08(self, tn=8):
        """
        Computes information gain of Wind in the examples and target_attribute PlayTennis.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        #print('bin_id3: avt={}'.format(avt))
        g   = bin_id3.gain(examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.04812703040826927
        err = 1.0e-3
        print('Gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut09(self, tn=9):
        """
        Tests information gain of Humidity in the examples and target_attribute PlayTennis.
        """        
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.15183550136234136
        err = 1.0e-3
        print('Gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut10(self, tn=10):
        """
        Tests information gain of Outlook in the examples and target_attribute PlayTennis.
        """        
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Outlook', avt)
        gt  = 0.2467498197744391
        err = 1.0e-3
        print('Gain(Outlook)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut11(self, tn=11):
        """
        Tests information gain of Temperature in the examples and target_attribute PlayTennis.
        """        
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.029222565658954647
        err = 0.0001
        print('Gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut12(self, tn=12):
        """
        Find all examples with Outlook=Sunny and compute info gain of Humidity.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.9709505944546686
        err = 1.0e-3
        print('Gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut13(self, tn=13):
        """
        Find all examples with Outlook=Sunny and compute info gain of Temperature.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.5709505944546686
        err = 1.0e-3
        print('Gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut14(self, tn=14):
        """
        Find all examples with Outlook=Sunny and compute info gain of Wind.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.01997309402197489
        err = 1.0e-3
        print('Gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut15(self, tn=15):
        """
        Find all examples with Outlook=Overcast and check that those examples consist 
        of 4 positive examples and 0 negative examples.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        print('Examples with Outlook=Overcast:\n')
        for i, ex in enumerate(outlook_over_examples):
            print('{}) {}'.format(i+1, ex))
        assert len(bin_id3.find_examples_given_attrib_val(outlook_over_examples, 'PlayTennis', 'Yes')) == 4
        assert len(bin_id3.find_examples_given_attrib_val(outlook_over_examples, 'PlayTennis', 'No'))  == 0

    def test_id3_ut16(self, tn=16):
        """
        Find all examples with Outlook=Overcast and compute info gain of Humidity.
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.00
        err = 1.0e-3
        print('Gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut17(self, tn=17):
        """
        Find all examples with Outlook=Overcast and compute info gain of Temperature.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.0
        err = 1.0e-3
        print('Gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut18(self, tn=18):
        """
        Find all examples with Outlook=Overcast and compute info gain of Wind.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.0
        err = 0.0001
        print('Gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err

    def test_id3_ut19(self, tn=19):
        """
        Find all examples with Outlook=Rain and check that they include 3 positive and 2 negative
        examples.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_rain_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Rain')
        print('Examples with Outlook=Rain:\n')
        for i, ex in enumerate(outlook_rain_examples):
            print('{}) {}'.format(i+1, ex))
        assert len(bin_id3.find_examples_given_attrib_val(outlook_rain_examples, 'PlayTennis', 'Yes')) == 3
        assert len(bin_id3.find_examples_given_attrib_val(outlook_rain_examples, 'PlayTennis', 'No')) == 2

    def test_id3_ut20(self, tn=20):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
        Compute 
        1) Entropy(S);
        2) Gain(Temperature);
        3) Gain(Humidity);
        4) Gain(Wind);
        """
        print('========== UT {} ===================='.format(tn))        
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H   = bin_id3.entropy(outlook_sunny_examples, 'PlayTennis', avt)
        gH  = 0.9709505944546686
        err = 1.0e-3
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.5709505944546686
        err = 1.0e-3        
        print('Gain(Temperature)={}'.format(g))
        assert abs(g-gt) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.9709505944546686
        err = 1.0e-3        
        print('Gain(Humidity)={}'.format(g))
        assert abs(g-gt) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.01997309402197489
        err = 1.0e-3        
        print('Gain(Wind)={}'.format(g))
        assert abs(g-gt) <= err

    def test_id3_ut21(self, tn=21):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}

        Find most common value for attribute PlayTennis
        Find most common value for attribute Humdity
        Find most common value for attribute Wind
        Find most common value for attribute Temperature
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'PlayTennis', avt)
        assert atv == 'No'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Humidity', avt)
        assert atv == 'High'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Wind', avt)
        assert atv == 'Weak'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Temperature', avt)
        assert atv == 'Hot' or atv == 'Mild'
        assert cnt == 2

    def test_id3_ut22(self, tn=22):
        """
        Find best (i.e., highest info gain) attribute in original Examples and display its
        info gain and the gains all the other attributes.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        ba, bag, gs = bin_id3.find_best_attribute(examples, 'PlayTennis', attribs, avt)
        assert ba == 'Outlook'
        gt  = 0.2467498197744391
        err = 0.0001
        assert abs(bag - gt) <= err
        bin_id3.display_info_gains(gs)
        print('Best Attribute = {}'.format(ba))
        print('Best Gain      = {}'.format(bag))

    ### =================== Problem 2 UTs ==============================

    def test_id3_ut23(self, tn=23):
        """
        Fit a decision tree with Binary ID3 to labeled examples and display it.
        """
        print('========== UT {} ===================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        root = bin_id3.fit(examples, target_attrib, attribs, avt, False)   
        bin_id3.display_id3_node(root, '')

    """
    This is the my output from test_id3_ut23(self, tn=23) that shows the gradual
    construction of the DT for Quinlan's dataset when the last argument to
    bin_id3.fit(examples, target_attrib, attribs, avt, False) is changed to True.  
========== UT 23 ====================
Looking for best attribute among Humidity, Outlook, Wind, Temperature...
Information gains are as follows:
	Humidity: 0.15183550136234136
	Outlook: 0.2467498197744391
	Wind: 0.04812703040826927
	Temperature: 0.029222565658954647
Best attrib is Outlook with a gain of 0.2467498197744391...
Removing Outlook from list of attributes...

Looking for examples where Outlook=Sunny...
Found the following examples where Outlook=Sunny...
{'Day': 'D1', 'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
{'Day': 'D2', 'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
{'Day': 'D8', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
{'Day': 'D9', 'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}

Recusively building decision tree for examples where Outlook=Sunny...
Looking for best attribute among Humidity, Temperature, Wind...
Information gains are as follows:
	Humidity: 0.9709505944546686
	Temperature: 0.5709505944546686
	Wind: 0.01997309402197489
Best attrib is Humidity with a gain of 0.9709505944546686...
Removing Humidity from list of attributes...

Looking for examples where Humidity=Normal...
Found the following examples where Humidity=Normal...
{'Day': 'D9', 'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}

Recusively building decision tree for examples where Humidity=Normal...
All examples positive...
Setting label of root to Yes
Adding child node Yes to root Humidity on link Normal...

Looking for examples where Humidity=High...
Found the following examples where Humidity=High...
{'Day': 'D1', 'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
{'Day': 'D2', 'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
{'Day': 'D8', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}

Recusively building decision tree for examples where Humidity=High...
All examples negative
Setting label of root to No
Adding child node No to root Humidity on link High...

Adding child node Humidity to root Outlook on link Sunny...

Looking for examples where Outlook=Overcast...
Found the following examples where Outlook=Overcast...
{'Day': 'D3', 'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D7', 'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
{'Day': 'D12', 'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
{'Day': 'D13', 'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}

Recusively building decision tree for examples where Outlook=Overcast...
All examples positive...
Setting label of root to Yes
Adding child node Yes to root Outlook on link Overcast...

Looking for examples where Outlook=Rain...
Found the following examples where Outlook=Rain...
{'Day': 'D4', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D5', 'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D6', 'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'}
{'Day': 'D10', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D14', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}

Recusively building decision tree for examples where Outlook=Rain...
Looking for best attribute among Humidity, Temperature, Wind...
Information gains are as follows:
	Humidity: 0.01997309402197489
	Temperature: 0.01997309402197489
	Wind: 0.9709505944546686
Best attrib is Wind with a gain of 0.9709505944546686...
Removing Wind from list of attributes...

Looking for examples where Wind=Strong...
Found the following examples where Wind=Strong...
{'Day': 'D6', 'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'No'}
{'Day': 'D14', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}

Recusively building decision tree for examples where Wind=Strong...
All examples negative
Setting label of root to No
Adding child node No to root Wind on link Strong...

Looking for examples where Wind=Weak...
Found the following examples where Wind=Weak...
{'Day': 'D4', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D5', 'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
{'Day': 'D10', 'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}

Recusively building decision tree for examples where Wind=Weak...
All examples positive...
Setting label of root to Yes
Adding child node Yes to root Wind on link Weak...

Adding child node Wind to root Outlook on link Rain...

Outlook
	Sunny
		Humidity
			Normal
				Yes
			High
				No
	Overcast
		Yes
	Rain
		Wind
			Strong
				No
			Weak
				Yes
    """

    def test_id3_ut24(self, tn=24):
        """
        Fit a decision tree with Binary ID3 to 14 labeled examples; 
        Predict labels of the same 14 examples with the target attribute values
        removed (such examples are called unlabeled).
        The unlabeled examples are loaded from play_tennis_unlbl.csv.
        """
        print('========== UT {} ===================='.format(tn))
        global PLUS
        global MINUS
        
        ### Let's learn a DT.
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        dtr = bin_id3.fit(examples, target_attrib, attribs, avt, False)   
        bin_id3.display_id3_node(dtr, '')

        ### Let's load unlabeled examples
        unlbl_examples, unlbl_colnames = bin_id3.parse_csv_file_into_examples('play_tennis_unlbl.csv')
        print(len(unlbl_examples))
        print('Unlabeled Examples:\n')
        for i, ex in enumerate(unlbl_examples):
            print('{}) {}'.format(i+1, ex))
        print('\nColumn names:')
        for i, cn in enumerate(unlbl_colnames):
            print('{}) {}'.format(i+1, cn))

        prediction = bin_id3.predict(dtr, unlbl_examples[0])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[1])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[2])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[3])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[4])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[5])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[6])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[7])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[8])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[9])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[10])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[11])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[12])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[13])
        assert prediction == MINUS

    ### test predict
    def test_id3_ut25(self, tn=25):
        """
        Tests the DT on play_tennis_data.csv and play_tennis_target.txt.
        play_tennis_data.csv contains 1000 examples whose target values are given
        in play_tennis_target.txt.
        """
        print('============ UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        dtr = bin_id3.fit(examples, target_attrib, attribs, avt, False)
        print('Learned decision tree is\n')
        bin_id3.display_id3_node(dtr, '')
        uexamples, ucolnames = bin_id3.parse_csv_file_into_examples('play_tennis_data.csv')
        gt = []
        with open('play_tennis_target.txt', 'r') as inf:
            for ln in inf:
                gt.append(ln.strip())
        assert len(uexamples) == len(gt)
        accurate_count = 0
        for uex, gtt in zip(uexamples, gt):
            pred = bin_id3.predict(dtr, uex)
            if pred == gtt:
                accurate_count += 1
        accuracy = accurate_count/len(uexamples)
        assert accuracy == 1.0
        print('classification accuracy = {}'.format(accurate_count/len(uexamples)))
        
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
