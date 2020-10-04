# -*- coding:utf-8 -*-
class A:
    class_attr = "test attr"
    
    def __init__(self):
        pass
        
    @classmethod
    def class_foo(cls):
        print("running class_foo(%s)" % (cls.class_attr))

    def class_bar(self):
        print("running class_bar(%s)" % (self.class_attr))


if __name__ == '__main__':
	A.class_foo()
	A.class_attr = 'update'
	A.class_foo()

	print('~~~~~~~')
	a = A()
	a.class_foo()
	a.class_attr = 'update by instance'
	a.class_foo() # updated instance's class_attr does not change Class A's class_attr

	print('~~~~~~~')



