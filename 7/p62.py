import p60


model = p60.read_vectors()
print(model.most_similar('United_States', topn=10))
