# Jacob DeNell
# Project #7
# April-27-2018
def verify_subseq(seq, subseq):
    j = 0
    i = 0   
    # Loops and makes sure every item in the subseq is in the seq in order.
    while j < len(subseq) and i < len(seq):
        if subseq[j] == seq[i]:  
            j = j + 1
            
        i = i + 1

    return j == (len(subseq))

def verify_increasing(seq):
    if not seq:
        return True
        
    small = seq[0]
    # Makes sure every item in the subseq is in bigger than the last.
    for i in seq[1:]:
        if i < small or i == small:
            return False
        small = i
    
    return True

def find_lis(seq):
    L = 1
    M = [0]   
    P = [-1]
    # Loops through every item in the sequence.
    for i in range(1,len(seq)):
        
        j = -1
        start = 0
        end = L - 1
        going = True
        
        while going:
            if (start == end):
                if (seq[M[start]] < seq[i]):
                    j = start
                going = False
                
            else:
                partition = 1 + ((end - start - 1) // 2)
                if (seq[M[start + partition]] < seq[i]):
                    start += partition
                    j = start
                else:
                    end = start + partition - 1
        # Appends the value if j is the next index.
        if (j >= 0):
            P.append(M[j])
        else:
            P.append(-1)
        j += 1
        
        if (j == L):
            M.append(i)
            L += 1
            
        if (seq[i] < seq[M[j]]):
            M[j] = i

    result = []
    index = M[L - 1]

    while (index >= 0):
        result.append(seq[index])
        index = P[index]

    # Returns the list in increasing order.
    return result[::-1]
            
            
        
