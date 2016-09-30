from id_from_username import IdFromUsername
from friends import Friends
import matplotlib.pyplot as plot

uname = input('Имя пользователя: ')
uclient = IdFromUsername(uname)
uid = uclient.execute()

friends_client = Friends(uid)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))

fig, ax = plot.subplots()
rects = ax.bar(list(map(lambda x: x[0], friends)), list(map(lambda x: x[1], friends)), 1)

plot.xlabel('Возраст')
plot.ylabel('Кол-во')
plot.title('Распределение друзей по возрастам')
plot.subplots_adjust()
plot.show()