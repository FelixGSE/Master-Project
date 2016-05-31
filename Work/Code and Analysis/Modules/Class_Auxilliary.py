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

	def subset_data(self,list_of_list,list_of_labels,labels_to_find):
		ordered_subset = []
		for label in labels_to_find:
			indices = [i for i, x in enumerate(list_of_labels) if x == label ]
			items = [ list_of_list[index] for index in indices ]
			ordered_subset = ordered_subset + items 
		return ordered_subset





