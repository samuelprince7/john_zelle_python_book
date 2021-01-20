# wordfreq.py

def byFreq(pair):
    return pair[1]
    #returns the 2nd value of a tuple, containing that word's frequency

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ") #input/code here that directs to file path
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words.
    n = int(input("Output analysis of how many words? "))
    items = list(counts.items()) #makes a list of tuples
    items.sort()#sorts the list of tuples in alphabetical order
    items.sort(key=byFreq, reverse=True) #sorts the tuples by frequency & highest to lowest
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

if __name__ == '__main__':  main()
