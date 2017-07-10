import os, sys, glob, time
from subprocess import Popen, PIPE

testdir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
forcegen = len(sys.argv) > 2
print('Start tester:', time.asctime())
print('in', os.path.abspath(testdir))

def verbose(*args):
    print('-'*80)
    for arg in args:
        print(arg)

def quiet(*args):
    pass

trace = quiet

testpatt = os.path.join(testdir, 'scripts', '*.py')
testfiles = glob.glob(testpatt)
testfiles.sort()
trace(os.getcwd(), *testfiles)

numfail = 0
for testpath in testfiles:
    testname = os.path.basename(testpath)
    
    infile = testname.replace('.py', '.in')
    inpath = os.path.join(testdir, 'inputs', infile)
    indata = open(inpath, 'rb').read() if os.path.exists(inpath) else b''
    
    argfile = testname.replace('.py', '.args')
    argpath = os.path.join(testdir, 'args', argfile)
    argdata = open(argpath).read() if os.path.exists(argpath) else ''
    
    outfile = testname.replace('.py', '.out')
    outpath = os.path.join(testdir, 'outputs', outfile)
    outpathbad = outpath + '.bad'
    if os.path.exists(outpathbad):
        os.remove(outpathbad)
        
    errfile = testname.replace('.py', '.err')
    errpath = os.path.join(testdir, 'errors', errfile)
    if os.path.exists(errpath):
        os.remove(errpath)
        
    pypath = sys.executable
    command = '%s %s %s' % (pypath, testpath, argdata)
    trace(command, indata)
    
    procces = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    procces.stdin.write(indata)
    procces.stdin.close()
    outdata = procces.stdout.read()
    errdata = procces.stderr.read()
    exitstatus = procces.wait()
    trace(outdata, errdata, exitstatus)
    
    if exitstatus != 0:
        print('Error status:', testname, exitstatus)
        
    if errdata:
        print('Error stream:', testname, errpath)
        open(errpath, 'wb').write(errdata)
        
    if exitstatus or errdata:
        numfail += 1
        open(outpathbad, 'wb').write(outdata)
    elif not os.path.exists(outpath) or forcegen:
        print('generating:', outpath)
        open(outpath, 'wb').write(outdata)
    else:
        priorout = open(outpath, 'rb').read()
        if priorout == outdata:
            print('passed:', testname)
        else:
            numfail += 1
            print('Failed output:', testname, outpathbad)
            open(outpathbad, 'wb').write(outdata)      
        
print('Finished:', time.asctime())
print('%s tests were run, %s tests failed' % (len(testfiles), numfail))