import os
from ftpdownloadmodule import configTransfer, connectFtp, isTextKind

def cleanRemotes(cf, connection):
    if cf.cleanall:
        for remotename in connection.nlst():
            try:
                print('deleting remote', remotename)
                connection.delete(remotename)
            except:
                print('cannot delete remote', remotename)
        
def uploadAll(cf, connection):
    localfiles = os.listdir(cf.localdir)
    for localname in localfiles:
        localpath = os.path.join(cf.localdir, localname)
        print('uploading', localpath, 'to', localname, 'as', end=' ')
        if isTextKind(localname):
            localfile = open(localpath, 'rb')
            connection.storlines('STOR '+localname, localfile)
        else:
            localfile = open(localpath, 'rb')
            connection.storbinary('STOR '+localname, localfile)
        localfile.close()
    connection.quit()
    print('Done:', len(localfiles), 'files uploaded')
    
if __name__ == '__main__':
    cf = configTransfer(site='example.org.ua', rdir='books', user='igor')
    conn = connectFtp(cf)
    cleanRemotes(cf, conn)
    uploadAll(cf, conn)   
    
    