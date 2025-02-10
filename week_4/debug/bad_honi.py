'''
HONI block

Consider a series of four consecutive letters of some word that make up the 
subword HONI (case sensitive) is called the HONI-block. 

Given a string by the user, throw out as many letters as you want (it might be
none), so that in the end there are as many HONI-blocks as possible in the word.  

upgrade to: 
--> where HONI-block is not case sensitive.  
--> let user provide any sub-block
'''


word = input("test pls:").lower()
sub_block = 'HONI'.lower()            
block_count = 0 
i = j = 0  

for i in word:
    if i == sub_block[j]:   
        j = (j + 1) % len(sub_block);              
        if j == len(sub_block) - 1:                
            block_count += 1   
print(f'number of HONI-blocks: {block_count}')