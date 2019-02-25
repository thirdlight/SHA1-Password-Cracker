import hashlib
import time
import sys
import io
import json

reload(sys)  
sys.setdefaultencoding('utf8') 

start_time = time.time()

try:
# check to see if file exists
    file = open("rainbow.json")
    
except:
# file does not exist, create one
    print("JSON file did not exist. Creating it now . . . .")
    with open("10-million-password-list-top-1000000.txt") as lst:
        passwords = lst.read().split("\n")
        # store basic hashes in a text file, and then load into a dictionary on startup.
        d = {}
        for password in passwords: # hash everything
            hash = hashlib.sha1()
            hash.update(password.encode('utf-8'))
            hash = hash.hexdigest()
            if password == "": # empty string causes problems in the split method, so store as ""
                d[hash] = ""
                break
            d[hash] = password
        with open("rainbow.json", "w") as j:
            json.dump(d, j)
    
# file does exit    
d = json.loads(open("rainbow.json").read())
# restart file position
input_hash =  sys.argv[1]
if len(sys.argv) == 2:
    if input_hash in d:
        # hash isn't salted, should match it in one try via lookup
        print("Match: password is: " + d[input_hash] + " and was found in 1 attempt through the rainbow table")
    

elif len(sys.argv) == 3:
    if sys.argv[2] == "salted":
        print("This program cannot crack a password if the salted hash is not known. See Github README for more information.")
    count = 1 # there is one lookup by default
    with io.open("10-million-password-list-top-1000000.txt") as lst:
        passwords = lst.read().split("\n")
        input_salt_hash = sys.argv[2]
        if input_salt_hash not in d:
            print("The salted hash isn't in the table.")
        else:
            salt = d[input_salt_hash]
            for password in passwords:    
                test = hashlib.sha1()
                test.update(salt+password)
                if(input_hash == test.hexdigest()):
                    print("Match: password is: " + salt+password + " and was found in " + str(count) + " attempts through the rainbow table")
                    break
                count+=1
else:
    print "Incorrect formatting. Please consult the Github README for proper formatting."

print("Program took " + str(time.time() - start_time) + " seconds to run")
