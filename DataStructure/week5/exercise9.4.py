# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest
# number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
# the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "txt.txt"
handle = open(name)

di = dict()

for line in handle:
    line = line.rstrip()
    words = line.split()
    for w in words:
        print("**", w, di.get(w, -99))
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            print("**NEW**")
        print(w, di[w])
print(di)