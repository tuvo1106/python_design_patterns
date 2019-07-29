"""
Facade
- Provides a simple, easy to understand/user interface over a
  large and sophisticated body of code

Motivation
- Balancing complexity and presentation/usability
- Typical home
  - Many subsystems (electrical, sanitation)
  - Complex internal structure (e.g., floor layers)
  - End users is not exposed to internals
- Same with software!
  - Many systems working to provide flexibility, but...
  - API consumers want it to 'just work'
"""


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def write(self, text):
        self.buffer += text

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


# facade
class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)

if __name__ == "__main__":
    C = Console()
    C.write('hello')
