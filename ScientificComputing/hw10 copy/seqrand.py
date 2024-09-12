##############################################
# module: seqrand.py
# description: tests of sequence randomness
# YOUR NAME: Paige Davidson
# YOUR A#: A023394245
# --------------------------------------------
# bugs to vladimir kulyukin in canvas.
##############################################

from prng import prng
import scipy.stats
import random

def get_transcendental_str(fp):
    with open(fp, 'r') as infs:
        _str = infs.readline()
        return ''.join([c for c in list(_str.strip()) if c != ' '])
    
def get_mantissa(fp):
    return get_transcendental_str(fp)[2:]

def chisquare_str_digit_seq(str_digit_seq, seq_start=0, seq_end=10):
    assert 0 <= seq_start < seq_end <= len(str_digit_seq)
    ### takes a string of digits str_digit_seq and returns the χ2 statistic V and its p-value 
    # of the substring that starts at position seq_start and ends at position seq_end-1 in str_digit_seq.

    substring = str_digit_seq[seq_start:seq_end]
    sublen = len(substring)
    Y_counts = [substring.count(str(d)) for d in range (10)]
    E_counts = [sublen*0.1 for _ in range(10)]
    v, pv = scipy.stats.chisquare(Y_counts, E_counts)

    return v, pv

def chisquare_mersenne_twister(pval_lower=0.1,
                               pval_upper=0.9,
                               seq_len=10, num_experiments=10):

    rand_seq_count = 0
    
    for _ in range(num_experiments):
        # Generate a new random sequence for each experiment
        mers_seq = prng.mersenne_twister(seq_len, lower=0, upper=9)()
        exp = [str(next(mers_seq)) for _ in range(seq_len)]
        
        v, pv = chisquare_str_digit_seq(exp, 0, len(exp))
        
        if pval_lower <= pv <= pval_upper:
            rand_seq_count += 1

    return rand_seq_count, rand_seq_count / num_experiments
        
        
