from collections import deque


# Function to generate binary numbers between 1 to N using
# queue data structure
def generate(n):

	# create an empty queue and push 1 to it
	q = deque()
	q.append('1')

	# run n times
	for i in range(n):
		# pop the front element
		front = str(q.popleft())

		# append 0 and 1 to the front element of the queue and
		# enqueue both Strings
		q.append(front + '0')
		q.append(front + '1')

		# print the front element
		print(front, end=' ')


if __name__ == '__main__':

	n = 16
	generate(n)
