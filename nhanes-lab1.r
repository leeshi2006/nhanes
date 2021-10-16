library(copent)
library(lattice)

load("lab1.rdata")
n = dim(csv1)[2]

mxce1 = matrix(0, n, n)
len = 1000
for (i in 1:n){
  for(j in i:n){
    data1 = csv1[1:len,c(i,j)]
    data1[,1] = data1[,1] + max(abs(data1[,1])) * 0.00005 * runif(len)
    data1[,2] = data1[,2] + max(abs(data1[,2])) * 0.00005 * runif(len)
    mxce1[i,j] = copent(data1)
    mxce1[j,i] = mxce1[i,j]
    str1 = paste("(",i,",",j,")")
    print(str1)
  }
}

levelplot(mxce1, xlab = '', ylab = '')
