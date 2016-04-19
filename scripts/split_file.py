#!/usr/bin/env python
import sys
import re

def clean_article_name(name):
    return name.replace('/', '_')

def clean_article(article):
    article = article.lower()
    article = re.sub('\(.*\)', '', article)
    article = re.sub('\[.*\]', '', article)
    article = re.sub('[^a-zA-Z\s:]', '', article)
    return article

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

# Turn sample into one article per line file
def oneline_file(f_name, output_file):
    curr_article = []
    article_name = None
    with open(output_file, 'w') as f:
        for line in open(f_name):
            s_line = line.strip()
            m = re.search('<title>(.*)</title>', s_line)
            if m and article_name:
                article_name = m.group(1)
                if not article_name.startswith('Talk:'):
                    article = ' '.join(curr_article)
                    f.write(clean_article(article))
                    f.write('\n')
                    article_name = clean_article_name(m.group(1))
                curr_article = []
            elif m:
                article_name = clean_article_name(m.group(1))
            else:
                curr_article.append(s_line)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        oneline_file(sys.argv[1], sys.argv[2])
    else:
        print "usage: <datafile> (<output folder>)"
