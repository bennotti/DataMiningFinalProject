__author__ = 'miao guo'

import math
from sklearn import preprocessing

def calc_dist(X1, X2):
    """
    Calculate the Euclidean distance between the two given vectors
    :param X1: d-dimensional vector
    :param X2: d-dimensional vector
    :return: Euclidean distance between X1 and X2
    """
    dist = 0
    for i in range(len(X1)):
         dist = math.pow(X1[i]-X2[i],2) + dist

    dist = math.sqrt(dist)

    return dist


class Knn():
    """
    This defines the kNN algorithm.
    """

    def __init__(self, k):

        self.k = k
        self.scaler = None


    def normalize(self, data):
        """
        Initializes self.scaler and returns a normalized version of the data
        :param data:
        :return:
        """

        self.scaler = preprocessing.MinMaxScaler()
        return self.scaler.fit_transform(data)



    def predict(self, train_data, test_data, train_label):

      #print train_data
      train_data = self.normalize(train_data)

      test_data = self.normalize(test_data)
      results = []

      for X1 in test_data:
          dists = []
          index = 0

          for X2 in train_data:
              dist = calc_dist(X1,X2)
              dists.append((dist,train_label[index]))
              index += 1

          dists.sort()
          labels = [x[1] for x in dists[:self.k]]
          result = max(set(labels),key = labels.count)
          results.append(result)
      return results




