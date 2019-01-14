import sys, os
import numpy as np

from models import loadData
from models import models

def predict(data_npy, weightPath):
    
    data = loadData.formatData(data_npy)
    
    model = models.loadModel(weightPath)

    predicted = model.predict(np.array([data]))

    return np.argmax(predicted)
