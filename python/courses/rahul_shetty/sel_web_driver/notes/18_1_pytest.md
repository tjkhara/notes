# Section 18 - PyTest

**Test case name is method name**

Running from pycharm seen in video.

    py.test

Will find all the py tests in the directory.

To see more info:

    py.test -v

Showing console logs

    py.test -v -s

The pycharm test running runs this command the last one.

Every method is treated as a test case.

## Running selected files

Format

    py.test test_demo2 {filename} -v -s

    py.test test_demo2.py -v -s

## Running selected test cases from multiple files

You can use regular expressions for the method names

Run tests with credit card present in the test name:

    py.test -k CreditCard -v -s

The text after the -k option will be found in different test cases.

## Grouping test cases

Marking test cases with one set of name and tell terminal to run marked test cases

    py.test -m smoke -v -s

This is how you mark tests:

    import pytest

    @pytest.mark.smoke
    def test_first_program():
        msg = "Hello"
        assert msg == "Hello", "Test failed no match"

    def test_second_CreditCard():
        a = 4
        b = 6
        assert a+2 == 6, "Addition does not match"

## Skipping test cases

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_first_program():
        msg = "Hello"
        assert msg == "Hello", "Test failed no match"

    py.test -v -s

### What is you want to perform one operation and now show the failing test case
### Skip reporting but run operation

    @pytest.mark.xfail
    def test_first_program():
        msg = "Hello" # operation
        assert msg == "Hello", "Test failed no match"

    py.test -v -s

Test will run but output will not be shown.

# Fixtures and their importance

Setup and tear down methods

# Data driven fixtures



