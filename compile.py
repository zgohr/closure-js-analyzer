import sys
import subprocess
import os


def compile_file(location):
    p = subprocess.Popen(location,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll()
        line = p.stdout.readline()
        yield line
        if(retcode is not None):
            break


if __name__ == "__main__":
    path = sys.argv[1]
    files = [s for s in os.listdir(path) if s.endswith('.js')]
    for f in files:
        print 'Starting %s...' % f
        for l in compile_file(['java', '-jar', 'compiler.jar',
                               '--js="%s"' % os.path.join(path, f),
                               '--js_output_file=/dev/null']):
            if len(l.rstrip()) > 0:
                print l.rstrip()
        print 'Done %s' % f
        print
