__author__ = 'regrant'

# import difflib
#
# t_list = ["ICR1_CBS2 M", "ICR1_CBS2 UM", "ICR2 M", "ICR2 UM"]
#
# s = difflib.SequenceMatcher(lambda x: x==" ", t_list[0], t_list[1])
# print s.find_longest_match(0, len(t_list[0]), 0, len(t_list[1]))

def phred_to_prob(phred_score):
    return 10 ** -(phred_score/10)

# print phred_to_prob(39.2) > float(1/10000)

example = "AAA,A, Tx"
print len(example.split(","))