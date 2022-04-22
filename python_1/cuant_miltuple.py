import sys
import math
from  contextlib import *
def compute_multiples_sum(n):
    for i in range(n) :
      if 0<=n<=100 :
          sum=0
          for i in range(n) :
              if i <n  :
               if  i % 3==0 :
                sum=sum+i
               elif i % 5 == 0:
                   sum = sum + i
               elif i % 7 == 0:
                       sum = sum + i
          return sum
print(compute_multiples_sum(15))