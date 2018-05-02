import csv
import pdb

reference_file = 'save/intubation_idx.txt'
consensus_file = 'save/consensus.csv'
seqgan_file = 'save/Generate.txt'

references = []
with open(reference_file, 'r') as f:
  for line in f:
    references.append(line.split(' '))

seqs_from_gan = []
with open(seqgan_file, 'r') as f:
  for line in f:
    seqs_from_gan.append(line.split(' '))

from nltk.translate.bleu_score import sentence_bleu
scores = [sentence_bleu(references, s) for s in seqs_from_gan]
# score = sentence_bleu(references, seqs_from_gan)
print(sum(scores)/len(scores))
