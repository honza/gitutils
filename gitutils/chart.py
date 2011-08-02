"""
Git Chart - Number of lines changed per author
Auhthor: honza <http://github.com/honza>

Usage: Drop this file into a Git repo and run it!
"""

from commands import getoutput
import sys


class GitChart(object):

    def __init__(self):
        authors = self.get_authors()
        r = {}
        for author in authors:
            c = "git log --author='%s' --pretty=tformat: --numstat" % author
            out = getoutput(c)
            out = out.split("\n")
            total = 0
            for s in out:
                if s is '':
                    pass
                else:
                    f = s.split("\t")
                    if f[0] is not '-':
                        try:
                            total += int(f[0])
                            total += int(f[1])
                        except ValueError:
                            print 'Not a git repo'
                            sys.exit(1)

            if total not in r:
                r[total] = [author]
            else:
                r[total].append(author)
            #print out
        h = r.keys()
        h.sort()

        x = h[len(h)-1]
        width = len(str(x))

        h.reverse()
        print '-'*80
        print "Git Score Board"
        print "Number of lines changed\n"

        for v in h:
            for auth in r[v]:
                local_width = len(str(v))
                s = ""
                s += ' '*(width-local_width)
                s += str(v)
                s += ' '
                s += str(auth)
                print s

    def get_authors(self):
        out = getoutput("git log --format='%aN' | sort -u")
        out = out.split("\n")
        return out


if __name__ == '__main__':
    GitChart()
