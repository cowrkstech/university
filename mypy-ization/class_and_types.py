class A:
    def f(self) -> int:
        return 2


class B(A):
    ...


class C:
    def k(self) -> int:
        return 3

obj1: A = A()  # success
obj2: B = A()  # raise error
obj3: C = C()  # Success
val = obj3.f()  # raise error by mypy (not run time, yaaaay)
