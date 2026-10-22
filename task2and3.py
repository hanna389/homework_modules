import mymodule as mm
import random
import datetime

mm.hi()
print(mm.name)
res = mm.add_3_numbers(1, 7, 4)
print("сума 3 чисел: ", res)

random_number = random.randint(0, 10)
print("Випадкове число від 0 до 10:", random_number)

current_time = datetime.datetime.now()
print("Поточна дата і час: ", current_time)