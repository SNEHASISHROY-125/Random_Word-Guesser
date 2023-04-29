import random
import sys

word_list = ['appple' , 'bot' ,'cat' , 'python']
empty_list = []
chosen_word = random.choice(word_list).lower()

for x in range(len(chosen_word)):
    empty_list += '_'

print(chosen_word)
print(empty_list)

correct = '''
✅
'''
wrong = '''
❌
'''

for i in chosen_word:
    user_ch =input('Choose a Letter : ').lower()
    if user_ch in chosen_word:
#        empty_list += user_ch
#        empty_list.insert(chosen_word.index(i),user_ch)        
        empty_list[chosen_word.index(i)] = user_ch
        print(f'{empty_list}{correct} ')
    else:
        print(f'{empty_list} {wrong} ')        
#    print(f'{empty_list}{correct} ')
'''
    if not '_' in empty_list:
        sys.exit(0)
'''         