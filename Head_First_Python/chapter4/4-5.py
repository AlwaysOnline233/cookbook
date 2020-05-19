# pickle模块
# dump保存 load恢复

import pickle
import chapter2.nester

new_man =[]

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error:' + str(err))
except pickle.PickleError as perr:
    print('Pickling Error:'+str(perr))

a = chapter2.nester.print_lol(new_man)
print('————————————————————————')
print(new_man[0])
print(new_man[-1])