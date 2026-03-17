# Answers to questions in the Profiling excercises

#### a. Investigate the performance of the ```matmult.py``` script
In which line(s) of the script would you start optimizing for speed?
- Probably the lines 11 and 16 that are the 'append' lines because it has the biggest time per hit.

#### b. Investigate the performance of the ```euler72.py``` script
In which line(s) of the script would you start optimizing for speed?
(This is one problem from the euler project: [https://projecteuler.net/problem=72](https://projecteuler.net/problem=72))
- Probably in the factorize function due to be associated with the biggest run time among all functions.

#### c. Improve the performance of the ```matmult.py``` script
What is the best performance that you achieved with N=250?
- A total time of: 0.0787547 that can be check at 'matmult_optimized.py.lprof'. 
