# coding=utf-8

class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('必须输入数字!')
		if value<0 or value>100:
			raise ValueError('必须大于-小于100!')
		self._score = value

s = Student()
s.score = 99
print(s.score)