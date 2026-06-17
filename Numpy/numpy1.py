import numpy as np     #importing numpy libraries in this file and np is a variable and as = alias

# arr1d=np.array([1,2,3,4,5])
# arr2d=np.array([[85,65,74],[96,67,89],[56,86,96]])      #3 students x 3 subjects
 
# print(arr2d.shape)      #3,3
# print(arr2d.dtype)      #int64 ----->datatype
# print(arr2d.ndim)       #2(2-dimensional)

# zeros=np.zeros((3,4))      # 3x4 array of 0s
# print(zeros)

# ones=np.ones((2,5))         #2x5 array of 1s
# print(ones)

# rng=np.arange(0,50,5)      #[0,5,10,15------,45]
# print(rng)

# lin=np.linspace(0,1,11)     
# print(lin)

# random=np.random.randint(40,100,(5,3))     #pick random no. between 40 and 100 and array of 5x3
# print(random)


# arr=np.array([10,20,30,40,50])

# print(arr * 2)     #each element multiply by 2
# print(arr + 5)
# print(arr ** 2)

# marks_2d=np.array([[85,64,76],[72,89,95],[91,76,83]])

# print(np.mean(marks_2d))    # overall mean

# print(np.mean(marks_2d,axis=1))     #mean per student (row)

# print(np.mean(marks_2d,axis=0))     #mean per subject (column)

# print(np.max(marks_2d))

# print(np.std(marks_2d))           #Standard deviation

#Boolean Indexing
arr=np.array([55,82,43,91,70,35,88])

print(arr[arr>70])    
