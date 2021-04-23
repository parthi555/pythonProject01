class add:
    def result(self):
        self.a = 20
        self.b = 30
        self.c = self.a + self.b
        print(self.c)

class helloworld(add):
    def result(self):

        print('hello world')

x = helloworld()
x.result()