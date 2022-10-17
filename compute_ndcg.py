def compute_ndcg(scores, relevance, n=10):
    '''
      scores: list of products scores given by algorithm
              [100, 98, 95, 90, 67, 55, ... ]
      relevance: list of relevance for each index given by user
              [0, 1, 5, 0, 0, 2, ....] 
      n: number of top n items to compute ndcg on. 
    '''
    scores = list(map(float,scores))
    relevance = list(map(float, relevance))
    array = list(zip(scores, relevance))
    dcg_array = sorted(array, key = lambda x:x[0], reverse = True)[:n]
    idcg_array = sorted(dcg_array, key = lambda x:x[1], reverse = True)
    dcg = 0
    for i, (_, rel) in enumerate(dcg_array):
        dcg += (2**rel - 1)/np.log2(i+2)
    idcg = 0
    for i, (_, rel) in enumerate(idcg_array):
        idcg += (2**rel - 1)/np.log2(i+2)

    ndcg = dcg/(idcg+1e-6)
    return float(ndcg)
