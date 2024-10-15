strs = ["eat","tea","tan","ate","nat","bat"]

def GroupAnagrams(strs):
        
    wordDict = {}

    for word in strs:

        sorted_word = ''.join(sorted(word))

        if sorted_word not in wordDict:

            wordDict[sorted_word] = []
        
        wordDict[sorted_word].append(word)
    

    return list(wordDict.values())

        




if __name__ == "__main__":
    print(GroupAnagrams(strs))