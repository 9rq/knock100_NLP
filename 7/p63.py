import p60


model = p60.read_vectors()

vector = model['Spain'] - model['Madrid'] + model['Athens']
print(vector)
print(model.most_similar(positive= ['Spain', 'Athens'], negative=['Madrid'], topn = 10))
