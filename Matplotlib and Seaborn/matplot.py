import matplotlib.pyplot as plt

#Data
# months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# sales=[45,52,34,78,69,75,68,90,95,82,90,99]

# #Line Chart
# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker='o',color='steelblue',linewidth=2,markersize=8)
# plt.fill_between(months,sales,alpha=0.15,color='steelblue')
# plt.title('Monthly sales 2024 (Rs.Thousands)',fontsize=14,fontweight='bold')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs. K)')
# plt.grid(True,alpha=0.3)
# plt.tight_layout()
# plt.show()

#BAR chart Example
# cities=['Bhopal','Indore','Jabalpur','Singrauli','Katni']
# students=[1200,2800,980,850,650]
# colors=['blue','green','orange','pink','red']

# #Bar chart-comparing categories
# plt.figure(figsize=(9,5))
# bars=plt.bar(cities,students,color=colors,edgecolor='black',linewidth=1.5)
# plt.title('Students Enrolled per city')
# plt.ylabel('Number of Students')
# plt.xlabel('Cities')
# for bar,val in zip(bars,students):
#     plt.text(bar.get_x()+bar.get_width()/2,val+30,str(val),ha='center',fontweight='bold')
# plt.tight_layout()
# plt.show()

#SCATTER PLOT - relationship between two variables
import numpy as np
study_hrs=np.random.uniform(2,10,50)
marks=study_hrs * 7 +np.random.normal(0,8,50)
marks=np.clip(marks,30,100)

plt.figure(figsize=(8,5))
plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn',s=100,alpha=0.8)
plt.colorbar(label='Marks')
plt.title('Study hours vs Exam Marks')
plt.xlabel('Study hours/day')
plt.ylabel('Exam Marks')
plt.show()
