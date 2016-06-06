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
					ind[i*avg_size:(i+1)*avg_size].count(ch2)) / float(10))
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