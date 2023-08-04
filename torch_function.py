from sklearn.metrics import precision_recall_fscore_support
import logging
import numpy as np
y_true = np.array([0,0,0,1,1])
y_pred = np.array([1,1,1,1,1])
result = precision_recall_fscore_support(y_true, y_pred, average='binary',pos_label=1)
logging.basicConfig(level=logging.INFO)
logging.info(result)