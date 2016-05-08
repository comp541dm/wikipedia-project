# wikipedia-project
[![Build Status](https://travis-ci.org/comp541dm/wikipedia-project.svg?branch=master)](https://travis-ci.org/comp541dm/wikipedia-project)

  - [Data here](https://en.wikipedia.org/wiki/Wikipedia:Database_download)

## Usage
```
sbt "run-main LDAExample --k=5 --stopwordFile=data/stop_words.txt data/cleaned_articles.txt"
```

### Fill the stopword file
Words that appear in more than k/4 of the topics will automatically get added to the stop word file. Run this to fill up the stop word file with common words.
```
# Run 5 times on random part of the dataset
for i in $(seq 5); do
    sbt "run-main LDAExample --k=20 --stopwordFile=data/stop_words.txt --vocabSize=100 ../wikipedia_data/disk{$(gshuf -i 1-999 -n 15 | paste -s -d, -)}.txt"
done
```

## Topic Modeling
[Project here](topic-modeling)

## Resources
  - [Latent Dirichlet Allocation](https://www.cs.princeton.edu/~blei/papers/BleiNgJordan2003.pdf)
  - [Generative Learning Algorithms](http://cs229.stanford.edu/notes/cs229-notes2.pdf)
  - [Singular Value Decomposition Tutorial](https://www.ling.ohio-state.edu/~kbaker/pubs/Singular_Value_Decomposition_Tutorial.pdf)
