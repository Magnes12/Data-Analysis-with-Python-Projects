import numpy as np

list = [9,1,5,3,3,3,2,9,0]

output = {
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

def calculate(list):
    a = np.array(list)
    b = np.reshape(a, (3, 3))
    
    calculations = {
        'mean': [b.mean(axis=0).tolist(), b.mean(axis=1).tolist(), float(b.mean())],
        'variance': [b.var(axis=0).tolist(), b.var(axis=1).tolist(), float(b.var())],
        'standard deviation': [b.std(axis=0).tolist(), b.std(axis=1).tolist(), float(b.std())],
        'max': [b.max(axis=0).tolist(), b.max(axis=1).tolist(), int(b.max())],
        'min': [b.min(axis=0).tolist(), b.min(axis=1).tolist(), int(b.min())],
        'sum': [b.sum(axis=0).tolist(), b.sum(axis=1).tolist(), int(b.sum())]
    }
    return calculations
    
calculate(list)