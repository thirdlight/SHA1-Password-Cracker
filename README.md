# SHA1-Password-Cracker
Homework 2 for Blockchain and Applications. This program takes the hash of a word and cracks it via a basic, brute force algorithm.
## Getting Started
### Dependencies:
* Python 2.7+
### Installation:
Download the sha1 folder locally onto your machine and enter that folder from the command line.
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

The program located in file rainbow sha1 reads a json file called "rainbow.json" into a dictionary inside that program. It then looks up hashes with only a single attempt. This program can also solve salted hashes only if the salted hash is known. If that file does not exist, the program will create it.

### Installation:
Download the rainbow sha1 folder locally onto your machine and enter that folder from the command line.
From there, there are two main ways to run this program.
1. If the password NOT salted, run:
 `py -2 [argument hash]`
1. If the hash is salted AND you know the hash of the salt, run: 
 `py -2 [argument hash] [argument salt hash]`
 This program cannot run if the salted hash is not known, as the process would be identical to the basic brute force algorithm in the previous section.
### Answers
1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3: letmein, found in 1 attempt, took 2.2 seconds to run
1. 801cdea58224c921c21fd2b183ff28ffa910ce31: vjhtrhsvdctcegth, found in 1 attempt, took 2.15 seconds to run
1. ece4bb07f2580ed8b39aa52b7f7f918e43033ea1: slayerharib, found in 546155 attempts, took 4.54 seconds when the salted hash was known. 

The additional time it takes to find the hashes can be attributed to the program loading the dictionary. However, from there, each hash lookup for a basic hash in the dictionary takes about 2 seconds each, where it can vary wildly in the original brute force program (O(1) vs. O(n)). For salted hashes, timing depends on the location of the input hash (not the salt), but worst case scenarios are still much faster than the original brute force (O(n) vs. O(n^2))
