# SHA1-Password-Cracker
Author: Nicole Grizzle<br />
Homework 2 for Blockchain and Applications.<br /> This program takes the hash of a word and cracks it via a basic, brute force algorithm. It compares the argument hash to the hashes of the passwords in the list line-by-line.
## Getting Started
### Dependencies:
* Python 2.7+
All modules are imported from python's standard libraries, so no additional libraries are needed.
### Installation:
Download the sha1 folder locally onto your machine and enter that folder from the command line.<br />
From there, there are three main ways to run this program.
1. If the password NOT salted, run:
 `py -2 [argument hash]`
1. If the hash is salted AND you know the hash of the salt, run: 
 `py -2 [argument hash] [argument salt hash]`
1. If you know the hash is salted, but you do NOT know the hash of the salt, run:
 `py -2 [argument hash] salted`
### Answers
1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3: letmein, found in 16 attempts, took 0.23 seconds to run
1. 801cdea58224c921c21fd2b183ff28ffa910ce31: vjhtrhsvdctcegth, found in 999968 attempts, took 6.8 seconds to run
1. ece4bb07f2580ed8b39aa52b7f7f918e43033ea1: slayerharib, found in 546372 attempts, took 2.75 seconds when the salted hash was known. 

## Bonus

The program located in file rainbow sha1 reads a json file called "rainbow.json" into a dictionary inside that program. It then looks up basic hashes with only a single attempt. This program can also solve salted hashes only if the salted hash is known. If that file does not exist, the program will create it.<br />

If "rainbow.json" does not exist (which it won't by default due to github sizing limits), the program will create the file.

### Installation:
Download the rainbow sha1 folder locally onto your machine and enter that folder from the command line.<br />
From there, there are two main ways to run this program.<br />
1. If the password NOT salted, run:
 `py -2 [argument hash]`
1. If the hash is salted AND you know the hash of the salt, run: 
 `py -2 [argument hash] [argument salt hash]`<br /><br />
This program cannot run if the salted hash is not known, as the process would be identical to the basic brute force algorithm in the previous section.
### Answers
**Note: times below assume the json file already exists in the directory.**<br />
1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3: letmein, found in 1 attempt, took 1.51 seconds to run
1. 801cdea58224c921c21fd2b183ff28ffa910ce31: vjhtrhsvdctcegth, found in 1 attempt, took 1.53 seconds to run
1. ece4bb07f2580ed8b39aa52b7f7f918e43033ea1: slayerharib, found in 546155 attempts, took 3.35 seconds when the salted hash was known. 

The additional time it takes to find the hashes can be attributed to the program loading the dictionary. However, from there, each hash lookup for a basic hash in the dictionary takes about 2 seconds each, where it can vary wildly in the original brute force program (O(1) vs. O(n)). For salted hashes, timing depends on the location of the input hash (not the salt), but worst case scenarios are still much faster than the original brute force (O(n) vs. O(n^2))
