# SHA1-Password-Cracker
Homework 2 for Blockchain and Applications
## Getting Started
### Dependencies:
* Python 2.7+
### Installation:
There are three main ways to run this program.
1. If the password NOT salted, run:
 `py -2 [input hash]`
1. If the hash is salted AND you know the hash of the salt, run: 
 `py -2 [input hash] [input salt hash]`
1. If you know the hash is salted, but you do NOT know the hash of the salt, run:
 `py -2 [input hash] salted`
### Anwswers
1. b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3: letmein, found in 16 attempts, took 0.23 seconds to run
1. 801cdea58224c921c21fd2b183ff28ffa910ce31: vjhtrhsvdctcegth, found in 999968 attemps, took 6.8 seconds to run
1.  ece4bb07f2580ed8b39aa52b7f7f918e43033ea1: slayerharib, found in 546372 attempts, took 2.75 seconds when the salted hash was known and __ seconds when the salted hash was unknown.
