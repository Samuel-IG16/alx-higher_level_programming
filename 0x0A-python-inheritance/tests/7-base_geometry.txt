=============================
The ``7-base_geometry`` module
=============================

Using ``BaseGeometry``
---------------------

Import the class:

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

Now test it:

    >>> bg = BaseGeometry()
    
    >>> bg.integer_validator("my_int", 12)

    >>> bg.integer_validator("width", 89)

    >>> bg.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

    >>> bg.integer_validator("name", "John")
    Traceback (most recent call last):
    TypeError: name must be an integer

    >>> bg.integer_validator("age", 0)
    Traceback (most recent call last):
    ValueError: age must be greater than 0
    
    >>> bg.integer_validator("distance", -4)
    Traceback (most recent call last):
    ValueError: distance must be greater than 0

    >>> bg.integer_validator("average", 7.8)
    Traceback (most recent call last):
    TypeError: average must be an integer

    >>> bg.integer_validator("average")
    Traceback (most recent call last):
    TypeError: integer_validator() missing 1 required positional argument: 'value'

    >>> bg.integer_validator()
    Traceback (most recent call last):
    TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

    >>> bg.integer_validator("NaN", float('nan'))
    Traceback (most recent call last):
    TypeError: NaN must be an integer

    >>> bg.integer_validator("Big", 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    >>> bg.integer_validator("age", (4,))
    Traceback (most recent call last):
    TypeError: age must be an integer

    >>> bg.integer_validator("age", [3])
    Traceback (most recent call last):
    TypeError: age must be an integer

    >>> bg.integer_validator("age", True)
    Traceback (most recent call last):
    TypeError: age must be an integer

    >>> bg.integer_validator("age", {3, 4})
    Traceback (most recent call last):
    TypeError: age must be an integer

    >>> bg.integer_validator("age", None)
    Traceback (most recent call last):
    TypeError: age must be an integer
