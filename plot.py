from math import pi
import matplotlib.pyplot as plt
import pandas as pd
import pdb
import numpy as np
import matplotlib.patches as mpatches
import math


# original file 
trace_len_ori = []
trace_len_gen = []

with open('save/intubation_idx.txt', 'r') as f:
    for line in f:
        seq = line.split(' ')
        i = 0
        for a in seq:
            if a == '16':
                break
            i += 1
        trace_len_ori.append(i)

with open('save/Generate.txt', 'r') as f:
    for line in f:
        seq = line.split(' ')
        i = 0
        for a in seq:
            if a == '16':
                break
            i += 1
        trace_len_gen.append(i)

ori_nd = np.array(trace_len_ori)
gen_nd = np.array(trace_len_gen)
print("Real mean: ", np.mean(ori_nd))
print("Gen mean:", np.mean(gen_nd))
print("Real std: ", np.std(ori_nd))
print("Gen std: ", np.std(gen_nd))
max_tl = max(trace_len_ori + trace_len_gen)
min_tl = min(trace_len_ori + trace_len_gen)
t = np.linspace(min_tl, max_tl, 100)
plt.hist(trace_len_ori, t, alpha = 0.8, edgecolor = 'black', color = 'r', label = 'real', normed=True)
plt.hist(trace_len_gen, t, alpha = 0.8, edgecolor = 'black', color = 'y', label = 'artificial', normed=True)
plt.legend(loc='upper right')
plt.savefig('trace_len_dist.png', dpi = 300)
plt.close()

'''
##########################################################################################################
# get activity occurrence distribution
acts_ori = df_original['category'].drop_duplicates().tolist()
act_num_ori = []
act_num_gen = []
colors_ori = []
colors_gen = []
for act_o in acts_ori:
    ori_num = df_original[df_original.category == act_o].shape[0]/len(ids_ori)*100
    gen_num = df_generate[df_generate.Activity == act_o].shape[0]/len(ids_gen)*100
    act_num_ori.append(ori_num)
    act_num_gen.append(gen_num)
    if ori_num > gen_num:
        colors_ori.append('g')
        colors_gen.append('r')
    else:
        colors_ori.append('r')
        colors_gen.append('g')
# print(len(act_num_ori))
# print(len(act_num_gen))
diff = [act_num_ori[i] - act_num_gen[i] for i in range(len(act_num_ori))]
df_act = pd.DataFrame({'acts':acts_ori,'ori_num':act_num_ori,'gen_num':act_num_gen, 'colors_ori':colors_ori, 'colors_gen':colors_gen,'diff':diff})
df_act.sort_values('diff', inplace=True)
acts_ori = df_act['acts'].tolist()
act_num_ori = df_act['ori_num'].tolist()
act_num_gen = df_act['gen_num'].tolist()
colors_ori = df_act['colors_ori']
colors_gen = df_act['colors_gen']
max_an = max(act_num_gen+act_num_ori)
t = range(len(acts_ori))
fig, axes = plt.subplots(ncols=2, sharey=True)
axes[0].barh(t, act_num_ori, align='center', color=colors_ori)
axes[1].barh(t, act_num_gen, align='center', color=colors_gen)
idx = 0
for i, v in enumerate(act_num_ori):
    axes[0].text(v + 9, i, '{:.1f}'.format(diff[idx]), color='black', fontsize=2,verticalalignment='center')
    idx+=1;
idx = 0
for i, v in enumerate(act_num_gen):
    axes[1].text(v + 3, i, '{:.1f}'.format(-diff[idx]), color='black', fontsize=2,verticalalignment='center')
    idx += 1
axes[0].invert_xaxis()
axes[0].set(yticks=t, yticklabels=acts_ori)
axes[0].tick_params(labelsize=2)
axes[1].tick_params(labelsize=2)
axes[0].yaxis.tick_right()
# fig.tight_layout()
fig.subplots_adjust(wspace=0.3)
# plt.show()
plt.savefig('act_dist.png',dpi = 600)
plt.close()
##########################################################################################################
# plot patient distribution
df_patient_ori = pd.read_csv('attributes.csv')
df_ori_pat = df_patient_ori.drop_duplicates(['id'], keep='first')[df_patient_ori.columns[1:24]]
df_gen_pat = df_generate.drop_duplicates(['id'], keep='first')[df_generate.columns[2:24]]
sum_ori = df_ori_pat.sum().tolist()
sum_gen = df_gen_pat.sum().tolist()
# pdb.set_trace()
real_values_0 = [i/df_ori_pat.shape[0] for i in sum_ori]
generated_values_0 = [i/df_gen_pat.shape[0] for i in sum_gen]
cat = df_ori_pat.columns.values.tolist()
# pdb.set_trace()
factor = [math.pow(10, -1 - math.floor(math.log10(max(generated_values_0[i],real_values_0[i])))) for i in range(len(generated_values_0))]
real_values = [100*factor[i] * real_values_0[i] for i in range(len(real_values_0))]
generated_values = [100*factor[i] * generated_values_0[i] for i in range(len(generated_values_0))]
cat = [cat[i]+'(x'+str(factor[i])[:-2] + ')' for i in range(len(cat))]
N = len(cat)
x_as = [n / float(N) * 2 * pi for n in range(N)]
# Because our chart will be circular we need to append a copy of the first
# value of each list at the end of each list with data
real_values += real_values[:1]
generated_values += generated_values[:1]
x_as += x_as[:1]
# Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor="#888888")
# plt.suptitle('Generated Sequences')
# Create polar plot
ax = plt.subplot(111, polar=True)
# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
# Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])
# pdb.set_trace()
# Set yticks
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])
# Plot data
p1 = ax.plot(x_as, real_values, color = 'red', linewidth=0.5, linestyle='solid', zorder=3,alpha=0.5)
# Plot data
p2 = ax.plot(x_as, generated_values, color = 'green', linewidth=0.5, linestyle='solid', zorder=3,alpha=1)
# Fill area
ax.fill(x_as, generated_values, 'green', alpha=0.7, label = 'Generate Data')
ax.fill(x_as, real_values, 'r', alpha=0.7, label = 'Real Data')
ax.fill(x_as, np.minimum(real_values,generated_values), 'blue', alpha=0.6,label='Overlap')
# ax.fill_between(x_as,real_values,generated_values,where,facecolor='blue',alpha=1)
# Set axes limits
plt.ylim(0, 100)
# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi
    if angle_rad == 0:
        ha, distance_ax = "center", 1
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 110 + distance_ax, cat[i], size=12, horizontalalignment=ha, verticalalignment="center")
plt.legend(bbox_to_anchor=(1.1, 1.1), loc='upper left', ncol=1)
plt.show()
# plt.savefig('pat_attr.png', dpi=300)
plt.close()
##########################################################################################################
# plot activity distribution

df_ori_pat = df_original[df_original.columns[4:-1]]
df_gen_pat = df_generate[df_generate.columns[24:]]
sum_ori = df_ori_pat.sum().tolist()
sum_gen = df_gen_pat.sum().tolist()
# pdb.set_trace()
real_values_0 = [i/df_ori_pat.shape[0] for i in sum_ori]
generated_values_0 = [i/df_gen_pat.shape[0] for i in sum_gen]
cat = df_ori_pat.columns.values.tolist()
# pdb.set_trace()
factor = [math.pow(10, -1 - math.floor(math.log10(max(generated_values_0[i],real_values_0[i])))) for i in range(len(generated_values_0))]
real_values = [100*factor[i] * real_values_0[i] for i in range(len(real_values_0))]
generated_values = [100*factor[i] * generated_values_0[i] for i in range(len(generated_values_0))]
cat = [cat[i]+'(x'+str(factor[i])[:-2] + ')' for i in range(len(cat))]
N = len(cat)
x_as = [n / float(N) * 2 * pi for n in range(N)]
# Because our chart will be circular we need to append a copy of the first
# value of each list at the end of each list with data
real_values += real_values[:1]
generated_values += generated_values[:1]
x_as += x_as[:1]
# plt.figure(figsize=(1000,600))
# Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor="#888888")
# plt.suptitle('Generated Sequences')
# Create polar plot
ax = plt.subplot(111, polar=True)
# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
# Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])
# pdb.set_trace()
# Set yticks
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])
# Plot data
p1 = ax.plot(x_as, real_values, color = 'red', linewidth=0.5, linestyle='solid', zorder=3,alpha=0.5)
# Plot data
p2 = ax.plot(x_as, generated_values, color = 'green', linewidth=0.5, linestyle='solid', zorder=3,alpha=1)
# Fill area
ax.fill(x_as, generated_values, 'green', alpha=0.7, label = 'Generate Data')
ax.fill(x_as, real_values, 'r', alpha=0.7, label = 'Real Data')
ax.fill(x_as, np.minimum(real_values,generated_values), 'blue', alpha=0.6,label='Overlap')
# ax.fill_between(x_as,real_values,generated_values,where,facecolor='blue',alpha=1)
# Set axes limits
plt.ylim(0, 100)
# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi
    if angle_rad == 0:
        ha, distance_ax = "center", 1
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 110 + distance_ax, cat[i], size=12, horizontalalignment=ha, verticalalignment="center")
plt.legend(bbox_to_anchor=(1.1, 1.1), loc='upper left', ncol=1)
# plt.legend()
plt.show()
# plt.set_size_inches(1000,600)
# plt.savefig('act_attr.png',dpi = 'figure')
plt.close()
'''
