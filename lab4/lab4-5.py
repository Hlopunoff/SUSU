soldiers = {}

for i in range(5):
    information = input().split(' ')
    soldiers['{0} {1} {2}'.format(*information[:3])] = '{0} {1}'.format(*information[3:])

print('Фамилия\t\t\tИмя\t\t\t\tОтчество\t\tГод рождения\tЗаболевание')
for key in soldiers.keys():
    print('{:<15} {:<15} {:<15} {:<15} {:<15}'.format(*key.split(' '), *soldiers[key].split(' ')))