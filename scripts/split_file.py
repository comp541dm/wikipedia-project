import sys
import re

def clean_article_name(name):
    return name.replace('/', '_')

def split_file(f_name, dir='.'):
    curr_article = []
    article_name = None
    for line in open(f_name):
        s_line = line.strip()
        m = re.search('<title>(.*)</title>', s_line)
        # first document
        if m and article_name:
            # article_name: full text contents dict
            f = open(dir + '/' + article_name, 'w')
            for l in curr_article:
                f.write(l)
            f.close()
            article_name = clean_article_name(m.group(1))
            curr_article = []
        elif m:
            article_name = clean_article_name(m.group(1))
        else:
            curr_article.append(s_line)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        split_file(sys.argv[1])
    elif len(sys.argv) == 3:
        split_file(sys.argv[1], sys.argv[2])
    else:
        print "usage: <datafile> (<output folder>)"
