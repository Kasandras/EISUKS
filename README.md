#### How to run tests:
    pytest test_mod.py   # run tests in module
    pytest somepath      # run all tests below somepath
    pytest -k stringexpr # only run tests with names that match the
                          # "string expression", e.g. "MyClass and not method"
                          # will select TestMyClass.test_something
                          # but not TestMyClass.test_method_simple
    pytest test_mod.py::test_func  # only run tests that match the "node ID",
                                    # e.g. "test_mod.py::test_func" will select
                                    # only test_func in test_mod.py
    pytest test_mod.py::TestClass::test_method  # run a single method in
                                                 # a single class

   
More detailed info at official documentation: https://docs.pytest.org/en/latest/usage.html
    
#### Requirements:
     pytest
     selenium

![okfuckit](https://media.giphy.com/media/wZCXWRgkF1UYg/200.gif)
