
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)
