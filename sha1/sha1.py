#!/usr/bin/python

# encoding=utf8



#hashing test
#just go through sequentially
# take input hash, optionally take salt, then do the thing
# take the hash, then go through and hash the password list, 


#letmein
#vjhtrhsvdctcegth
#slayerharib

# ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
# f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
import hashlib
import time
import sys
import io

reload(sys)  
sys.setdefaultencoding('utf8') 

start_time = time.time()

match = False
salt_match = False

input_hash = sys.argv[1]
count=0
if len(sys.argv) == 2:
    with io.open("10-million-password-list-top-1000000.txt") as lst:
        passwords = lst.read().split("\n") 
        for password in passwords:
            count+=1
            test = hashlib.sha1()
            test.update(password.decode('utf-8'))
            if(input_hash == test.hexdigest()):
                print("Match: password is: " + password + " and was found in " + str(count) + " attempts through brute force")
                match = True
                break
elif len(sys.argv) == 3:
    # salted password
    if sys.argv[2] == "salted":
    # salt is unknown
        with io.open("10-million-password-list-top-1000000.txt") as lst:
            passwords = lst.read().split("\n")    
            for password in passwords:
                for salt in passwords:
                    count+=1
                    test = hashlib.sha1()
                    test.update(salt)
                    test.update(password.decode('utf-8'))
                    if(input_hash == test.hexdigest()):
                        print("Match: password is: " + salt + password + " and was found in " + str(count) + " attempts through brute force")
                        match = True
                        break
                if match == True:
                    break
    else:
        # the hash of the salt is known
        
        with io.open("10-million-password-list-top-1000000.txt") as lst:
            passwords = lst.read().split("\n")    
            input_salt_hash = sys.argv[2]
            for password in passwords:
                count+=1
                salt = hashlib.sha1()
                salt.update(password)
                if(input_salt_hash == salt.hexdigest()):
                    print("Salt found: " + password )
                    salt_match = True
                    salt = password
                    break
            if salt_match:
                for password in passwords:
                    count+=1
                    test = hashlib.sha1()
                    test.update(salt)
                    test.update(password)
                    if(input_hash == test.hexdigest()):
                        print("Match: password is: " + salt + password + " and was found in " + str(count) + " attempts through brute force")
                        match = True
                        break
            else:
                print("Could not crack salt hash")
else:
    print "Incorrect formatting. Please consult the Github README for proper formatting"

print("Program took " + str(time.time() - start_time) + " seconds to run")

''''
with open("10-million-password-list-top-1000000.txt") as lst:
    passwords = lst.read().split("\n")
    input_hash = raw_input("Enter the hash > ")
    input_salt_hash = raw_input("Enter the known salt (optional; if no salt, type nothing)> ")
    count=0
    if input_salt_hash != "":
        for password in passwords:
            count+=1
            salt = hashlib.sha1()
            salt.update(password)
            if(input_salt_hash == salt.hexdigest()):
                print("Salt found: " + password )
                salt_match = True
                salt = password
                break
        if salt_match:
            for password in passwords:
                count+=1
                test = hashlib.sha1()
                test.update((salt+password).encode('utf-8'))
                if(input_hash == test.hexdigest()):
                    print("Match: password is: " + salt + password + " and was found in " + str(count) + " attempts through brute force")
                    match = True
                    break
        else:
            print("Could not crack salt hash")
    else:
        for password in passwords:
            count+=1
            test = hashlib.sha1()
            test.update(password.encode('utf-8'))
            if(input_hash == test.hexdigest()):
                print("Match: password is: " + password + " and was found in " + str(count) + " attempts through brute force")
                match = True
                break
if not match:
    print("Hash could not be found")
    
'''