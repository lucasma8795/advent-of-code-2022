from collections import deque

data = deque()
size_records = []

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size

class Directory:
	def __init__(self, name, parent=None):
		self.name = name
		self.children = []
		self.parent = parent

	def add_child(self, child):
		child.parent = self
		self.children.append(child)
	
	def get_child(self, name):
		for child in self.children:
			if isinstance(child, Directory) and child.name == name:
				return child

	def get_size(self):
		global size_records
		size = 0
		for child in self.children:
			if isinstance(child, File):
				size += child.size
			else:
				size += child.get_size()

		size_records.append((self.name, size))
		return size

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		line = line.strip().split(" ")
		data.append(line)

root = Directory("/")
cur_directory = root
while data:
	line = data.popleft()
	# list directory
	if line[1] == "ls":
		while True:
			if not data: break
			next_line = data[0]
			if next_line[0] == "$":
				break
			else:
				itemtype, name 	= data.popleft()
				if itemtype == "dir": # item is directory
					cur_directory.add_child(Directory(name))
				else: # item is a file; itemtype is its size
					cur_directory.add_child(File(name, int(itemtype)))
	# goto directory
	elif line[1] == "cd":
		goto = line[2]
		if goto == "..":
			cur_directory = cur_directory.parent
		else:
			cur_directory = cur_directory.get_child(goto)

root.get_size()
ans = 0
for name, size in size_records:
	if size <= 100000:
		ans += size
print(ans)