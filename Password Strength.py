dictionarywords=[]
dict_hash=[]

knownpass=input('Please enter a password: ')
w,m,s = " ", " ", " "

with open('dictionary.txt', 'r') as f:
    for line in f:
        word=line.strip('\n')
        dictionarywords.append(word)        

for i in range(0,len(dictionarywords)):
    if (dictionarywords[i] in knownpass):
        if (knownpass==dictionarywords[i]):
            w=True
        else:
            m=True       
    else:
        s=True       

if (w==True):
    print('Weak Password')
elif (m==True):
    print('Moderate Password')
elif (s==True):
    print('Strong Password')
