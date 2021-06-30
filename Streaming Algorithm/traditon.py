import datetime
print(datetime.datetime.now() )
filename = '../input/coding2/stream_data.txt'
index=0
count=0
windowsize=1000
with open(filename, 'r') as sfile:
    while True:
        char = sfile.read(1)
        if not char:
            print(count)# no more input
            break
        index=(index + 1) % windowsize
        if char == "1":
            count+=1
        if index==0:
            print(count)
            count=0


print(datetime.datetime.now() )



