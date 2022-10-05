# Your names:
# Oori Schubert
# Wesley Gilpin

# no other modules allowed
import random,time,sys
import string #used for spell check


class Dictionary:
    def __init__(self,newDict='N/A'):
        self.__name = newDict
        if newDict == 'N/A':
            self.__words = []
        else: 
            try: 
                file = open(newDict, "r")
                self.__words = file.read().split()
            except:
                print("File " + newDict + " does not exist!")
                sys.exit(0)
        self.__size = len(self.__words)
        self.index=0
        self.steps=0
        self.rand = random.seed(8)
        self.__scoreList = [] #for scrabble game


    #### To complete
    def get_name(self):
        """Return the name of the dictionary"""
        return self.__name

    def get_size(self):
        """Return the size of the dictionary"""
        return self.__size
    
    def insert(self,word):
        """Insert a word into the dictionary"""
        self.__words.append(word)
        self.__size += 1
    
    def display(self,score=False):
        """Display the dictionary"""
        for i in range(len(self.__words)):
            if score:
                num = self.__scoreList[i]
            else:
                num = ''
            print(self.__words[i],str(num))
        
    def shuffle(self):
        t1 = time.process_time()
        """Shuffle the list of words"""
        for i in range(self.__size):
            j = random.randint(0,self.__size-1)
            temp = self.__words[i]
            self.__words[i] = self.__words[j]
            self.__words[j] = temp
        t2 = time.process_time()
        return t2-t1

    def get_index(self):
        """Return the index of the current word"""
        return self.index
    
    def get_steps(self):
        """Return the number of steps taken by the last search"""
        return self.steps

    def lsearch(self,word):
        """Linear search for word in the dictionary"""
        self.index = 0
        self.steps = 0
        print(self.__size)
        for i in range(self.__size):
            self.steps += 1
            if self.__words[i].lower() == word.lower():
                return True
        self.index = -1
        return False

    @staticmethod
    def searchList(word,list):
        """Search for a word in a list"""
        for i in range(len(list)):
            if list[i] == word:
                return True
        return False

    def bsearch(self,word):
        """Binary search for word in the dictionary"""
        self.steps = 0
        self.index = 0
        low = 0
        high = self.__size-1
        while low <= high:
            self.steps += 1
            self.index = self.steps-1
            mid = (low + high) // 2
            if self.__words[mid].lower() == word.lower():
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
        n=len(word)
        wordList = list(word)
        for out in range(n-1):
            imin=out
            for i in range(out+1,n):
                if wordList[i]<wordList[imin]:
                    imin=i
            temp=wordList[imin]
            wordList[imin]=wordList[out]
            wordList[out]=temp
        return "".join(wordList)
        
    def insertion_sort(self):
        """Sort the items list in place."""
        t1 = time.process_time() #capture time
        n = self.__size
        for out in range(1,n): #outer loop
            temp=self.__words[out] #save the value to be inserted
            i=out
            while i>0 and temp<self.__words[i-1]: #move items to the right
                self.__words[i]=self.__words[i-1] 
                i-=1
            self.__words[i]=temp #insert temp
        t2 = time.process_time() #capture time
        return t2-t1
    
    def enhanced_insertion_sort(self):
        """Sort the items list in place."""
        t1 = time.process_time()
        n = self.__size
        for out in range(1,n): #outer loop
            temp=self.__words[out] #save the value to be inserted
            i=out
            while i>0 and temp<self.__words[i-1]: #move items to the right
                low = 0
                high = i-1
                while low <= high:
                    mid = (low + high)//2
                    if temp < self.__words[mid]:
                        self.__words.insert(mid,temp) #fix this shit
                    elif temp > self.__words[mid]:
                        low = mid
        t2 = time.process_time()
        return t2-t1
        
    def save(self,name):
        """Save the dictionary to a file"""
        try:
            file = open(name, "w")
        except:
            print("File " + name + " does not exist!")
            sys.exit(0)
        for word in self.__words:
            file.write(word)
        file.close()

    def spell_check(self,filename):
        """Check the spelling of a text file"""
        punc=string.punctuation
        try:
            file = open(filename, "r")
        except:
            print("File " + filename + " does not exist!")
            sys.exit(0)
        for line in file:
            for word in line.split():
                cleanWord = word.lower().strip(punc)
                if not self.bsearch(cleanWord):
                    print("(" + word + ")",end=' ')
                else:
                    print(word,end=' ')
        file.close()
    
    def anagram(self,word):
        """Return a list of anagrams for a word"""
        anagrams = []
        for w in self.__words:
            if len(w) == len(word):
                if (self.sort_word(w) == self.sort_word(word)) and (not self.searchList(w,anagrams)): # and (w.lower() != word.lower())
                    anagrams.append(w.lower())
        return anagrams
    
    def compute_score_scrabble(self):
        """Compute the scrabble score for a word"""
        oneP = ["e","a","i","n","r","t","l","s","u"]
        twoP = ["d","g"]
        threeP = ["b","c","m","p"]
        fourP = ["f","h","v","w","y"]
        fiveP = ["k"]
        eightP = ["j","x"]
        tenP = ["q","z"]
        for word in self.__words:
            score = 0
            for letter in list(word):
                if Dictionary.searchList(letter,oneP):
                    score += 1
                elif Dictionary.searchList(letter,twoP):
                    score += 2
                elif Dictionary.searchList(letter,threeP):
                    score += 3
                elif Dictionary.searchList(letter,fourP):
                    score += 4
                elif Dictionary.searchList(letter,fiveP):
                    score += 5
                elif Dictionary.searchList(letter,eightP):
                    score += 8
                elif Dictionary.searchList(letter,tenP):
                    score += 10
            self.__scoreList.append(score)
    
    def score_sort(self):
        for out in range(self.__size):
            imin=out
            for i in range(out+1,self.__size):
                if self.__scoreList[i]<self.__scoreList[imin]:
                    imin=i
            temp=self.__scoreList[imin]
            self.__scoreList[imin]=self.__scoreList[out]
            self.__scoreList[out]=temp
            #repeat for words!
            temp1=self.__words[imin]
            self.__words[imin]=self.__words[out]
            self.__words[out]=temp1

    

    
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

    print("test...")
    if dict1.lsearch("scooped"):
        print("scooped is in the dictionary")
    else:
        print("scooped is not in the dictionary")

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
