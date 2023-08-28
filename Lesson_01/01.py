class A:
    def foo(self):
        print("Foo from A")


class B(A):
    def foo(self):
        super().foo()


class C(A):
    def foo(self):
        print("Foo from C")


class D(B, C):
    def foo(self):
        super(A, self).foo()


instance = D()
print(D.__mro__)
instance.foo
