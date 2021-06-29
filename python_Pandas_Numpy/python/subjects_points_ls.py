subjects_ls = ["korean","english","math"]
points_ls = [80,90,100]
points_dict = {"korean": 80, "english": 90, "math":100}

total, avg =0, 0

datas = points_ls.copy()

while datas:
	total += datas.pop()
avg = total / len(points_ls)
total, avg
