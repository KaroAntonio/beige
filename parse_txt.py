import json

poem_titles = ['raw']
poems = {}
for title in poem_titles:
    f = open('assets/'+title+'.txt')
    lines = []
    
    for line in f:
        lines.append(line)
    poems[title] = lines
    f.close()
    
with open('assets/lines.json', 'w') as outfile:
    json.dump(poems, outfile)
    
