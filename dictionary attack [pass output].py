import hashlib
import time
import random

dictionarywords=[]
dict_hash=[]
knownhash= '2b29c5739ec4158573c66d2124e2c7e9'


with open('dictionary.txt', 'r') as f:
    for line in f:
        word=line.strip('\n')
        dictionarywords.append(word)        
        hashpass = hashlib.md5(word.encode('utf8')).hexdigest()
        dict_hash.append(hashpass)

digits = ['0','1','2','3','4','5','6','7','8','9']
spchar= ['@', '#', '$', '%', '&']
possiblepass=[]

for word in dictionarywords:
        rand_digit1 = random.choice(digits)
        rand_digit2 = random.choice(digits)   
        rand_symbol1 = random.choice(spchar)
        rand_symbol2 = random.choice(spchar)
        temp_pass = rand_digit1 + rand_digit2 + word + rand_symbol1 + rand_symbol2
        possiblepass.append(temp_pass)
 

start = time.time()
for i in range(0,len(dict_hash)):
        if (dict_hash[i]==knownhash):
            print('Cracked Password: '+dictionarywords[i])
            stop = time.time()
            print('Time (Approx) taken for the first user: {:.2f} seconds'.format(stop - start))
