"""
Visitor
- A component (visitor) that knows how to traverse a data structure
  composed of (possibly related) types

Motivation
- Need to define a new operation on an entire class hierarchy
  - E.g., make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in the hierarchy
- Need access to the non-common aspects of classes in the hiearchy
- Create an external component to handle rendering
  - But avoid explicit type checks
"""


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self): return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # represents 1+(2+3)
    E = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    E.print(buffer)
    print(''.join(buffer), '=', E.eval())

    # breaks OCP: requires we modify the entire hierarchy
    # what is more likely: new type or new operation?
