"""
Builder
 - When piecewise object construction is complicated,
   provide an API for doing it succinctly

Motivation
- some objects are simply and can be created in a single
  initializer call
- other objects require a lot of ceremony to create
- having an object with 10 initializer arguments is not
  productive
- instead, opt for piecewise construction
- Builder provides an API for constructing an object
  step-by-step
"""

# simple scenario
text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

# more complicated
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'\t<li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)

builder = HtmlBuilder('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# chaining methods
fluent_builder = HtmlBuilder('ul')
fluent_builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print('Fluent builder:')
print(fluent_builder)

# create
created_builder = HtmlElement.create('ul')
created_builder.add_child_fluent('li', 'python')
print('Created builder:')
print(created_builder)
