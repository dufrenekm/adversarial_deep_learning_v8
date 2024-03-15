import numpy as np
import matplotlib.pyplot as plt

# Generate some dank plots for our presentation

# Map 50-96
clean95             =np.array([ 0.753 ,      0.609      ,     0.564      ,  0.643])
watermelon95        =np.array([ 0.698 ,      0.735      ,     0.572      ,  0.626])
copy95         =np.array([ 0.674 ,      0.600      ,     0.728      ,  0.629])
stop95         =np.array([ 0.704 ,      0.611      ,     0.594      ,  0.741])
c50_5095   =np.array([ 0.726 ,      0.615      ,     0.675      ,  0.651])
c70_3095   =np.array([ 0.754 ,      0.665      ,     0.751      ,  0.696])
c30_7095   =np.array([ 0.775 ,      0.674      ,     0.717      ,  0.709])

# mAP 50
clean50             =np.array([ 0.886 ,      0.806      ,     0.743      ,  0.810])
watermelon50        =np.array([ 0.865 ,      0.896      ,     0.745      ,  0.827])
copy50         =np.array([ 0.847 ,      0.797      ,     0.881      ,  0.818])
stop50         =np.array([ 0.879 ,      0.792      ,     0.771      ,  0.894])
c50_5050   =np.array([ 0.880 ,      0.798      ,     0.829      ,  0.822])
c70_3050   =np.array([ 0.906 ,      0.851      ,     0.899      ,  0.868])
c30_7050   =np.array([ 0.915 ,      0.855      ,     0.888      ,  0.877])

X = ['Clean', 'Copyright', 'Watermelon', 'Stop Sign']
X_axis = np.arange(len(X))*1.2


plt.figure(figsize=(8,6))

plt.bar(X_axis, clean50, label='Clean Model')

'''plt.bar(X_axis - 0.4, clean95, 0.2, label = 'Clean Model') 
plt.bar(X_axis - 0.2, copy95, 0.2, label = 'Copyright Model') 
plt.bar(X_axis - 0.0, c50_5095, 0.2, label = '50/50 Model') 
plt.bar(X_axis + 0.2, c70_3095, 0.2, label = '70/30 Model') 
plt.bar(X_axis + 0.4, c30_7095, 0.2, label = '30/70 Model') '''


'''plt.bar(X_axis - 0.4, clean50, 0.2, label = 'Clean Model') 
plt.bar(X_axis - 0.2, copy50, 0.2, label = 'Copyright Model') 
plt.bar(X_axis - 0.0, c50_5050, 0.2, label = '50/50 Model') 
plt.bar(X_axis + 0.2, c70_3050, 0.2, label = '70/30 Model') 
plt.bar(X_axis + 0.4, c30_7050, 0.2, label = '30/70 Model') '''
plt.ylim([0,1])

plt.title('mAP50 on Adversarial Images')
plt.xticks(np.arange(len(X))*1.2, X)
plt.xlabel('Validation Image Sets')
plt.ylabel('mAP50')

plt.legend(loc='upper right')

plt.show()