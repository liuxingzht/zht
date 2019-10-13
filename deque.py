from collections import deque
#把队列当栈来使用
stack=deque(('Kotlin','Python'))
#元素入栈
stack.append("Erlang")
stack.append("Swift")
print('Stack中的元素:',stack)
#元素出栈，后添加的先出
print(stack.pop())
print(stack.pop())
print(stack)

#把队列当队列来使用
q=deque(('Kotlin','Python'))
#元素入队列
q.append('Erlang')
q.append('Swift')
print("q中的元素为：",q)
#元素出队列，先添加的先出
print(q.popleft())
print(q.popleft())
print(q)

#把队列当双端队列来使用
q=deque(range(5))
print('q中的元素：',q)
#执行旋转，队尾移到对头，使之首尾相连
q.rotate()
print('q中的元素：',q)
#再次执行旋转，队尾移到对头，使之首尾相连
q.rotate()
print('q中的元素：',q)
