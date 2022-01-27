# a look at file handling

try: 
    f = open('myfile.dat', 'rb')
except:
    print('file not found')