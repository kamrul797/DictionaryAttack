import hashlib
import time

# using any password hash from the given list

dictionarywords=[]
dict_hash=[]
passlist=[]
targethash="2b29c5739ec4158573c66d2124e2c7e9"
usernames=[] 

with open('dictionary.txt', 'r') as f:
    for line in f:
        word=line.strip('\n')
        dictionarywords.append(word)        
        hashpass = hashlib.md5(word.encode('utf8')).hexdigest()
        dict_hash.append(hashpass)
      
with open('accountfile.txt', 'r') as f:
    for line in f:
        as_list = line.split("\t")
        passlist.append(as_list[1].strip('\n'))
        usernames.append(as_list[0].strip('\n'))

start = time.time()
for i in range(0,len(passlist)):
    if (passlist[i]==targethash):
        for j in range(0,len(dict_hash)):
            if (dict_hash[j]==passlist[i]):
                print('Cracked Username: '+usernames[i])
                print('Cracked Password: '+dictionarywords[j])
                stop = time.time()
                print('Time (Approx) taken for the first user: {:.2f} seconds'.format(stop - start))
