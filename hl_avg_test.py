'''
Pim
higher or lower card game average game length simulation
'''

import random as r
import matplotlib.pyplot as plt

r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(sum(r_list)/len(r_list))
empt_avg_score_list = []

def rng():
	global r_list
	rn_pos1 = r.randint(1, len(r_list)-1)
	rn_start = r_list[rn_pos1]
	r_list.pop(rn_pos1)
	rn_pos2 = r.randint(1, len(r_list)-1)
	rn_new = r_list[rn_pos2]
	r_list.pop(rn_pos2)
	return rn_start, rn_new


def main():
	# rn_start, rn_new = rng()
	global r_list
	# print(rn_start)
	# rn_start, rn_new = rng()
	i = 0
	while i < 100000:
		q = 0
		ln = 0
		rn_start, rn_new = rng()

		while q == 0:
			rn_start, rn_new = rn_start, rng()[1]
			# rn_start, rn_new = rng()
			lst_avg = sum(r_list)/len(r_list)
			print("start:", rn_start, "  new: ", rn_new)
			print(r_list)
			if rn_start >= lst_avg:
				if rn_start == rn_new:
					empt_avg_score_list.append(ln)
					r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
					q = 1
					i += 1
				elif rn_start > rn_new:
					ln += 1
					if len(r_list) <= 2:
						empt_avg_score_list.append(ln)
						r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
						q = 1
						i += 1
					else:
						pass
				else:
					empt_avg_score_list.append(ln)
					r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
					q = 1
					i += 1

			elif rn_start < lst_avg:
				if rn_start == rn_new:
					empt_avg_score_list.append(ln)
					r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
					q = 1
					i += 1
				elif rn_start < rn_new:
					ln += 1
					if len(r_list) <= 2:
						empt_avg_score_list.append(ln)
						r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
						q = 1
						i += 1
					else:
						pass
				else:
					empt_avg_score_list.append(ln)
					r_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
					q = 1
					i += 1

main()
print(empt_avg_score_list)
print("avg:", sum(empt_avg_score_list)/len(empt_avg_score_list))

# print(empt_avg_score_list.count(1))
empt_perc_list = []
j = 0
for j in range(max(empt_avg_score_list)+1):
	empt_perc_list.append(empt_avg_score_list.count(j))

print(empt_perc_list)
perc_listtt = []
k = 0
for k in range(max(empt_avg_score_list)+1):
	perc_listtt.append((empt_perc_list[k]/sum(empt_perc_list))*100)

# print(empt_perc_list)
print(perc_listtt)
plt.hist(empt_avg_score_list, bins = (max(empt_avg_score_list)*2)+1)
plt.hist(perc_listtt, bins = (max(perc_listtt)*2)+1)
# print(perc_listtt)
plt.show()
