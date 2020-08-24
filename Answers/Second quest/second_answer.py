import re
from collections import Counter

with open('hits.txt', 'r') as f:
    sites = f.readlines()
    aggr = []
    pattern = re.compile('\\t(.*?)\\t')

    for i in range(len(sites)):
        ex = re.findall(pattern, sites[i])
        aggr += ex

    c = Counter(aggr).most_common(5)
    for i in c:
        print(i)