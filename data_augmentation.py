import numpy as np
import tensorflow as tf
import random
from dataloader import Gen_Data_loader, Dis_dataloader
from generator import Generator
from discriminator import Discriminator
from rollout import ROLLOUT
from target_lstm import TARGET_LSTM
import pickle

positive_file = 'save/real_sequence.txt'
BATCH_SIZE = 4
generate_data = [0]*101

def generate_mutant():
	ran = np.random.rand(1)
	for i in range (len(generate_data)):
		if(ran<=generate_data[i]):
			return i

def generate_mutant_seq(seq,num):
	tmp = seq
	tmp = np.asarray(tmp)
	length = np.where(tmp==100)[0][0]
	for i in range (num):
		ran = np.random.randint(0,length,1)[0]
		tmp[ran] = generate_mutant()
	return tmp

def ran_select_sequence(seq_list):
	length = len(seq_list)
	ran = np.random.randint(0,length,1)[0]
	return seq_list[ran]


def main():
	global generate_data
	gen_data_loader = Gen_Data_loader(BATCH_SIZE)
	gen_data_loader.create_batches(positive_file)
	# print(gen_data_loader.token_stream)
	data = gen_data_loader.token_stream
	for each_line in data:
		for each in each_line:
			if each>=100 or each==0:
				continue 
			else: 
				generate_data[each]+=1
	generate_data = (generate_data/np.sum((generate_data))) # probability list
	for i in range (len(generate_data)):
		if (i==0): continue
		generate_data[i] = generate_data[i]+generate_data[i-1] # generate final probability list
	# print(generate_mutant_seq(data[4],4))
	count = 0
	while(count<5000-120):
		seq = ran_select_sequence(data)
		num = np.random.randint(1,10,1)[0]
		gen_seq = generate_mutant_seq(seq,num)
		data.append(gen_seq)
		count+=1
	Dis_dataloader.write_train_data(data)





	# for each in data:
	# 	tmp_1 = each 
	# 	tmp_2 = each
	# 	last = each.index(100)
	# 	tmp[100-1] = 100
	# 	tmp[100] = 4999
	# 	generate_data.append(tmp)
	# data.extend(generate_data)

if __name__ == '__main__':
    main()