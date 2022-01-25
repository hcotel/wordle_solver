import csv
import pickle

five_word_list = []
with open('data/unigram_freq.csv', newline='') as freq_file:
    word_freq = csv.reader(freq_file, delimiter=',', quotechar='|')
    for row in word_freq:
        if row[1] == 'count':
            continue
        if len(row[0]) == 5:
            five_word_list.append(row[0])
with open("data/five_words_with_freq.pkl", "wb") as mypicklefile:
    pickle.dump(five_word_list, mypicklefile)