# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:09:16 2018

@author: Administrator
"""
import random as rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster, datasets, metrics
from sklearn.cluster import KMeans
data = pd.read_csv("C:/Users/Administrator/Desktop/data.csv")
rd.seed(1111)
print(data.head(3))
print(data.shape)

silhouette_avgs = []
ks = range(2, 11)
for k in ks:
    kmeans_fit = cluster.KMeans(n_clusters = k).fit(data)
    cluster_labels = kmeans_fit.labels_
    silhouette_avg = metrics.silhouette_score(data, cluster_labels)
    silhouette_avgs.append(silhouette_avg)
    
print(silhouette_avgs)
plt.bar(ks, silhouette_avgs)
#K=2
km = KMeans(n_clusters = 3)
y_pred = km.fit_predict(data)
plt.figure(figsize=(10, 6))
plt.xlabel('x1')
plt.ylabel('x2')
plt.scatter(data.iloc[:,0], data.iloc[:, 1], c=y_pred) #C是第三維度 已顏色做維度
plt.show()

new_value = [170, 50]
(sum((km.cluster_centers_[0]-new_value)**2))**(1/2) #紫色
(sum((km.cluster_centers_[1]-new_value)**2))**(1/2) #綠色
(sum((km.cluster_centers_[2]-new_value)**2))**(1/2) #黃色

print(km.cluster_centers_[2])
