# Your names:
# Oori Schubert
# Wesley Gilpin

# no other modules allowed
import random,time,sys


class Dictionary:
    def __init__(self,newDict):
        self.__name = newDict
        self.__words = []
        if newDict == None:
            self.__name = 'N/A'
        else: 
            try: 
                file = open(newDict, "r")
                self.__words = list(file)
            except:
                print("File " + newDict + " does not exist!")
                sys.exit(0)
        self.__size = len(self.__words)
        self.index=0
        self.steps=0
        self.rand = random.seed(8) 


    #### To complete
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size
    
    def insert(self,word):
        """Insert a word into the dictionary"""
        self.__words.append(word)
        self.__size += 1
    
    def display(self):
        """Display the dictionary"""
        print(self.__words)
    
    def shuffle(self):
        for i in range(self.__size):
            j = random.randint(0,self.__size-1)
            temp = self.__words[i]
            self.__words[i] = self.__words[j]
            self.__words[j] = temp
    
    def lsearch(self,word):
        """Linear search for word in the dictionary"""
        self.steps = 0
        for i in range(self.__size):
            self.steps += 1
            if self.__words[i] == word:
                return True
        return False

    def bsearch(self,word):
        """Binary search for word in the dictionary"""
        self.steps = 0
        low = 0
        high = self.__size-1
        while low <= high:
            self.steps += 1
            mid = (low + high) // 2
            if self.__words[mid] == word:
                return True
            elif self.__words[mid] < word:
                low = mid + 1
            else:
                high = mid - 1
        return False


    def get_random_list(self,length):
        """Return a list of random words from the dictionary"""
        #return random.sample(self.__words, 20)
        return random.sample(self.__words, length)

    def selection_sort(self):    #provided to you
        """Perfom selection sort, must return the time it takes to sort the list of words
        Remark: Routine works 'in-place'"""
        t1 = time.process_time() #capture time
        n=self.get_size()
        for out in range(n-1):        #outer loop
            #find minimum between out+1 and n-1
            imin=out
            for i in range(out+1,n):  #inner loop
                if self.__words[i]<self.__words[imin]: 
                    imin=i #update  minimum index
            #swap (3 step here)
            temp=self.__words[imin]
            self.__words[imin]=self.__words[out]
            self.__words[out]=temp
        t2 = time.process_time() #capture time
        return t2-t1
        


    
    @staticmethod  # provided to you
    def get_word_combination(word, combs=['']):
        """ return a list that contains all the letter combinations (all length) of the input 'word' """
        if len(word) == 0:
            return combs
        head, tail = word[0], word[1:]
        combs = combs + list(map(lambda x: x+head, combs))
        return Dictionary.get_word_combination(tail, combs)

    

    @staticmethod
    def sort_word(word):  # to complete
        """ must return a string with letters included in 'word' that are now sorted"""
        return ''.join(sorted(word)) #Work on this!





    

    
########################################################################
########################################################################


def main():

    ### step-1 test constructor
    name=input("Enter dictionary name (from file 'name'.txt): ")    
    dict1=Dictionary(name+".txt")

    ### step-2 test get_name, get_size, get_random_list        
    print('Name first dictionary:',dict1.get_name())   
    print('Size first dictionary:',dict1.get_size()) 
    print("Five random words:",end=" ")
    rlist=dict1.get_random_list(5) # 5 means the number of random words we want
    for w in rlist: print(w,end=" ")
    print("\n")

    ### step-3 test constructor again
    dict2=Dictionary()
    print('Name second dictionary:',dict2.get_name())
    
    ### step-4 test insert and display
    for w in rlist: dict2.insert(w)
    print('Display second dictionary:')
    dict2.display()

    ### step-5 test shuffle 
    t=dict2.shuffle()
    print('\nSecond dictionary shuffled in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()

    ### step-6 test linear search
    word="morning"
    print("\nLinear search for the word '%s' in second dictionary"%word)
    status=dict2.lsearch(word)
    print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))

    ### sort second using selection sort (provided to you)
    t=dict2.selection_sort()
    print('\nSecond dictionary sorted in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()

    ### step-7 test binary search (find it)
    word="morning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("Is '%s' found: %s at index %s"%(word,status,dict2.get_index()))

    # binary search (did no find it)
    word="ning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("'%s' is not found so it must be inserted at index %s"%(word,dict2.get_index()))
    

    


## call the main function if this file is directly executed
if __name__=="__main__":
    main()
