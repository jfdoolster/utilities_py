import numpy as np

def polynomial_regression(x_arr: np.ndarray, y_arr: np.ndarray, power=1, force_zero=False, y_offset=0.0):

    x_arr.shape = (len(x_arr),)
    y_arr.shape = (len(y_arr),1)

    x_lists = [np.ones((len(x_arr),))]
    if force_zero:
        x_lists = []

    for i in range(1,power+1):
        x_lists.append(x_arr**i)

    x_mat = np.vstack(x_lists)
    x_mat = np.transpose(x_mat)

    x_mat_prime = np.transpose(x_mat)
    x_cross_xprime = np.matmul(x_mat_prime, x_mat)
    xx_determinant = np.linalg.det(x_cross_xprime)

    if xx_determinant == 0.0:
        print("Singluar Matrix!")
        return np.empty((power+1,1)), np.empty((len(y_arr),1))

    xx_inv = np.linalg.inv(x_cross_xprime)
    xx_cross_xp = np.matmul(xx_inv, x_mat_prime)

    beta = np.matmul(xx_cross_xp, y_arr - y_offset)
    beta.shape = (len(beta), 1)

    yhat = np.matmul(x_mat, beta) + y_offset

    if force_zero:
        beta = np.insert(beta, 0, 0, axis=0)

    return beta, yhat

def calc_Rsquared(y_data: np.ndarray, y_hat:np.ndarray):
    # https://en.wikipedia.org/wiki/Partition_of_sums_of_squares
    y_bar:float = np.sum(y_data)/len(y_data)
    ssreg:float = np.sum((y_hat  - y_bar)**2)
    ssres:float = np.sum((y_hat - y_bar)**2)
    sstot:float = np.sum((y_data - y_bar)**2)
    return float((ssreg/sstot))


    #ESS:float = np.sum(np.square(y_hat  - y_bar))
    #TSS:float = np.sum(np.square(y_data - y_bar))
    #RSS:float = np.sum(np.square(y_data - y_hat))
    #Stot:float = ESS + RSS
    #Sres:float = RSS
    #print(TSS, Stot)
    #R2:float = 1 - (Sres/Stot)
    #return R2


