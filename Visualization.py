import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from numpy import *

array = loadtxt("hbond.txt")
x=len(array[0])
df_cm = pd.DataFrame(array, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size

plt.savefig('/Users/Tim/Desktop/hbond.png')

plt.figure()

array2 = loadtxt("/vbond.txt")

df_cm = pd.DataFrame(array2, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size
plt.savefig('/Users/Tim/Desktop/vbond.png')

plt.figure()

array3 = loadtxt("bru.txt")

df_cm = pd.DataFrame(array3, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size

plt.savefig('/Users/Tim/Desktop/bru.png')

plt.figure()

array5 = loadtxt("elas.txt")

df_cm = pd.DataFrame(array5, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size

plt.savefig('elas.png')

plt.figure()

array4 = loadtxt("full.txt")

df_cm = pd.DataFrame(array4, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size
plt.savefig('full.png')

plt.figure()

array8 = loadtxt("/loops.txt")

df_cm = pd.DataFrame(array8, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size

plt.savefig('loops.png')

plt.figure()

array9 = -array4 + array5

df_cm = pd.DataFrame(array9, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10},vmax=2)# font size

plt.savefig('comb.png')

plt.figure()

array10 = array5 + array8

df_cm = pd.DataFrame(array10, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10},vmax=3)# font size

plt.savefig('combgr.png')

plt.figure()

array11 = loadtxt("blobs.txt")

df_cm = pd.DataFrame(array11, range(x), range(x))

sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 10})# font size

plt.savefig('blobs.png')
