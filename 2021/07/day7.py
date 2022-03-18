data = [int(x) for x in open('input.txt').read().split(",")]
sorted_data = sorted(data)
median = sorted_data[len(sorted_data)//2]
print(sum([abs(x-median) for x in data]))
