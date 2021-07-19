def to_pig_latin(sentence):
    words = sentence.split(" ")
    sentence_2=" "
    for i in range(0,len(words)):
        wrd= words[i]
        b=0
        if wrd=="":
            wrd_2=""
        elif wrd[0]=='a' or wrd[0]=='e' or wrd[0]=='i' or wrd[0]=='o' or wrd[0]=='u':
            wrd_2 =wrd + 'way'
            
        else:
            while wrd[b]!='a' and wrd[b]!='e' and wrd[b]!='i' and wrd[b]!='o' and wrd[b]!='u':
                b+= 1
                if b==len(wrd):
                    break
            wrd_2 =wrd[b:]+'a'+wrd[:b]+'ay'
        if i==0:
            sentence_2 =wrd_2
        elif wrd_2=='':
            sentence_2+=wrd_2
        else:
            sentence_2+=" "+wrd_2
    return sentence_2

def to_english(sentence):
    words=sentence.split(" ")
    sentence_2=""
    for i in range(0,len(words)):
        wrd= words[i]
        b=3
        if wrd=='':
            wrd_2=''
        else:
            while wrd[len(wrd)-b]!='a' and wrd[len(wrd)-b]!='w':
                b+=1
            wrd_2 =wrd[len(wrd)-b+1:len(wrd)-2]+wrd[:len(wrd)-b]
        if i==0:
            sentence_2 =wrd_2
        elif wrd_2=='':
            sentence_2+=wrd_2
        else:
            sentence_2+=" "+wrd_2
    return sentence_2
        
