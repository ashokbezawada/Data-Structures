pad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrx',
    '8': 'tuv',
    '9': 'wxyz'
}



def WordsHelper(digits, word):
  
  letters = pad[digits[0]]    
  if len(digits) == 1:
    for letter in letters:
      print(word + letter) 
  else:
   for letter in letters:                     
     WordsHelper(digits[1:], word+letter)         

def GenerateWords(digits):
  WordsHelper(digits, '')
    

GenerateWords('228')   