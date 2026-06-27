import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maxz = np.max(z)
        shifted_exp = np.exp(z-maxz)
        sumz = np.sum(shifted_exp)
        ans = shifted_exp/sumz
        return np.round(ans,4)