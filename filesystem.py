import os

class FileSystem:

	_locations = []

	def __init__(self):
		self._locations.append('/Users/Gabor/Devel/src-jdk/')

	def findFile(self, fileNamePrefix, extension):
		for location in self._locations:
			for dirname, dirnames, filenames in os.walk(location, topdown=True):
				for filename in filenames:
					if filename.startswith(fileNamePrefix) and filename.endswith(extension):
						print self.toClassName(location, dirname, filename)
						#print os.path.join(dirname, filename)

	def toClassName(self, location, dirname, filename):
		path = os.path.join(dirname, filename)
		path = path.replace(location, '')
		path = path.replace('.java', '')
		path = path.replace('/', '.')
		return path



fs = FileSystem()
fs.findFile('Str', 'java')

	#for filename in filenames:
	#	print filename