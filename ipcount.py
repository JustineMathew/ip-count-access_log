import sys
import os
import parser
import collections

#Taking command line arguments
args=sys.argv

#Setting a python counter for storing the IP from the log
counter=collections.Counter()
print()
heading="The first {} IPS the are found from the log are listed below".format(args[2])
print()
print(heading)
print('-' * len(heading))
print()
#Excluding Loop back IP address
excludes=["::1","127.0.0.1"]

#Checking the condition of the commmand line arguments
if len(args) == 3:
    if not args[2].isdigit():
        print("The {} should be digit".format(args[2]))
        sys.exit()
    if not os.path.exists(args[1]):
        print("The location {} does not exist".format(args[1]))
        sys.exit(1)
    if not os.path.isfile(args[1]):
        print("This {} is not a valid file".formt(agrs[1]))
        sys.exit(1)

#Taking each IP from the log  counting the occurance using the counter
    f=open(args[1],'r')
    for line in f:
        content=parser.parser(line)
        ip=content['host']
        if ip not in excludes:
            counter.update([ip])
    f.close()

#printing the list of IP and their counts
    for ips,count in counter.most_common(int(args[2])):
        print("{:18} : {}".format(ips,count))
print()
print('-' * len(heading))
print()
print()

