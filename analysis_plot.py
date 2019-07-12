#!/usr/bin/env python
# coding: utf-8

# In[31]:


# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"


# In[ ]:


# rm(list = ls()) in R


# In[68]:


reset


# In[25]:


get_ipython().run_line_magic('pylab', 'inline')
get_ipython().run_line_magic('matplotlib', 'inline')
# 環境
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns


# In[65]:


X = list(range(1,10))
y = []
for x in range(1,10):
    y.append (x ** 3 - 2 * x +5)

print(y)
print(X)
plot(X, y)


# In[66]:


L = [3, 7, -5, 9]
G = [1, 2, 8, 8]
L + G
#  L - G error
print(L * 5)
print("hello world")
print("翊瑋是瘦子")
print("太后是胖子")


# In[29]:


grades = [77, 85, 60, 90, 66, 0, 88]
round(np.mean(grades), 2)


# In[30]:


grades = []
grades.append(77)
grades.append(85)
grades


# In[33]:


grades = []
for i in range(5):
    a = input("input number:")
    grades.append(a)


# In[34]:


grades


# In[35]:


from random import *
for i in range(50):
    print(randint(1, 10), end = ', ')


# In[36]:


from numpy.random import *
for i in range(50):
    print(randint(1, 10), end = ', ')


# In[37]:


prices = [1096.95, 596.95, 896.95]

usd2twd = 37.71
twd_prices = []
for price in prices:
    twd = price * usd2twd
    twd_prices.append(twd)
twd_prices


# In[38]:


import numpy as np
prices = np.array(prices)
prices * usd2twd


# In[39]:


A = np.random.rand(50)
A.shape


# In[40]:


x = np.linspace(start = 0, stop = 10, num = 100)
x
# help(np.linspace)
plt.subplot(221)
plt.plot(x, np.sin(x) + x)
plt.subplot(224)
plt.plot(x, np.cos(3*x))


# In[41]:


x = np.linspace(-5, 5, 200)
y = np.sinc(x)
plt.plot(x, y)
plt.plot(x[y > 0], y[y > 0], 'o')


# In[42]:


from IPython.display import YouTubeVideo
YouTubeVideo('WY6nQK7zbsk')


# In[43]:


x = np.linspace(0, 10, 200)
y = np.sin(5*x) / (1 + x ** 2)
plt.plot(x, y)


# ## 基本修飾
# |參數|說明|
# |---|---|
# |alpha|透明度 |
# |color (c)|顏色 |
# |linestyle (ls)|線條風格|
# |linewidth (lw)|線寬|
#
# ### 顏色表示法 1
#     c = 'r'
#
# 可以用 blue (b), green (g), red (r), cyan (c), magenta (m), yellow (y), black (k), white (w)
#
# ### 顏色表示法 2
# 用一個 0 到 1 的數字表灰階, 越大越白。
#
#     c = '0.6'
#
# ### 顏色表示法 3
# 網頁常用的標準 16 進位 RGB 表示法。
#
#     c = '#00a676'
#
# 我們怎知哪裡可選顏色呢? 可以用之前彥良介紹的 Coolors.co 等。
#
# ### 顏色表示法 4
# 用 0-1 的數字表 RGB 也可以。
#
#     c=(0.7, 0.4, 1)



plt.plot(x, y, c = '#00a676', lw = 5)


# In[45]:


x = range(20)
y = np.random.randn(20)
plt.plot(x, y, c = 'b', lw = 1, marker = 'o');


# ### marker 可以設的參數
# |參數|說明|
# |---|---|
# |marker|marker 的風格|
# |markeredgecolor (mec)|	邊線顏色|
# |markeredgewidth (mew)|	邊線寬度|
# |markerfacecolor (mfc)|	marker 的顏色|
# |markerfacecoloralt (mfcalt)|marker 替換色|
# |markersize (ms)|marker 大小|
# |markevery|	隔多少畫一個 marker|

# In[46]:


plt.plot(x, y, c='k', lw=5, marker='o', mfc='y', mec="g", mew=3, ms=10)


# In[47]:


x = np.linspace(0, 10, 200)
y = np.sin(5*x) / (1 + x ** 2)
plt.plot(x, y, marker = 'o', ms = 8, markevery = 10)


# In[48]:


plt.bar(range(1, 6), np.random.randint(1, 30, 5))


# In[49]:


np.random.seed(1234)
plt.bar(np.arange(0.6, 5), np.random.randint(1, 30, 5))
# np.arange(0.1, 7)
np.random.randint(1, 30, 5)


# In[50]:


x = np.arange(1, 6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width = 0.4, ec = 'none', fc = '#e63946')
plt.bar(x, [6, 3, 12, 5, 8], width = 0.4, ec = 'none', fc = '#7fb069')


# In[51]:


A = np.random.randint(2, 15, 5)
B = np.random.randint(2, 15, 5)
C = np.random.randint(2, 15, 5)
plt.bar(x, A, fc='#e63946', ec='none')
plt.bar(x, B, fc='#7fb069', ec='none', bottom = A)
plt.bar(x, C, fc='#e55934', ec='none', bottom = A+B)


# In[52]:


x = np.arange(0.6, 6)
plt.barh(x, np.random.randint(1,15,6), fc='#e55934', ec='none')


# In[53]:


x = np.arange(0.6, 6)
A = np.random.randint(1, 15, 6)
B = np.random.randint(1, 15, 6)
plt.barh(x, A, fc = '#e63946', ec = 'none')
plt.barh(x, -B, fc = '#7fb069', ec = 'none')


# # subplot 畫多個圖
# #### 我們每次畫圖的時候, matplotlib 就弄 1 個 figure 畫圖區出來, 裡面可以有很多子圖, 在 figure 裡叫 axes。目前我們都只有 1 個 figure 內含 1 張圖, 所以都不用設, 現在我想畫 4 張圖時。我們就要先想好「陣式」。
#
# ###### 類似R的 par(mfrow= c(2,2))
#
# #### 比如說 2x2 這樣排列的 4 張圖。

# In[54]:


x = np.linspace(0, 10, 100)

plt.subplot(221)
plt.plot(x, np.sin(x), c='#e63946', lw=3)

plt.subplot(222)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)

plt.subplot(223)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)

plt.subplot(224)
plt.bar(range(10), np.random.randint(1,30,10), fc='#e55934')


# In[55]:


x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
y = np.sin(x)
plt.title("My lovely sin function")
plt.xlabel('x-axes')
plt.ylabel('values')

plt.subplot(121)
plt.plot(x, y, lw = 5)
# 邊界的設定
plt.subplot(122)
plt.xlim(-6, 6)
plt.ylim(-1.2, 1.2)
plt.plot(x, y, c = 'y', lw = 5)


# In[56]:


# xticks
xv = np.linspace(0, 2*np.pi, 100)
yv = np.sin(xv)
plt.subplot(221)
plt.plot(xv, yv, lw = 3)
plt.subplot(222)
plt.plot(xv, yv, lw = 3)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
          ['$0$', '$\pi/2$', '$\pi$', '$-3\pi/2$', '$-2\pi$'])


# In[57]:


plt.xlim(-6, 6)
plt.ylim(-1.2, 1.2)
plt.plot(x, y, lw = 3, label = '$\sin$')
plt.plot(x, np.cos(x), lw = 3, label = '$\cos$')
plt.legend() # print label
plt.legend(loc = 4)


#
# ## 取得現在工作中 axes
# 我們有時要設 axes 的背景啦等等的資訊。這時就要取得現在工作中的 axes。這一般有兩種方式, 第一種是設 subplot 時可以取得:
#
#     fig, ax = plt.subplot()
#
# 另一種是用 gca 函數:
#
#     ax = plt.gca()

# In[58]:


ax = plt.gca()
ax.set_facecolor('pink')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)
plt.plot(x,y,lw=5,c='white')


# In[60]:


# 移動 x, y 座標軸
ax = plt.gca()
ax.set_facecolor('pink')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(x,y,lw=5,c='white')


# In[61]:


x = np.linspace(-10,10,200)
y = np.sinc(x)

plt.plot(x,y)


# In[62]:


# ↓↓↓ trans to .py ↓↓↓
get_ipython().system('jupyter nbconvert --to script analysis_plot.ipynb')


# In[ ]:
