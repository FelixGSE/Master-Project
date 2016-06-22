class auxilliary:
	
	def entropy(self,list_of_lists):
		entropies = []
		for lis in list_of_lists:
			entropy = []
			for i in range(len(lis)):
				subset = lis[:i+1]
				freq = [subset.count(p) for p in subset]
				freqset = dict(zip(lis,freq)).values()
				probs = [x / float(sum(freqset)) for x in freqset]
				entropy.append(-sum([x * np.log2(x) for x in probs]))
			entropies.append(entropy)
		return entropies

	def entropy_block(self,list_of_lists,no_bin=10):
		entropies = []
		avg_size = len(list_of_lists[0])/no_bin
		for lis in list_of_lists:
			entropy = []
			for i in range(no_bin):
				subset = lis[i*avg_size:(i+1)*avg_size]
				freq = [subset.count(p) for p in subset]
				freqset = dict(zip(subset,freq)).values()
				probs = [x / float(sum(freqset)) for x in freqset]
				entropy.append(-sum([x * np.log2(x) for x in probs]))
			entropies.append(entropy)
		return entropies

	def read_csv(self,name,delimiter = '\t',quotechar='|'):
		with open(name, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
			file = list(reader)
			final = []
			for item in file:
				sub = []
				for character in item:
					sub.append(int(character))
				final.append(sub)
		return final

	def read_csv2(self,name,delimiter = '\t',quotechar='|'):
		with open(name, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
			file = list(reader)
			final = [int(i[0]) for i in file ]
		return final

	def subset_data(self,list_of_list,list_of_labels,labels_to_find,healthy_list = None, n = None):
		ordered_subset = []
		for label in labels_to_find:
			indices = [i for i, x in enumerate(list_of_labels) if x == label ]
			items = [ list_of_list[index] for index in indices ]
			ordered_subset= ordered_subset + items
		if healthy_list is not None:
			if n == None:
				n = len(ordered_subset)
			nrows = len(healthy_list)
			new_indices = rd.sample(range(nrows), n )
			additional_items = [ healthy_list[index] for index in new_indices ]
			ordered_subset = ordered_subset + additional_items
		return ordered_subset

	def avg(self,list_of_list):
		lol_avg=[]
		avg_size = len(list_of_list[0])/10
		for ind in list_of_list:
			avg_ind = []
			for i in range(10):
				avg_ind.append(np.mean(ind[i*avg_size:(i+1)*avg_size]))
			lol_avg.append(avg_ind)
		return lol_avg

	def labels(self,list_of_labels,labels_to_find, n = None, healthy=True):
		labelset = []
		for label in labels_to_find:
			indices = [i for i, x in enumerate(list_of_labels) if x == label ]
			items = [ list_of_labels[index] for index in indices ]
			labelset = labelset + items
		if healthy == False:
			return labelset
		if n == None:
			labelset = labelset + [66]*len(labelset)
		else:
			labelset = labelset + [66]*n
		return labelset

	def avg_bad(self,list_of_list,no_bin=10,ch1=1,ch2=2):
		lol_avg=[]
		avg_size = len(list_of_list[0])/no_bin
		for ind in list_of_list:
			avg_ind = []
			for i in range(no_bin):
				avg_ind.append((ind[i*avg_size:(i+1)*avg_size].count(ch1) + \
					ind[i*avg_size:(i+1)*avg_size].count(ch2)) / float(avg_size))
			lol_avg.append(avg_ind)
		return lol_avg

	def avg_bad_multi(self,list_of_list,no_bin=10,n=2):
		lol_avg=[]
		avg_size = len(list_of_list[0])/no_bin
		for ind in list_of_list:
			avg_ind = []
			for i in range(no_bin):
				avg_ind.append(1 - (ind[i*avg_size:(i+1)*avg_size].count(n) / float(avg_size)))
			lol_avg.append(avg_ind)
		return lol_avg

	def jload(self,name):
			with open(name) as file:
				file_content = file.read()
				full_file = json.loads(file_content)
			return full_file

	def rep(self, item, n ):
		new = []
		for i in range(n):
			new.append(item)
		return new

	def column(self, matrix, i):
		return [row[i] for row in matrix]

	def avg_bad_cum(self,list_of_list, ch1=1, ch2=2):
		lol_avg = []
		for lis in list_of_list:
			ind = []
			for i in range(len(lis)):
				subset = lis[:i+1]
				ind.append((subset.count(ch1) + subset.count(ch2)) / float(len(subset)))
			lol_avg.append(ind)
		return lol_avg

	def setdiff(self,first_list,second_list):
		# Compute the difference in sets - Erase stuff that is both the first and the secon
		difference = list(set(first_list) - set(second_list))

		# Return the remaining items in list one
		return difference

	def summary_df(self,list_of_frames,col_list):

		# Subset names
		full_names = list_of_frames[0].columns
		# Define names which are excluded from summary

		# Compute data frame with those columns
		df01 = list_of_frames[0].ix[:,:9]

		# Compute summary for measure columns
		df02 = self.statistics_df(list_of_frames,col_list)

		# Compute final data frame
		temp_data_frame = pd.concat([df01,df02],axis=1)

		rankings = self.rankings_df(temp_data_frame)

		final_data_frame = pd.concat([temp_data_frame,rankings],axis=1)

		# Return results
		return final_data_frame


	def statistics_df(self,list_of_frames,cols):

		# Filter from all data frames columns with measures
		new_frames = self.filter_df(list_of_frames,cols)

		# Concat all measure columns from list of frames
		big_df  = pd.concat(new_frames)

		# Compute the mean and standard deviations
		grouped_mean = big_df.groupby(level=0).mean()
		grouped_sd   = big_df.groupby(level=0).std()

		# Concat results and rename columns
		final_frame = pd.concat([grouped_mean,grouped_sd],axis=1)
		names = ['MI-M','ADMI-M','NMI-M','ARI-M','CO-M','HO-M','VM-M',
				 'MI-S','ADMI-S','NMI-S','ARI-S','CO-S','HO-S','VM-S']
		final_frame.columns = names

		# Return data frame with summary
		return final_frame

	def filter_df(self,list_of_frames,list_of_columns):

		# Initialize list for filtered data frames
		new_frames = []

		# Subset from each data frame the column according to arguments
		for frame in list_of_frames:
			temp_df = frame[list_of_columns]
			new_frames.append(temp_df)

		# Return new list of data frames
		return new_frames


	def rankings_df(self,dframe,p_len = 53, sim_size = 6):
		temp_names = ['MI-MR','ADMI-MR','NMI-MR','ARI-MR','CO-MR','HO-MR','VM-MR']
		rank_frame = pd.DataFrame(0,index=np.arange(dframe.shape[0]),columns=temp_names)
		for step in range(sim_size):
			for i in range(9,16):
				rank_frame.ix[:,i-9][step*p_len:(step+1)*p_len]=dframe.ix[:,i][step*p_len:(step+1)*p_len].rank(method="min",ascending=False)
		return rank_frame



