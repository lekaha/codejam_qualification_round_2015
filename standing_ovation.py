def standing(audiences):
    if not audiences or len(audiences) == 0 or len(audiences) == 1:
        return 0
    count = 0
    need = 0

    for i in xrange(len(audiences)):
        need = max(need, i - count)
        count += audiences[i]
    return need


def load_input(filename = None):
    if not filename:
        return
    line_buffer = None
    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys  

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', '6 0000001']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')
    print int(lines[0]) == (len(lines) - 1)
    for i in xrange(int(lines[0])):
        shyness, audiences = map(str, lines[i + 1].split(' '))
        req_audience = standing([int(a) for a in audiences])
        s =  'Case #%d: %s\n'%(i+1, req_audience)
        f.writelines(s)
        print '%s'%s
    f.close()
    

if __name__ == '__main__':
    main(sys.argv[1:])