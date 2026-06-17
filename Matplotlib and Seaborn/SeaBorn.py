import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
#Data
df=pd.DataFrame({
    'marks':      np.random.randint(40,100,100),
    'study_hours':np.random.uniform(2,10,100),
    'city':       np.random.choice(['Bhopal','indore','Jabalpur'],100),
    'gender':     np.random.choice(['Male','Female'],100)

})

#Histogram with KDE - see the distribution
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'],bins=20,kde=True,color='pink')
# plt.title('Distribution of Student Marks')
# plt.show()

# Box plot
# sns.boxplot(data=df,x='city',y='marks',palette='Set2')
# plt.title('Marks Distribution by city')
# plt.show()

# Correlation heatmap - critical in data science
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='coolwarm',vmin=1,vmax=1)
# plt.title('Correlation Matrix')
# plt.show()

# Pair plot
sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
plt.show()