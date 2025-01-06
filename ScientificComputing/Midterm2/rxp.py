##############################################
# module: rxp.py
# description: Richardson Extrapolation
# for differentiation and integration.
# It implements 2nd richardson (r2) computed
# as AV_2n + (AV_2n - AV_n)/3.0. Higher
# order richardsons can be added as needed.
# -----------------------------------------
# bugs to vladimir kulyukin in canvas.
##############################################

class rxp(object):

    @staticmethod
    def r2(av_2n, av_n):
        """
        Richardson Extrapolation computed as
        AV_2n = AV_2n + (AV_2n - AV_n)/3.0.
        See Slide 7 in Lecture 13 (RE in Differentiation)
        and Slide 10 in Lecture 14 (RE in Integration).
        """
        return av_2n + (av_2n - av_n)/3.0

    

    

    
        
    
