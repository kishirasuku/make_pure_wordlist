import getopt
import sys
import itertools
import datetime

def usage():
    print "Usage:python maker.py [-option]"
    print "Option:"
    print "-r,--range     this option is set"
    print "               range of words"
    print "               ex)1:3"
    print ""
    print "-s,--setnumber this option is whe"
    print "               ther you set numbe"
    print "               r in wordlist"
    print "-o,--output    this option is sel"
    print "               ecting file name f"
    print "               or output"
    sys.exit(0)

def writer(i,f,alp):
    pair = list(itertools.permutations(alp,i))
    for l in pair:
        word = "".join(l)
        f.write(word+"\n")
        
def main():
    if not len(sys.argv[1:]):
        usage()
    
    s,l = 1,2
    
    try:
        opts,args = getopt.getopt(
            sys.argv[1:],
            "r:o:s",
            ["range=","output=","setnumber"]
        )
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    numflag = False

    today = datetime.datetime.today()
    today = str(today)
    filename = today[0:10] + ".txt"

    for o in opts:
        if o[0] in ("-s","--setnumber"):
            numflag = True
        elif o[0] in ("-r","--range"):
            s,l = o[1].split(":")
            s = int(s)
            l = int(l)
        elif o[0] in ("-o","--output"):
            filename = o[1]

    alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num = ["0","1","2","3","4","5","6","7","8","9"]

    if numflag:
        alp += num
    
    with open(filename,mode = "a") as f:
        for i in range(s,l+1):
            writer(i,f,alp)

    print "Complete!!"
    print "success making %s" % filename
    
if __name__ == "__main__":
    main()
    
            

    
        
        
    
