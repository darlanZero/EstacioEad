import Excetion
class ExcecaoCustomizada(Excetion):
    pass

x = -1
if x < 0:
    raise Excetion("Valor negat6ivo!!!")

x = "Hello"
if not  type(x) is int:
    raise TypeError("Use apenas inteiros!")