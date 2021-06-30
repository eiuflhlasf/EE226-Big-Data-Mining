# Your code here, you can add cells if necessary
import math
import datetime
print(datetime.datetime.now() )

filename = '../input/coding2/stream_data.txt'

sum=[]
container = {}
windowsize = 1000
timestamp = 0
updateinterval = 1000# no larger than the windowsize
updateindex = 0

keysnum = int(math.log(windowsize, 2)) + 1
keylist = list()
# initialize the container
for i in range(keysnum):
    key = int(math.pow(2, i))
    keylist.append(key)
    container[key] = list()

def UpdateContainer(inputdict, klist, numkeys):
    for key in klist:
        if len(inputdict[key]) > 2:
            inputdict[key].pop(0)
            tstamp = inputdict[key].pop(0)
            if key != klist[-1]:
                inputdict[key * 2].append(tstamp)
        else:
            break

def OutputResult(inputdict, klist, wsize):
    cnt = 0
    firststamp = 0
    for key in klist:
        if len(inputdict[key]) > 0:
            firststamp = inputdict[key][0]
        for tstamp in inputdict[key]:
            print ("size of bucket: %d, timestamp: %d" % (key, tstamp))
    for key in klist:
        for tstamp in inputdict[key]:
            if tstamp != firststamp:
                cnt += key
            else:
                cnt += 0.5 * key
    sum.append(cnt)

    print ("Estimated number of ones in the last %d bits: %d" % (wsize, cnt))
    print(datetime.datetime.now() )

with open(filename, 'r') as sfile:
    while True:
        char = sfile.read(1)
        if not char:# no more input
            OutputResult(container, keylist, windowsize)
            break
        timestamp = (timestamp + 1) % windowsize
        for k in container.keys():
            for itemstamp in container[k]:
                if itemstamp == timestamp:# remove record which is out of the window
                    container[k].remove(itemstamp)
        if char == "1":# add it to the container
            container[1].append(timestamp)
            UpdateContainer(container, keylist, keysnum)
        updateindex = (updateindex + 1) % updateinterval
        if updateindex == 0:
            OutputResult(container, keylist, windowsize)
            print ("\n")

    summ=0
    for item in sum:
        summ+=int(item)
    print(summ)

