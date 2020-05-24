class Solution(object):  
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        if not sentence:
            return -1
        s = sentence.split()
        s_n = len(s)
        for i in range(0, s_n):
            a = 1
            n2 = len(searchWord)
            while(i<s_n):
                temp = s[i]
                n1 = len(temp)
                if n2 > n1:
                    i += 1
                else:
                    for k in range(0, n2):
                        if temp[k] != searchWord[k]:
                            a = 0
                    if a == 1:
                        return i+1
                    else:
                        i += 1                  
        return -1
       
                    
                

        
