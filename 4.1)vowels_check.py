#program to check the vowels in a word
word=input('Enter a word: ')
length=int(len(word))
for i in range(length):
     if(word[i]=='a')or(word[i]=='e')or(word[i]=='i')or(word[i]=='o')or(word[i]=='u'):
         print('vowel at index{} is {}'.format(i,word[i]))
