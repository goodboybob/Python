def read_dict():
    f=open("words.txt",'rU')
    words=f.read()
    wordlist=[]
    wordlist=words.split()
    return wordlist
    f.close()

def read_domains():
    t=open("domains_dos.txt",'rU')
    
    domains=t.read()
    domainlist=[]
    domainlist=domains.split()
    domainmap={}
    for dom in domainlist:
        domainmap[dom]=0;
    return domainmap
    t.close()

def dashes_digit_rank_sub(string):
    length=len(string)
    count=0
    digit=0
    ranksub=0
    for a in range(length):
        if string[a]=='-':
            count=count+1
        if (string[a]).isdigit()==True:
            digit=1
            
    ranksub=(count*2)+(digit*2)
    return ranksub
    
def number_of_words():

    wordlist=[]
    wordlist=read_dict()
    domainmap={}
    domainmap=read_domains()
    outstring=""
    o=open("output.txt",'w')

    for domain in domainmap:
        for word in wordlist:
            if len(word)>2:
                if domain.find(word)>=0:
                    a=domainmap[domain]
                    domainmap[domain]=a+1
        rank=domainmap[domain]
        domlen=len(domain)
        
        if domlen>12:
            rank=rank-((domlen-12))
        else:
            rank=rank+4
            
        rank=rank- dashes_digit_rank_sub(domain)

        
        x=domain+"  "+str(rank)+'\n'
        outstring=outstring+x
        print(domain)
    
    #print(wordlist)
    o.write(str(outstring))

    

def main():
    number_of_words()

if __name__=="__main__":
    main()
