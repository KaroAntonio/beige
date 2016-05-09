import json

fids = ['top-1m']
lines = {}
for fid in fids:
	lines[fid] = []
	with open('assets/' + fid + '.csv','r') as file:
		for line in file:
			line = line.split(',')[1].strip()[:-4]
			lines[fid] += [line]
		break

with open ('assets/lines.json','w') as out:
	json.dump(lines,out)
