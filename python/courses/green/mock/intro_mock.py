from unittest.mock import MagicMock
from mock import DEFAULT

m = MagicMock()

def f(x,y):
    return 5

m.side_effect = f
print(m(1,2))
print(m.called)
print(m.call_count)
