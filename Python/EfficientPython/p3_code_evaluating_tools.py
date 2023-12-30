# %% [markdowm]
# Tools for Evaluating Codes

# We have learned how to improve our code with more pythoninc tricks, now we will to learn how to verify if our changes are faster indded.
# In this section we could use Ipython magig commands to calculate runtime.
# To calculate the runtime use:
# - %timeit when you have just one row of code
# - %%timeit when you have multiple rows of code
# - `-r` to set the numbers of runs
# - `-n` to set the numbers of loops

# %%
import sys
from p3_module_test import simulate
import numpy as np
import timeit

%timeit rand = np.random.rand(500)

%timeit - r3 - n5 rand2 = np.random.rand(1000)

# %%
% % timeit
names = ["Jose", "Maria", "Tõe", "Creuza"]
# Time to run a non pythonic code
big_names = []
for name in names:
    if len(name) > 4:
        big_names.append(name)

# %%
timeit.timeit()
par_values = [n for n in range(1, 10) if n % 2 == 0]
par_values
timeit.timeit()
# %%

# %%
inicio = timeit.default_timer()
par_values = [n for n in range(1, 10) if n % 2 == 0]
par_values
fim = timeit.default_timer()
print('>>>>> Tempo execução função fatorial: %f' % (fim - inicio))

# %%
% % timeit
# time to run a pythonic code
names = ["Jose", "Maria", "Tõe", "Creuza"]

big_names = [name for name in names if len(name) > 4]

# %%
# to save the time from a variable

times = %timeit - o rand = np.random.rand(500)
times
# %%
# Now we can use some methods to compare runtimes

# times.timing - list of times saved
# times.best - best time saved
# times.worst - worst time saved

# Lets to create two dicst and to compare the time difference

time_one = %timeit - o dict_formal = dict()

time_two = %timeit - o dict_informal = {}

# comparing runtime for this methods
diff = (time_one.average - time_two.average) * 10**9
print("The diffrence it: {}".format(diff))
# %% [markdown]

# Code Profilling for Runtimes

# Sometimes we must evaluate how long a code is running and how often this code is called. To do this with the line_profiler is a good option in Python.

# %%
# load the profiler in the session
%load_ext line_profiler

# use the lprun, -f flag to tell your are timming a function
# tell the function name, and then use the function as usuall
%lprun - f simulate simulate(100)
# %%

# Memory usage
num_list = [*range(1000)]
sys.getsizeof(num_list)
