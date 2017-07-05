import sys, os
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)

def splitfile(fromfile, todir, chunksize=chunksize):
    if not os.path.exists(todir):
        os.mkdir(todir)
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir, fname))
    partnum = 0
    inputf = open(fromfile, 'rb')
    while True:
        chunk = inputf.read(chunksize)
        if not chunk:
            break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()
    inputf.close()
    assert partnum <= 9999
    return partnum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: splitfile.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split? ')
            todir = input('Directory to store part files? ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]
            if len(sys.argv) == 4:
                chunksize = int(sys.argv[3])
            absfrom, absto = map(os.path.abspath, [fromfile, todir])
            print('Splitting', absfrom, 'to', absto, 'by', chunksize)
            
            try:
                parts = splitfile(fromfile, todir, chunksize)
            except:
                print('Error during split:')
                print(sys.exc_info()[0], sys.exc_info()[1])
            else:
                print('Split finished:', parts, 'parts are in', absto)
            if interactive:
                input('Press Enter key')
                     