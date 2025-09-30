import mymodules
import test_mymodule_fibo

mymodules.testdef()

print(test_mymodule_fibo.fib(1000))
print("dir(test_module_fibo -> )", dir(test_mymodule_fibo))
print(test_mymodule_fibo.__name__)
print(__name__) # like this.name or self.name 