import numpy as np

def calculate(list):

    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    else:
        x=np.array(list).reshape(3,3)
  
    mean_list=[x.mean(axis=0).tolist(),x.mean(axis=1).tolist(),x.mean().tolist()]
    var_list=[x.var(axis=0).tolist(),x.var(axis=1).tolist(),x.var().tolist()]
    std_list=[x.std(axis=0).tolist(),x.std(axis=1).tolist(),x.std().tolist()]
    max_list=[x.max(axis=0).tolist(),x.max(axis=1).tolist(),x.max().tolist()]
    min_list=[x.min(axis=0).tolist(),x.min(axis=1).tolist(),x.min().tolist()]
    sum_list=[x.sum(axis=0).tolist(),x.sum(axis=1).tolist(),x.sum().tolist()]
    calculations={'mean':mean_list,'variance':var_list,'standard deviation':std_list,'max':max_list,'min':min_list,'sum':sum_list}


    return calculations