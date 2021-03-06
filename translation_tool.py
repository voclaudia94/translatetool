#!/usr/bin/env python
# coding: utf-8

import argparse

class ORFerror(Exception):
    #create custom error if ATG is not encountered in the sequence.
    pass

def translate_tool1(sequence):
    """This function takes a dna sequence as the input and translates it into an amino acid sequence"""
    
    codon_table={"ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
                 "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
                 "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
                 "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
                 "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
                 "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
                 "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
                 "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
                 "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
                 "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
                 "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
                 "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
                 "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
                 "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
                 "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
                 "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"}
    protein=""

    sequence=sequence.upper()
    #first, find ATG position to start the translation
    start=sequence.find("ATG") 
    
    if start<0: #if ATG is not found in the sequence, start = -1
        raise ORFerror
    
    #iterate from the start codon until the end
    for i in range(start,len(sequence),3):
        if codon_table[sequence[i:i+3]]=="*": #when iteration encounters a stop codon, translation ends.
            break
        protein+=codon_table[sequence[i:i+3]]
    return print("The amino acid sequence is: {}".format(protein))


#initiate the parser
parser=argparse.ArgumentParser()

#-i as the input argument
parser.add_argument("-i",type=str,required=True)
args = parser.parse_args()
user_input = args.i

try:
    if user_input.isalpha():
        translate_tool1(user_input)
    else:
        raise TypeError
except ORFerror:
    print("The sequence is not in the open reading frame.")
except KeyError:
    print("One of the codons does not translate into a protein. Please check if a nucleotide is missing") 
except TypeError:
    print("Input must be alphabetic characters, specifically DNA nucleotides.")



