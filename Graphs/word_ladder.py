# The main goal of this function is to find the word which is present in the word list in least number no of steps
# The function takes arguments startword, endWord, wordList

def word_ladder(startword,endWord,wordList):
    wordSet = set(wordList)
    if endWord not in wordList:
        return 0
    length = 1
    queue = [(startword,length)]
    while queue is not None:
        word,length = queue.pop(0)
        if word == endWord:
            return length
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for c in alphabets:
                generated = word[:i] + c + word[i+1:]
                if generated in wordSet:
                    wordSet.remove(generated)
                    queue.append((generated,length+1))
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(word_ladder(beginWord,endWord,wordList))