
import numpy as np

def sample_stats(arr: np.ndarray) -> tuple[float, float, int]:
    n = len(arr)
    mean = np.mean(arr)
    std = np.std(arr)

    return mean, std, n
