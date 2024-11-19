from collections import deque

my_list= []
my_list.append('Comer')
my_list.append('Estudar mais')
my_list.append('Se eu não estudar vou morrer burro e pobre')


i = my_list.index('Se eu não estudar vou morrer burro e pobre')
my_list.insert(i, 'Jantar')  


print(my_list)

queue = deque(my_list)
queue.append('lavar o carro')
print(queue.popleft(), '- done!')
my_list_upd = list(queue)





