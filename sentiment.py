# usage python test.py my.json
import sys
import csv
# import pygraphviz as pgv
import numpy as np
import networkx as nx
from datetime import datetime
import math
from collections import defaultdict
import liwc.categories

# import liwc.categories

labels = ["first_person", "second_person", "third_person", "posemo", "negemo", "cognitive", "sensory", "time", "past",
          "present", "future", "work", "leisure", "swear", "social", "family", "friend", "humans", "anx", "anger",
          "sad", "body", "health", "sexual", "space", "time", "achieve", "home", "money", "relig", "Affect", "cause",
          "Quant", "Numb", "inhib", "ingest", "motion", "nonfl", "filler", "number_classified_words", "number_words"]


def main():
    tweets_csv = sys.argv[1]
    output_file = open('liwc_' + tweets_csv, 'w')
    csv_writer = csv.writer(output_file, delimiter=',')

    with open(tweets_csv) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            tweet_id = row[0]
            tweet_date = row[1]
            tweet_text = row[2]

            print(tweet_text)
            liwc_data = liwc_classify(tweet_text)

            row = [tweet_id, tweet_date, tweet_text] + liwc_data
            csv_writer.writerow(row)


def liwc_classify(text):
    # text is the body of text we want to run LIWC on
    vals = liwc.categories.classify(text)
    
    for i in range(len(vals)):
        print(labels[i], vals[i])
        
    return list(vals)

                        
if __name__ == "__main__":
    main()
