import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1,2,1)
x=[1,3,5,7,9]
y=[6,3,1,8,5]
plt.plot(x,y)

plt.subplot(1,2,2)
x=[1,3,5,7,9]
y=[5,3,8,9,9]
plt.plot(x,y)

plt.subplot(1,3,3)
x=[1,3,5,7,9]
y=[5,3,8,9,9]
plt.plot(x,y)

plt.show
