# Initial notes

Normal way to run tests

    python -m unittest discover

or

    python -m unittest discover -v

With green

    green

    green -vvv

This is for more verbose output.

Very concise is

    green -k

Can also do

    green -vvvk

## Where to put the test file

Can put it right next to the module

In every package make a test sub directory and put your test there.

## how to not see skipped

    green -vvv -k