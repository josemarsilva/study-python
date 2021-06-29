#
# filename   : lab-113-module-datetime-math-random-sys-time.py
# Description: Dictionary
# Docs       : * https://docs.python.org/3/library/
#              * https://docs.python.org/3/library/datetime
#              * https://docs.python.org/3/library/math
#              * https://docs.python.org/3/library/random.html
#

print('\n# 1. module (improved) - datetime\n')
import time
import datetime
print('dir(datetime): ', dir(datetime))                     # ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
print('datetime.date.today(): ', datetime.date.today())     # 2021-06-28
print('datetime.datetime.now(): ', datetime.datetime.now()) # 2021-06-28 20:33:21.683789
print('')
dt = datetime.date(2021, 6, 28)   # Atenção: não colocar 0 (zero) na frente do numero 6
print('dt      : ', dt)        # 2021-06-28
print('dt.year : ', dt.year)   # 2021
print('dt.month: ', dt.month)  # 6
print('dt.day  : ', dt.day)    # 28
print('')
dt_hr = datetime.datetime( 2021, 6, 28, 20, 41, 0)
print('dt_hr       : ', dt_hr)  # 2021-06-28 20:41:00
print('dt_hr.hour  : ', dt_hr.hour)    # 20
print('dt_hr.minute: ', dt_hr.minute)  # 41


print('\n# 2. module (improved) - math\n')
import math
print('math.sqrt(9): ', math.sqrt(9))   # 3
print('math.pi: ', math.pi)             # 3.141592653589793


print('\n# 3. module (improved) - random\n')
import random
print('random.random()         : ', random.random()) # 0.01947058069425911
print('random.random()         : ', random.random()) # 0.9924554989286543
print('random.randint(1,5)     : ', random.randint(1,5)) # random between 1 and 5
print('random.randrange(2,10,2): ', random.randrange(2,10,2)) # random pares entre 2 a 10
l1 = [ 'amarelo', 'azul', 'vermelho' ]
print('random.choice(list): ', random.choice(l1)) # sorteia um elemento da lista


print('\n# 4. module (improved) - sys\n')
import sys
l1 = list(range(1000))  # range(1000): [0,1,2, ... 999]
print('l1               :', l1)                # [0, 1, 2, .. , 9]
print('sys.getsizeof(l1): ', sys.getsizeof(l1)) # 9112 bytes memory


print('\n# 5. module (improved) - time\n')
import time as tm
print(tm.time())
tm_start = tm.time()
print('tm_start: ', tm_start)
l1 = []
for element in range(1,100):
    time.sleep(0.1)
    l1.append(element)

tm_finish = tm.time()
elapsed = tm_finish - tm_start
print('tm_start: ', tm_start)
print('tm_finish: ', tm_finish)
print(f'elapsed : {elapsed}')