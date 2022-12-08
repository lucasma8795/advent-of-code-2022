from collections import deque

data = deque()
sizes = []

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
	
	def get_directory(self, name):
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

		sizes.append(size)
		return size

with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		line = line.strip().split(" ")
		data.append(line)

root = Directory("/")
cur_directory = root
while data:
	line = data.popleft()
	assert line[0] == "$" # is a command

	# list directory
	if line[1] == "ls":
		while True:
			if not data: break # deque is empty
			next_line = data[0] # peek at leftmost element of deque
			if next_line[0] == "$": break # next line is a command

			itemtype, name 	= data.popleft() # e.g. dir bjlcfcfq; 83465 bnm
			if itemtype == "dir": # item is directory
				cur_directory.add_child(Directory(name))
			else: # item is a file; itemtype is its size
				cur_directory.add_child(File(name, int(itemtype)))

	# traverse directory
	elif line[1] == "cd":
		name = line[2]
		if name == "..": # go up a level
			cur_directory = cur_directory.parent
		else:
			cur_directory = cur_directory.get_directory(name)

root_size = root.get_size()
total_disk_size = 70000000
reqd_disk_size = 30000000
min_free_size = reqd_disk_size - total_disk_size + root_size
ans = 10**9
for size in sizes:
	if size < min_free_size:
		continue
	ans = min(ans, size)
print(ans)