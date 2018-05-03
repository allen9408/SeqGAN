import csv
import pdb
trace_dict = {}
word_set = set()
word_dict = {}

with open('intubation.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  # header = reader.next()
  next(reader)
  for row in reader:
    # pdb.set_trace()
    caseID, activity = row[0:2]
    if not caseID in trace_dict.keys():
      trace_dict[caseID] = []
    trace_dict[caseID].append(activity)
    word_set.add(activity)

idx = 1
lens = [len(v) for k,v in trace_dict.items()]
maxlen = max(lens)
for word in word_set:
  word_dict[word] = idx
  idx += 1

import pickle as pkl
pkl.dump(word_dict, open( "word_d.pkl", "wb" ) )

with open('intubation_idx.txt', 'w') as f:
  wr = csv.writer(f, delimiter=' ')
  for k, v in trace_dict.items():
    cur_len = len(v)
    wr.writerow([0] + [word_dict[i] for i in v] + [idx for i in range(maxlen + 1 - cur_len)])

