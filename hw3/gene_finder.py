# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    # YOUR IMPLEMENTATION HERE
    # This bit will chop off extra letters at end of a string
    dnaFixed = dna[0:(len(dna)- len(dna)%3)]
    
    #This section divides DNA input into list of 3-letter elements
    dnaCodons = []   
    i = 0
    while i < len(dnaFixed):
         dnaCodons.append(dna[i:i+3])
         i += 3
         
    
    
   
    
    
    #This will turn the codon list into amino acids 
    i = 0
    aminos = []
    for i in range (len(dnaCodons)):
        j = 0
        for j in range (len(codons)):
            k = 0
            for k in range (len(codons[j])):
                print codons[j][k]
                if dnaCodons[i] in codons[j]:
                    aminos.append(aa[j]) 
                    break
            
    delimiter = ''
    aminosString = delimiter.join(aminos)
    return aminosString
    
                     
                     
         
         
         

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    # YOUR IMPLEMENTATION HERE
    coding_strand_to_AA
    
    #put input and expected output here
    dnaInput = 'TCTTTTGGTTGGAA'
    expectedOutput = 'SFGW'
    
    actualOutput = coding_strand_to_AA(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + actualOutput
    



def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE
    
    backwards = dna[::-1]
    
    reverse = []
    for i in range (len(backwards)):
        if backwards[i] == 'A':
            reverse.append('T')
        if backwards[i] == 'T':
            reverse.append('A')
        if backwards[i] == 'G':
            reverse.append('C')
        if backwards[i] == 'C':
            reverse.append('G')
    
    delimiter = ''
    reverseOutput = delimiter.join(reverse)
    
    return reverseOutput   
            
        
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    # YOUR IMPLEMENTATION HERE    

    dnaInput = 'TCTTTTGGTTGG'
    expectedOutput = 'CCAACCAAAAGA'
    
    actualOutput = get_reverse_complement(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + actualOutput
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE

    dnaCodons = []   
    i = 0
    while i < len(dna):
         dnaCodons.append(dna[i:i+3])
         i += 3
         
    i = 0
    ORFOutput = []
    for i in range(len(dnaCodons)):
        if dnaCodons[i] == 'TAG':
            break
        elif dnaCodons[i] == 'TAA':
            break
        elif dnaCodons[i] == 'TGA':
            break
        ORFOutput.append(dnaCodons[i])
        
        
    delimiter = ''
    ORFStringOut = delimiter.join(ORFOutput)
    
    return ORFStringOut
   

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    # YOUR IMPLEMENTATION HERE
    dnaInput = 'ATGAGACGCTAGAAA'
    expectedOutput = 'ATGAGACGC'
    
    actualOutput = rest_of_ORF(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + actualOutput
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE        
   
    dnaCodons = []   
    i = 0
    while i < len(dna):
         dnaCodons.append(dna[i:i+3])
         i += 3
         
    #print 'Input dna string is ' + dna
    restOfORFOut = []
    oneFrameOut = []
    i = 0
    while i < (len(dnaCodons)):
        if dnaCodons[i] == 'ATG':
            #print 'Start codon detected. Beginning ORF reporting. :)'
            delimiter = ''
            inputToORF = delimiter.join(dnaCodons[i:len(dnaCodons)])
            restOfORFOut = rest_of_ORF(inputToORF)
            oneFrameOut.append(restOfORFOut)
            #print 'string to res_of_ORF = ' + inputToORF
            #print 'restoforfout' + restOfORFOut
            i += ((len(restOfORFOut))/3)
        else:
            i += 1
        #i +=1
        
        
            #print 'No start codon detected. Trying next codon.'
                    
    return oneFrameOut
        
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE
    #I introduced another start codon in the middle of an ORF to 
    #confirm that it won't sense that start codon
    dnaInput = 'GCGATGAGAATGCGCTAGAAAATGCGTTAGCG'
    expectedOutput = "['ATGAGACGC','ATGCGT']"
    
    actualOutput = find_all_ORFs_oneframe(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + str(actualOutput)
    #This works
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE

    findAllORFsOutput = []
    
    findAllORFsOutput.extend(find_all_ORFs_oneframe(dna))
    
    findAllORFsOutput.extend(find_all_ORFs_oneframe(dna[1:]))
    
    findAllORFsOutput.extend(find_all_ORFs_oneframe(dna[2:]))
    
    return findAllORFsOutput

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    # YOUR IMPLEMENTATION HERE
    
    dnaInput = 'ATGCATGCCTAGGTAG'
    expectedOutput = "['ATGCATGCC','ATGCCTAGG']"
    
    actualOutput = find_all_ORFs(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + str(actualOutput)
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    # YOUR IMPLEMENTATION HERE
    bothStrandsOut = []
    
    bothStrandsOut.extend(find_all_ORFs(dna))
    
    dnaReverse = get_reverse_complement(dna)
    
    bothStrandsOut.extend(find_all_ORFs(dnaReverse))
    
    return bothStrandsOut
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

    dnaInput = 'ATGCGAATGTAGCATCAAA'
    expectedOutput = "['ATGCGAATG', 'ATGCTACATTCGCAT']"
    
    actualOutput = find_all_ORFs_both_strands(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + str(actualOutput)

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE
    if (len(find_all_ORFs_both_strands(dna)))>2:
        return max(find_all_ORFs_both_strands(dna), key=len)
    else:
        return 'No ORFS found'
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

    dnaInput = 'ATGCGAATGTAGCATCAAA'
    expectedOutput = "ATGCTACATTCGCAT"
    
    actualOutput = longest_ORF(dnaInput)
    

    print 'input: ' + dnaInput
    print 'expected output: ' + expectedOutput
    print 'actual output: ' + str(actualOutput)
    
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE
    import random
    i = 0
    dnaList = []
    while i < len(dna):
            dnaList.append(dna[i:i+1])
            i += 1
    
    i = 0
    
    shuffledLongest = []
    for i in range(num_trials):
        random.shuffle(dnaList)
#        print 'dna list  '
#        print dnaList
        dnaString = (collapse(dnaList))
        #print 'dna string  ' + dnaString
        dnaLong= longest_ORF(dnaString)
        #print 'Dna from longest_ORF ' + dnaLong
        shuffledLongest.append(dnaLong)
#        print shuffledLongest
        print i
#    print shuffledLongest
    print (len(max(shuffledLongest, key=len)))
        
        
        
    

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE
    dnaSequences = []
    allORFList = find_all_ORFs_both_strands(dna)
    print allORFList
    minLength = threshold
    print minLength
    i = 0
    for i in range (len(allORFList)):
        if len(allORFList[i])>minLength:
            dnaSequences.append(allORFList[i])
        else:
            print 'ORF not sufficiently long'
        print i
    i=0
    aminosList = []
    for i in range (len(dnaSequences)):
        aminosStrand = coding_strand_to_AA(dnaSequences[i])
        aminosList.append(aminosStrand)
       
        
    return aminosList
        
    
