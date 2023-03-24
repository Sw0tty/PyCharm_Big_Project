class MyClass:
    def my_file(self):
        return 155


mc2 = MyClass()
print("It's for test too", mc2.my_file())

if __name__ == "__main__":
    mc = MyClass()
    print("It's only for test", mc.my_file())
