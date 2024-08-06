import numpy as np

def polynomial_regression(x_arr:np.ndarray, y_arr:np.ndarray, power:int=1, force_zero:bool=False, y_offset:float=0.0) -> tuple[np.ndarray, np.ndarray]:

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

    beta:np.ndarray = np.matmul(xx_cross_xp, y_arr - y_offset)
    beta.shape = (len(beta), 1)

    yhat:np.ndarray = np.matmul(x_mat, beta) + y_offset

    if force_zero:
        beta = np.insert(beta, 0, 0, axis=0)

    return beta, yhat

def calc_Rsquared(y_data: np.ndarray, y_hat:np.ndarray) -> float:
    # https://en.wikipedia.org/wiki/Partition_of_sums_of_squares
    y_bar:float = np.sum(y_data)/len(y_data)
    ssreg:float = np.sum((y_hat  - y_bar)**2)
    ssres:float = np.sum((y_hat - y_bar)**2)
    sstot:float = np.sum((y_data - y_bar)**2)
    return float((ssreg/sstot))

def polynomial_new(x:np.ndarray, y:np.ndarray, degree:int):
    x.shape = (len(x),)

    if y.shape[0] != x.shape[0]:
        print(f"ERROR: incompatibile arrays! (x.shape={x.shape}, y.shape={y.shape})")

    #print(f"(x.shape={x.shape}, y.shape={y.shape})")

    p = np.polyfit(x, y, degree)

    xs = np.linspace(min(x), max(x), num=len(x))








