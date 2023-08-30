'''maximal_repeats.py'''
import sys 
#Fonction pour lire une séquence au fichier fasta

def readfasta(file):
    """
    Parameters
    ----------
    file : a fasta file
        
    Returns 
    -------
    
    The sequence contained in the file : string
    """
    with open(file,"r") as filin:
        seq=''
        lines=filin.readlines()
        for i in lines: 
            if '>' not in i :
                seq=seq+i
                seq=seq.rstrip()

            else : 
                i=''
    return seq

def occurences(file,k):
    """
    Parameters
    ----------
    file :file
    k: int
        
    Returns
    -------
    
    A dictionnary with all the words and the number of their occurences
    """
    dic = {}
    f1=readfasta(file)
    for i in range(len(f1)-k+1):
        motif=f1[i:i+k]
        if motif not in dic.keys():
            dic[motif]=1 
        dic[motif]+=1
    return dic

def sort(file,k):
    """
    Parameters
    ----------
    file : a fasta file
    k: int
        
    Returns
    -------
    
    A list of the words with a number of occurrences superior to 1
    """
    dictio=occurences(file,k)
    mots=[]
    for motif in dictio.keys():
        if dictio[motif]> 1 :
            mots.append(motif)
    return mots    
    
def get_positions_word(file,word):
    """
    Parameters
    ----------
    file : a fasta file
    word : the pattern
        
    Returns
    -------
    a list with the positions of the word
    """
    liste=[]
    f2=readfasta(file)
    i=0
    for i in range(len(f2)-1):
            if word in f2[i:i+len(word)] :
                liste.append(i)
    return liste

def get_nt_bef(file,word):
    """
    Parameters
    ----------
    file : a fasta file
    word : the pattern
        
    Returns
    -------
    
    a list with the nucleotide before the word
    """
    f2=readfasta(file)
    nt_bef=[]
    for i in range(len(f2)-1):
        if f2[i:i+len(word)] == word:
            if i == 0:
                before='None'
                nt_bef.append(before)
            else :
                before = f2[i-1]
                nt_bef.append(before)
            
                
    return nt_bef
    



def get_nt_after(file,word):
    """
    Parameters
    ----------
    file : a fasta file
    word : the pattern 
        
        
    Returns
    -------
    
    a list with the nucleotide after the word
    """
        
       
    f2=readfasta(file)
    nt_aft=[]
    for i in range(len(f2)):
        if f2[i:i+len(word)]== word:
            if i == len(f2)-len(word):
                after='None'
                nt_aft.append(after)
            else :
                after =f2[i+len(word):i+len(word)+1]
                nt_aft.append(after)
            #print(pos_aft)
            
    return nt_aft

def full_position(file,word):
	ok=get_positions_word(file,word)
	aft=get_nt_after(file,word)
	bef=get_nt_bef(file,word)
	o=[]
	for i in range(len(ok)): 
    	#Add to the list o the position and the tuple containing the nucleotide before and after
         t = word, ok[i] , (bef[i],aft[i])
         o.append(t)
	return o

def all_words(file,k):
    dictio=sort(file,k)
    z=[]
    for element in dictio:
        p=full_position(file,element)
        z.append(p)
    return z

def maximal_repeats(file,k):
	
    z=all_words(file,k)
    i_motif=0
    i_pos=0
    mp=[]
    max_rep = False
    #For each indice of our list obtained with all_words, compare the element before and the element after
    #If the element respect our condition, it will be add to our list of maximal repeats
    for i_motif in range(len(z)-1):
        for i_pos in range(len(z[i_motif])-1):
            if z[i_motif][i_pos][-1][0] != z[i_motif][i_pos+1][-1][0]:
                if z[i_motif][i_pos][-1][1] != z[i_motif][i_pos+1][-1][1]:
                    max_rep=True
        if max_rep is True:     
            mp += z[i_motif]
            max_rep=False
           
    return mp


#Main Program

if __name__ == "__main__":
    #sys.exit("il faut deux ou trois arguments")
    if len(sys.argv)<2:
        sys.exit("You need at least two arguments. Try again ")

    elif len(sys.argv)==2:
        #répétitions de taille supérieure à 20 qui sont recherchées.
        file=sys.argv[1]
        seq=readfasta(file)
        for i in list(range(20, len(seq)-1)):
            out1=maximal_repeats(file,i)
            if out1 != []:
                print("{} {}".format(out1[0][0],len(out1[0][0])))
                for p in list(range(0,len(out1))):
                    print("{} {} ".format(out1[p][1],out1[p][2]))

    elif len(sys.argv)==3:
    	#répétitions de taille > sys.argv[2]
        file=sys.argv[1]
        seq=readfasta(file)
        k=sys.argv[2]
        k=int(k)
        for i in list(range(k,len(seq))):
            out2=maximal_repeats(file,i)
            if out2 != []:
                print("{} {}".format(out2[0][0],len(out2[0][0])))
                for p in list(range(0,len(out2))):
                    print("{} {} ".format(out2[p][1],out2[p][2]))

    elif len(sys.argv)==4:
    	#répétitions de taille comprises entre sys.argv[2] et sys.argv[3]
        file=sys.argv[1]
        k=sys.argv[2]
        k=int(k)
        p=sys.argv[3]
        p=int(p)
        for i in list(range(k,p)):
            out3=maximal_repeats(file,i)
            if out3 != []:
            	#Format d'affichage similaire
                print("{} {}".format(out3[0][0],len(out3[0][0])))
                for p in list(range(0,len(out3))):
                    print("{} {} ".format(out3[p][1],out3[p][2]))


