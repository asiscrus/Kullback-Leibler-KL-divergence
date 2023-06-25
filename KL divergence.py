# Creating a class for the Kullback–Leibler (KL) divergence from Information theory
def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))