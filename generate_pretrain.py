import numpy as np
import tensorflow as tf
import random
from dataloader import Gen_Data_loader, Dis_dataloader
from generator import Generator
from discriminator import Discriminator
from rollout import ROLLOUT
# from target_lstm import TARGET_LSTM
from target_lstm_new import TARGET_LSTM
import pickle
import pdb

#########################################################################################
#  Generator  Hyper-parameters
######################################################################################
EMB_DIM = 32 # embedding dimension
HIDDEN_DIM = 32 # hidden state dimension of lstm cell
SEQ_LENGTH = 22 # sequence length
# SEQ_LENGTH = 253 # sequence length
START_TOKEN = 0
# PRE_EPOCH_NUM = 120 # supervise (maximum likelihood estimation) epochs
PRE_EPOCH_NUM = 120 # supervise (maximum likelihood estimation) epochs
SEED = 88
# BATCH_SIZE = 64
BATCH_SIZE = 4
#########################################################################################
#  Discriminator  Hyper-parameters
#########################################################################################
dis_embedding_dim = 64
# dis_filter_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
# dis_num_filters = [100, 200, 200, 200, 200, 100, 100, 100, 100, 100, 160, 160]
dis_filter_sizes = [3, 5]
dis_num_filters = [200, 100]
dis_dropout_keep_prob = 0.75
dis_l2_reg_lambda = 0.2
# dis_batch_size = 64
BATCH_SIZE = 4
#########################################################################################
#  Basic Training Parameters
#########################################################################################
TOTAL_BATCH = 200
# TOTAL_BATCH = 50
positive_file = 'save/intubation_idx.txt'
# positive_file = 'save/real_sequence.txt'

negative_file = 'save/generator_sample.txt'
eval_file = 'save/eval_file.txt'
# generated_num = 10000
generated_num = 1000

def generate_samples(sess, trainable_model, batch_size, generated_num, output_file):
    # Generate Samples
    generated_samples = []
    for _ in range(int(generated_num / batch_size)):
        generated_samples.extend(trainable_model.generate(sess))

    with open(output_file, 'w') as fout:
        for poem in generated_samples:
            buffer = ' '.join([str(x) for x in poem]) + '\n'
            fout.write(buffer)


def target_loss(sess, target_lstm, data_loader):
    # target_loss means the oracle negative log-likelihood tested with the oracle model "target_lstm"
    # For more details, please see the Section 4 in https://arxiv.org/abs/1609.05473
    nll = []
    data_loader.reset_pointer()

    for it in range(data_loader.num_batch):
        batch = data_loader.next_batch()
        g_loss = sess.run(target_lstm.pretrain_loss, {target_lstm.x: batch})
        nll.append(g_loss)

    return np.mean(nll)


def pre_train_epoch(sess, trainable_model, data_loader):
    # Pre-train the generator using MLE for one epoch
    supervised_g_losses = []
    data_loader.reset_pointer()

    for it in range(data_loader.num_batch):
        batch = data_loader.next_batch()
        # pdb.set_trace()
        _, g_loss = trainable_model.pretrain_step(sess, batch)
        supervised_g_losses.append(g_loss)

    return np.mean(supervised_g_losses)


def main():
    random.seed(SEED)
    np.random.seed(SEED)
    assert START_TOKEN == 0

    gen_data_loader = Gen_Data_loader(BATCH_SIZE, SEQ_LENGTH)
    likelihood_data_loader = Gen_Data_loader(BATCH_SIZE, SEQ_LENGTH) # For testing
    # vocab_size = 5000
    vocab_size = 102
    dis_data_loader = Dis_dataloader(BATCH_SIZE, SEQ_LENGTH)

    generator = Generator(vocab_size, BATCH_SIZE, EMB_DIM, HIDDEN_DIM, SEQ_LENGTH, START_TOKEN)
    # target_params = pickle.load(open('save/target_params.pkl'))
    target_params = pickle.load(open('save/target_params.pkl', 'rb'), encoding='latin1')
    # target_lstm = TARGET_LSTM(vocab_size, BATCH_SIZE, EMB_DIM, HIDDEN_DIM, SEQ_LENGTH, START_TOKEN, target_params) # The oracle model
    target_lstm = TARGET_LSTM(vocab_size, BATCH_SIZE, EMB_DIM, HIDDEN_DIM, SEQ_LENGTH, START_TOKEN) # The oracle model

    # discriminator = Discriminator(sequence_length=20, num_classes=2, vocab_size=vocab_size, embedding_size=dis_embedding_dim, 
    #                             filter_sizes=dis_filter_sizes, num_filters=dis_num_filters, l2_reg_lambda=dis_l2_reg_lambda)
    discriminator = Discriminator(sequence_length=SEQ_LENGTH, num_classes=2, vocab_size=vocab_size, embedding_size=dis_embedding_dim, 
                                filter_sizes=dis_filter_sizes, num_filters=dis_num_filters, l2_reg_lambda=dis_l2_reg_lambda)

    # config = tf.ConfigProto()
    # config.gpu_options.allow_growth = True
    # sess = tf.Session(config=config)
    # sess.run(tf.global_variables_initializer())
    config = tf.ConfigProto()
    # config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    # sess.run(tf.global_variables_initializer())
    # gen_data_loader.create_batches(positive_file)


    rollout = ROLLOUT(generator, 0.8)
    saver = tf.train.Saver()
    saver.restore(sess, 'models/intubation.ckpt')

    
   
    # generate sequences
    generate_samples(sess, generator, BATCH_SIZE, generated_num, 'save/Generate.txt')

    # save models
    # saver = tf.train.Saver()
    # saver.save(sess, 'models/intubation.ckpt')

if __name__ == '__main__':
    main()
