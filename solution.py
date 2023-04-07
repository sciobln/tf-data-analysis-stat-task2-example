import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 477540310 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    M = (x**2).sum()/n
    scale = np.sqrt(M / 23)
    return scale * np.sqrt(chi2.ppf(1 - alpha / 2, 2*n)), \
           scale * np.sqrt(chi2.ppf(alpha / 2, 2*n))
