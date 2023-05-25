import sys
import re

args = sys.argv

#print(args[0])
#print(args[1])
#print(args[2])

a = args[1]
md = re.sub('.md', '', a)
md = re.sub('^.*_', '', md)

d = '/home/tmp_github/hatenablog_push/articles/'
f = open(d + args[1], 'r', encoding='UTF-8')

data = f.read()
#data = data.replace('title: "', '').replace('---\n', '')
data = re.sub('---\n', '', data)
data = re.sub('title: ', '', data)
data = re.sub('"\n', '\n', data)
data = re.sub('", "', ',', data)
data = re.sub('emoji: .*\n', '', data)
data = re.sub('type: .*\n', '', data)
data = re.sub('topics: \[', '', data)
data = re.sub('\]', '', data)
data = data.replace('published: true', md)
print(data)

f.close()
