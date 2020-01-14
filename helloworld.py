import subprocess
import sys
import getopt
#print('hello world'.upper() + str(len('Hello, World!')))

#print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('arguments', sys.argv[1:])



#def append_to_sequence (myseq):
#    myseq += (9,9,9)
#    return myseq

# tuple1 = (1,2,3)
# list1 = [1,2,3]
# tuple2 = append_to_sequence(tuple1)
# list2 = append_to_sequence(list1)

# print ('apa kalle balle'.split())

# print ('tuple1 = ', tuple1)
# print ('tuple2 = ', tuple2)
# print ('list1 = ', list1)
# print ('list2 =', list2)

logfile = open('logfile', 'w')

commands = sys.argv[1:]

for i in range(10):
    print ('test')
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    print ('hej')
    for line in process.stdout:
        print ('the line', line)
        sys.stdout.write(line)
        logfile.write(line)
        sys.stdout.flush()
    process.wait()