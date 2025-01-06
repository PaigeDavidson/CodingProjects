import csv
import math
import copy

##################################################
# module: bin_id3.py
# description: Binary ID3 decision tree learning
# -----------------------------------------------
# YOUR NAME: Paige Davidson
# YOUR A#: A02339425
#
# ------------------------------------------------
# bugs to vladimir kulyukin in canvas.
###################################################

### Positive and Negative Constant labels; don't change
### these.
PLUS  = 'Yes'
MINUS = 'No'

class id3_node(object):

    def __init__(self, lbl):
        self.__label = lbl
        self.__children = {}

    def set_label(self, lbl):
        self.__label = lbl
        
    def add_child(self, attrib_val, node):
        self.__children[attrib_val] = node

    def get_label(self):
        return self.__label

    def get_children(self):
        return self.__children

    def get_child(self, attrib_val):
        assert attrib_val in self.__children
        return self.__children[attrib_val]

class bin_id3(object):

    @staticmethod
    def get_attrib_values(a, kvt):
        """
        Looks up values of attribute a in key-value table.
        """
        return kvt[a]

    @staticmethod
    def get_example_attrib_val(example, attrib):
        """
        Get the value of attribute attrib in example.
        """
        assert attrib in example
        return example[attrib]

    @staticmethod
    def parse_csv_file_into_examples(csv_fp):
        """
        Takes a csv file specified by the path csv_fp and
        converts it into an array of examples, each of which
        is a dictionary of key-value pairs where keys are
        column names and the values are column attributes.
        """
        examples = []
        with open(csv_fp) as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            key_names  = None
            for row in csv_reader:
                if len(row) == 0:
                    continue
                if line_count == 0:
                    key_names = row
                    for i in range(len(key_names)):
                        ## strip whitespace on both ends.
                        row[i] = row[i].strip()
                        line_count += 1
                else:
                    ex = {}
                    for i, k in enumerate(key_names):
                        ## strip white spaces on both ends.
                        ex[k] = row[i].strip()
                    examples.append(ex)
            return examples, key_names

    @staticmethod
    def construct_attrib_values_from_examples(examples, attributes):
        """
        Constructs a string-to-set-of-strings dictionary from a list 
        of examples; each attribute is mapped to a set of all its 
        possible values found in examples.
        """
        avt = {} ## attibute-value table, a dictionary
        for a in attributes:
            if not a in avt:
                avt[a] = set()
            for ex in examples:
                if a in ex:
                    if not ex[a] in avt[a]:
                        avt[a].add(ex[a])
                else:
                    avt[a].add(None)
        return avt

    @staticmethod
    def find_examples_given_attrib_val(examples, attrib, val):
        """
        Finds all examples in such that attrib = val.
        """
        rslt = []
        #print('Looking for examples where {}={}'.format(attrib, val))
        for ex in examples:
            if attrib in ex:
                if ex[attrib] == val:
                    rslt.append(ex)
        return rslt

    @staticmethod
    def find_most_common_attrib_val(examples, attrib, avt):
        """
        Finds the most common value of attribute attrib in examples.
        """
        attrib_vals = bin_id3.get_attrib_values(attrib, avt)
        val_counts = {}
        for av in attrib_vals:
            SV = bin_id3.find_examples_given_attrib_val(examples, attrib, av)
            val_counts[av] = len(SV)
        max_cnt = 0
        max_val = None
        #print('val_counts = {}'.format(val_counts))
        for val, cnt in val_counts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_val = val
        assert max_val != None
        return max_val, max_cnt

    @staticmethod
    def get_non_target_attributes(target_attrib, attribs):
        """
        Returns a comma separated string of all attributes in the list attribs that
        that are not equal to target_attrib; 
        - target_attrib is a string.
        - attribs is a list of strings.
        """
        return ', '.join([a for a in attribs if a != target_attrib])

    @staticmethod
    def display_info_gains(gains):
        """
        Displays a dictionary of information gains in the format attribute: gain.
        """
        print('Information gains are as follows:')
        for attrib, gain in gains.items():
            print('\t{}: {}'.format(attrib, gain))

    @staticmethod
    def display_id3_node(node, tabs):
        """
        Displays the subtree rooted at a node.
        """
        print(tabs + '{}'.format(node.get_label()))
        children = node.get_children()
        for v, n in children.items():
            print(tabs + '\t{}'.format(v))
            bin_id3.display_id3_node(n, tabs+'\t\t')

    ## HW11
    @staticmethod
    def proportion(examples, attrib, val):
        """
        Computes the proportion of examples whose attribute attrib has the value val.
        """
        totalex = len(examples)

        count = 0
        for i in examples:
            for a in i:
                if a == attrib and i[a] == val:
                    count += 1

        return count / totalex

    ## HW11
    @staticmethod
    def entropy(examples, attrib, avt):
        """
        Computes entropy of examples with respect of attribute attrib.
        avt is the attribute value table computed by construct_attrib_values_from_examples().
        """
        h = 0
        
        for i in avt[attrib]: 
            # pi is the proporition of the examples for which A = vi 
            p = bin_id3.proportion(examples=examples, attrib=attrib, val=i)
            if p != 0:
                h -= p * math.log2(p)

        return h

    ## HW11    
    @staticmethod
    def gain(examples, target_attrib, attrib, avt):
        """
        Computes gain of the attribute attrib in examples.
        """
        # Calculate H(S, T)
        hST = bin_id3.entropy(examples, target_attrib, avt)

        # Get the number of elements of the set of examples for which A = v
        Sav = [example for example in examples if example[attrib] in avt[attrib]]
        sLen = len(Sav)

        # Perform calculation to get gain
        gain = 0

        for v in avt[attrib]:
            # Filter examples where attribute A = v
            Sv = [example for example in Sav if example[attrib] == v]
            SvLen = len(Sv)

            # Skip if Sv is empty
            if SvLen == 0:
                continue

            # Calculate H(SA=v, T)
            hSAvT = bin_id3.entropy(Sv, target_attrib, avt)

            # Update gain
            gain += (SvLen / sLen) * hSAvT
        return hST - gain

    ## HW11    
    @staticmethod
    def find_best_attribute(examples, target_attrib, attribs, avt):
        """
        Finds the attribute in attribs with the highest information gain.
        Break ties arbitrarily.
        """
        best_attribute = ""  
        best_gain = 0.0  
        gains = {}

        # Calculate the gain for each attribute in the attribs list
        for attribute in attribs:
            if(attribute == target_attrib):
                continue
            else:
                gain = bin_id3.gain(examples, target_attrib, attribute, avt)

                gains[attribute] = gain

                # If the current gain is higher than the best gain so far, update best_gain and best_attribute
                if gain > best_gain:
                    best_gain = gain
                    best_attribute = attribute

        return best_attribute, best_gain, gains



    ## HW11    
    @staticmethod
    def fit(examples, target_attrib, attribs, avt, dbg):
        """
        Returns the root of a decision tree from examples given target_attribute target_attrib,
        attributes attribs, and attribute-value table.
        - examples is a list of examples (list of dictionaries);
        - target_attrib is a string (e.g., 'PlayTennis')
        - attribs is a list of attributes (strings)
        - avt is a dictionary constructed by construct_attrib_values_from_examples()
        - dbg is a debug flag True/False. When it is true, then things should
          be printed out as the algorithm computes the decision tree. For example,
          in my implementation I have things like
          if len(SV) == len(examples):
            ## if all examples are positive, then return the root node whose label is PLUS.
            if dbg == True:
                print('All examples positive...')
                print('Setting label of root to {}'.format(PLUS))
            root.set_label(PLUS)
            return root
        """
        # A call to fit() returns the id3_node object that is the root of a decision tree fit on a given dataset of examples.
        global PLUS
        global MINUS

        # 1. create a root node
        root = id3_node("Root")

        # 2. find all examples in Examples where the value of TargetAttrib is PLUS (positive/Yes)
        PosExamples = bin_id3.find_examples_given_attrib_val(examples, target_attrib, PLUS)
        # 3. if entropy is zero return the root
        if len(examples) == len(PosExamples):
            if dbg == True:
                print("All examples positive...")
                print("Setting label of root to {}".format(PLUS))
            root.set_label(PLUS)
            return root
        
        # 4. find all examples in Examples where the value of TargetAttrib is MINUS (negative/No)
        NegExamples = bin_id3.find_examples_given_attrib_val(examples, target_attrib, MINUS)
        # 5. if all examples are negative, then set the label of the root node to MINUS and return the root node (entropy is 0)
        if len(examples) == len(NegExamples):
            if dbg == True:
                print("All examples negative...")
                print("Setting label of root to {}".format(MINUS))
            root.set_label(MINUS)
            return root
        
        # 6. If there are no more non-target attributes (i.e., number of attributes in Attributes is 0), 
        # then set the label of the root node to the most common value of TargetAttrib in Examples
        # and return the root node
        commonVal = bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)
        if len(attribs) == 0:
            root.set_label(commonVal)
            return root
        
        # 7. Find best attribute (best_attrib) and its information gain (best_gain) among the attributes in Attributes 
        # and set the root’s label to best_attrib
        best_attrib, best_gain, gains = bin_id3.find_best_attribute(examples, target_attrib, attribs, avt)
        if dbg == True:
            print("Looking for best attribute among Humidity, Outlook, Wind, Temperature...")
            print("Information gains are as follows:")
            print(gains)
            print('Best Attribute = {}'.format(best_attrib) + "with a gain of {}".format(best_gain))
        root.set_label(best_attrib)

        # 8.for each value bav of best_attrib
        for bav in avt[best_attrib]:
            split_examples = bin_id3.find_examples_given_attrib_val(examples, best_attrib, bav)
            if len(split_examples) == 0:
                lbl = bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)
                child_node = id3_node(lbl)
                root.add_child(bav, child_node)
            else:
                copy_attribs = copy.copy(attribs)
                if dbg == True:
                    print("Removing {} from list of attributes...".format(best_attrib))
                copy_attribs.remove(best_attrib)       
                child_node = bin_id3.fit(split_examples, target_attrib, copy_attribs, avt, dbg)
                root.add_child(bav, child_node)

        return root


    ## HW11            
    @staticmethod
    def predict(root, example):
        """
        Classifies an example given a decision tree whose root is root.
        """
        global PLUS
        global MINUS
        """
        predict(root, example)
        IF the root’s label is PLUS
            THEN return PLUS
        IF the root’s label is MINUS
            THEN return MINUS
        Let RAT be the root’s label.
        Let RAV be the value of RAT in example.
        Let CH be the root’s child connected to the root on the link RAV.
        Return predict(CH, example)

        You can use bin_id3.get_example_attrib_val to 
        compute RAV and id3_node.get_child to get CH connected to the root on RAV.
        """
        if(root.get_label() == PLUS):
            return PLUS
        elif(root.get_label() == MINUS):
            return MINUS
        
        RAT = root.get_label()
        RAV = bin_id3.get_example_attrib_val(example, RAT)
        CH = root.get_child(RAV)

        return bin_id3.predict(CH, example)

        
