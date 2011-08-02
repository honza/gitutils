import os
from commands import getoutput

class Blamer(object):
    """
    This script will run through all the files git tracks, and see how many
    lines each user has written/edited. You will get a number of lines and
    percentage. Throughout the course of a project, you will add lines and your
    lines will be deleted. This shows you how much of your code is still in the
    project now.
    """
       
    def __init__(self):
        os.chdir(os.getcwd())
        out = getoutput('git ls-files')
        files = out.split("\n")
        results = {}
        counter = 0

        for file in files:
            blame = getoutput('git blame -p %s' % file)
            parts = blame.split("\n")
            lines = []
            line = []
            commits = {}

            for part in parts:
                if not part.startswith("\t"):
                    line.append(part)
                else:
                    lines.append(line)
                    line = []

            counter += len(lines)

            for line in lines:
                bits = line[0].split(" ")
                sha = bits[0]
                if sha not in commits:
                    if line[1].startswith('author '):
                        commits[sha] = self.get_author(line[1])
                    else:
                        commits[sha] = None
                else:
                    if not commits[sha]:
                        commits[sha] = self.get_author()

            for line in lines:
                try:
                    name = self.get_author(line[1])
                except IndexError:
                    # look up from commits
                    sha = line[0].split(" ")[0]
                    name = commits[sha]
                if name not in results:
                    results[name] = 1
                else:
                    results[name] += 1
                   

        k = results.keys()
        chart = {}
        for c in k:
            if results[c] not in chart:
                chart[results[c]] = c
            else:
                pass

        k = chart.keys()
        k.sort()
        k.reverse()
        try:
            w = len(str(k[0]))
        except IndexError:
            print 'Not a git repository'

        for c in k:
            x = ' '*( w - len(str(c)) )
            x += '%d: %s' % (c, chart[c],)
            print x

        print '-'*80

        o = float(float(counter)/100)
        for c in k:
            n = float(float(c)/o)
            x = str(int(n))
            x += "%: "
            x += str(chart[c])
            print x


    def get_author(self, name):
        name = name.split(" ")
        name.remove("author")
        name = " ".join(name)
        return name



if __name__ == '__main__':
    Blamer()
