"""
This file runs a very simple simulation to compare the upper bound generated by using the method found in Open-World Probabilistic Databases (Ceylan et. Al, 2016) with a method which uses summary statistics.

"""

import sys
import math
from random import uniform 

def generate_tables(s1=10, s2=1000, s3=100, lam=0.7):
    t1 = {x: uniform(lam, 1) for x in xrange(s1)}
    t2 = {x: uniform(lam, 1) for x in xrange(s1, s1+s2)}
    t3 = {x: uniform(lam, 1) for x in xrange(s1+s2, s1+s2+s3)}
    return t1, t2, t3

def main():
    LiS, LiLA, S = generate_tables()
    d = 2000
    LiS_dist = 15 - sum(LiS.itervalues())
    LiLA_dist = 1100 - sum(LiLA.itervalues())
    S_dist = 150 - sum(S.itervalues())
    print compute_open_prob(LiS, S)
    print compute_open_prob(LiLA, S)
    print compute_completed_prob(LiS, LiS_dist, S, S_dist)
    print compute_completed_prob(LiLA, LiLA_dist, S, S_dist)


def compute_open_prob(t1, t2, lam=0.7, d=2000):
    # very important: assumes they're mutually exclusive
    inv_log_prob = 0
    inv_log_prob += sum(math.log10(1.0-x*lam) for x in t1.itervalues())
    inv_log_prob += sum(math.log10(1.0-x*lam) for x in t2.itervalues())
    inv_log_prob += (float)(d-len(t1)-len(t2)) * math.log10(lam * lam)
    print inv_log_prob
    return 1.0 - math.pow(10, inv_log_prob)

def compute_completed_prob(t1, m1, t2, m2, lam=0.7, d=2000):
    # Still assumes they're mutually excluse, but now also uses the "distribution" amount given
    inv_log_prob = 0
    t1_vals = sorted(t1.values(),reverse=True)
    t2_vals = sorted(t2.values(),reverse=True)
    for x in t1_vals:
        inv_log_prob += math.log10(1.0-x*min(lam, m2))
        m2 -= min(lam,m2)
        if m2 <= 0:
            break
    
    for x in t2_vals:
        inv_log_prob += math.log10(1.0-x*min(lam,m1))
        m1 -= min(lam, m1)
        if m1 <= 0:
            break

    extra = min(m1, m2)
    inv_log_prob += (float)(math.floor(extra/lam)) * math.log(1.0 - lam*lam)
    print inv_log_prob
    return 1.0 - math.pow(10, inv_log_prob)

if __name__ == '__main__':
    sys.exit(main())
