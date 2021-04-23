from multipledispatch import dispatch


class demo:

    @dispatch(int, int)
    def product(a,b):
        p = a * b
        print(p)

        @dispatch(int,int,int)
        def product(a,b,c):
            p = a * b * c
            print(p)



obj = demo
obj. product(4,5)
obj.product(4,5,6)