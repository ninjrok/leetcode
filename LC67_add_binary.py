class Stack:
    def __init__(self, string=''):
        self.arr = [s for s in string]

    def is_empty(self):
        return (True if not self.arr else False)

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        return (None if self.is_empty() else self.arr.pop())


class Solution:
    def __init__(self):
        self.table = {
            ('0', '0', '0'): ('0', '0'),
            ('0', '0', '1'): ('1', '0'),
            ('0', '1', '0'): ('1', '0'),
            ('0', '1', '1'): ('0', '1'),
            ('1', '0', '0'): ('1', '0'),
            ('1', '0', '1'): ('0', '1'),
            ('1', '1', '0'): ('0', '1'),
            ('1', '1', '1'): ('1', '1'),
            ('0', None, '0'): ('0', '0'),
            ('0', None, '1'): ('1', '0'),
            ('1', None, '0'): ('1', '0'),
            ('1', None, '1'): ('0', '1')
        }

    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            stack_a = Stack(a)
            stack_b = Stack(b)
        else:
            stack_a = Stack(b)
            stack_b = Stack(a)

        sum_stack = Stack()
        carry_stack = Stack('0')

        while not stack_a.is_empty() or not stack_b.is_empty():
            x = stack_a.pop()
            y = stack_b.pop()
            carry_back = carry_stack.pop()
            sum_, carry_fwd = self.table[(x, y, carry_back)]
            sum_stack.push(sum_)
            carry_stack.push(carry_fwd)

        ans = ''
        while not carry_stack.is_empty():
            c = carry_stack.pop()
            if carry_stack.is_empty() and c == '0':
                continue
            else:
                ans += c

        while not sum_stack.is_empty():
            ans += sum_stack.pop()

        return ans
