import zipfile
import time
import termcolor
#ZipFile Cracker
#author: SuckerPunch
#based on the book ViolentPython with improvements
#Capabilities to load other Dictionaries
#Other functions will be added soon




def testpass(pas, zipf):
   #Basic function that takes a password and a zipfile to extract
    try:
        zipf.extractall(pwd=pas)
        print termcolor.colored("===============================",'green')
        green = termcolor.colored("[+] Password Found: ",'green')
        print green + pas
        print termcolor.colored("===============================",'green')
        #print"===============================\n"
        exit(0)
        #Ah! my favorite part ;)
    except Exception, e:
        return False
       
def ifnotfound(zipo):
    while testpass:
    #Okay, you need better dictionary mate, Load another one?
        print "\n[-] Password not found, try other Dictionary"
        choice = raw_input("(Y)es,(N)o >> ")
        if choice == 'N':
            exit(0) 
        elif choice == 'Y':
            next = raw_input("[x]Type in next Dictionary File >> ")
            dictwo = open(next)
            for line in dictwo.readlines():
                passwd = line.strip('\n')
                print "[-] Trying " + passwd
                testpass(passwd, zipo)
                time.sleep(0.05)    
        

        
def main():
    zipfile = raw_input("Enter zipfile name: ")
    Zfile = zipfile.ZipFile(zipfile)
    dic = raw_input("Wordlist: ")
    passdic = open(dic)
    
    for line in passdic.readlines():
        #Let's hammer down this zip.
        
        psd = line.strip('\n')
        print "[-] Trying " + psd
        testpass(psd, Zfile)
  
        time.sleep(0.02)#let's set the time to 2 milliseconds between each password   
        
           
    ifnotfound(Zfile)
    
if __name__ == "__main__":
    main()    
