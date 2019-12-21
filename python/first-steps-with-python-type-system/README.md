
# First Steps with Python Type System

  * Base on Pawetł Święcki's [First Steps with Python Type System](https://blog.daftcode.pl/first-steps-with-python-type-system-30e4296722af)
  * This post is based on [PEP 483: The Theory of Type Hints, PEP 484: Type Hints](https://www.python.org/dev/peps/pep-0483)
  * Python 3.6 and mypy 0.620

---

## 1. Type vs. Class

  * A type is a **type checker** concept
  * A class is a **runtime** concept
  * Type checker is similar to flake8, but way smarter
  * Official type checker: [mypy](https://mypy.readthedocs.io/en/latest/)
  * Other type checkers: Facebook's [pyre-check](https://github.com/facebook/pyre-check) and Google [pytype](https://github.com/google/pytype)

---

### 1.1. How to define a type?

Type definition provides information for type checker. There are three ways:

  * Define a `class`
    * Example: `class Animal: ...`, `int`
  * Specify type for a variable based on its functionality
    * It is called structural subtyping, in the spirit of duck typing
    * Example: `Sized` type for an object has `__len__` method
  * Compoase complex types from basic types
    * Example: a list of integers or strings

---

## 2. Type annotation syntax

### 2.1. Annotating variables

  * Declaring variable: `name: Type`
  * Declaring with initialization: `name: Type = initial_value`
  * Without initialization, `NameError` will be raised when using it.
  * When initializing, `mypy` will check if `initial_value` fit `Type` type
  * Example
```python
width: int
width = 15  # no mypy error
height: int
height = '25'  # error:
# Incompatible types in assignment
# (expression has type "str", variable has type "int")
depth: int = 15.5  # error:
# Incompatible types in assignment
# (expression has type "float", variable has type "int")
```

---

### 2.2. Annotating functions

  * We can annotate the type of a function by annotating its **parameters** and **return type**:

```python
def function(param1: Type1, param2: Type2) -> ReturnType:
    ...
```

  * Example

```python
def add_ints(x: int, y: int) -> int:
    return x + y  # no mypy error
add_ints(1, 2)  # no mypy error
# error:
# Argument 2 to "add_ints" has incompatible type "float"; expected "int"
add_ints(1, 2.0)  
def broken_add(x: int, y: int) -> str:
    return x + y  # error:
    # Incompatible return value type (got "int", expected "str")
```

  * In `broken_add`, `mypy` finds out that `x + y` doesn't return a `str`

---

## 3. Subtyping

Subtyping is about class inheritance, like:

```python
class Animal:
	...
class Dog(Animal):
	...
```

  * Basically, a subtype is a less general type, e.g. `Dog` is a subtype of `Animal`.
  * The definition of subtype will determine `assignment rules` and usage of `attributes rules` that `mypy` enforces on the code.

---

### 3.1. Definition

  * `B <: A` means `B` is a subtype of `A`
  * `B <: A` if and only if:
    * every value of type `B` is also in the set of values of type `A`
	* every function of type `A` is also in the set of functions of type `B`
  * A function of type `A` means either
    * a standalone function accepting type `A` as parameter, or
	* a method defined on class `A`
  * So a subtype have smaller value set, but have a larger function set.
  * For `Dog <: Animal`,
    * There are **fewer** `Dog`s than `Animal`s
	* A `Dog` can do **more** than an `Animal`

---

### 3.2. Assignment rules

The definition of subtyping determines which assignment is acceptable and which isn't.

  * `scooby` is guarantted to be an `Animal`

```python
# Dog <: Animal
scooby: Dog
an_animal: Animal
an_animal = scooby # no mypy error
```

  * Assigning `an_animal` to `scooby` is not type-safe, because `an_animal` might not be a `Dog`

```python
# Dog <: Animal
scooby: Dog
an_animal: Animal
scooby = Animal # mypy error
# Incompatible types in assignment (expression has type "Animal", variable has type "Dog")
```

  * Checking inheritance relationships is part of the **nominal subtyping** approach

---

### 3.3. Attribute rules

  * `mypy` keeps an eye not only on assignments but also on attribute usage.
  * More precisely, it checks if an attribute is actualy defined on an object.

```python
class Animal:
	def eat(self): ...
class Dog:
	def bark(self): ...
```

  * Now, a `Dog` can both `bark` and `eat`, but an `Animal` can only `eat`
  * Checking attribute, especially methods, is a part of **structural subtyping** approach.

---

## 4. Defining complex types

  * 4.1. List
  * 4.2. Tuple
  * 4.3. NamedTuple
  * 4.4. Dict
  * 4.5. Union
  * 4.6. `None` type and `Optional` type

---

### 4.1. List

  * One of the most basic complex type is `List`
  * Sytax: `List[TypeOfElement]`
  * Example: `List[int]`, `List[str]`

```python
from typing import List
 
my_list: List[int] = [1, 2, 3]  # no mypy error
 
my_other_list: List[int] = [1, 2, '3']  #  error:
# List item 2 has incompatible type "str"; expected "int"
 
class Animal: pass
class Dog(Animal): pass
 
scooby = Dog()
lassie = Dog()
pinky = Animal()
 
my_dogs: List[Dog] = [scooby, lassie, pinky]  # error:
# List item 2 has incompatible type "Animal"; expected "Dog"
```

  * All elements should have the same type
  * A valid `list` `[1, 2, '3']` in python should be expressed in other ways

---

### 4.2. Tuple

  * In python, `tuple` is used to be an `immutable list` or a `record` or `row of values`.
  * `Tuple` type supports both
  * Syntax: `Tuple[Type1, Type2, Type3]`, `Tuple[TypeOfAllElements, ...]`
    * `...` is the ellipsis object
	* `Tuple[T, ...]` is used for immutable list with all the elements have the same type.

```python
from typing import Tuple
 
bob: Tuple[str, str, int] = ('Bob', 'Smith', 25)  # no mypy error
 
frank: Tuple[str, str, int] = ('Frank', 'Brown', 43.4)  # error:
# Incompatible types in assignment (expression has type "Tuple[str, str, float]",
#   variable has type "Tuple[str, str, int]")
 
ann: Tuple[str, str, int] = ('Ann', 'X', 1, 2)  # error:
# Incompatible types in assignment (expression has type "Tuple[str, str, int, int]",
#   variable has type "Tuple[str, str, int]")
 
scores1: Tuple[int, ...] = (5, 8, 4, -1)  # no mypy error
 
scores2: Tuple[int, ...] = (5, 8, 4, -1, None, 7)  # error:
# Incompatible types in assignment (expression has type
#   "Tuple[int, int, int, int, None, int]", variable has type "Tuple[int, ...]")
```

---

### 4.3. NamedTuple

  * In python, there is a handy `namedtuple`, which supports field-name look-up and has a nice string representation.

```python
rom collections import namedtuple
Person = namedtuple('Person', 'first_name last_name age')
bob = Person(first_name='Bob', last_name='Smith', age=41)
print(bob.age, bob) # 41 Person(first_name='Bob', last_name='Smith', age=41)
print(bob[0]        # 'Bob'
print(bob[1:])      # ('Smith', 41)
print(list(bob)     # ['Bob', 'Smith', 41]
```

  * `NamedTuple` is an typed alternative to `namedtuple`

```python
from typing import NamedTuple
class Person(NamedTuple):
    first_name: str
    last_name: str
    age: int
Person('Bob', 'Smith', 41)  # no mypy error
Person('Kate', 'Smith', '32')  # error:
# Argument 3 to "Person" has incompatible type "str"; expected "int"
```

  * In python 3.7, there is a `dataclass`, which is kind of `NamedTuple` on steroids

---

### 4.4. Dict

  * Syntax: `Dict[KeyType, ValueType]`
  * Example: `Dict[int, str]`

```python
from typing import Dict
 
id_to_name: Dict[int, str] = {1: 'Bob', 23: 'Ann', 7: 'Kate'}  # no error
id_to_age: Dict[int, int] = {'1': 41, 2: 22}  # error:
# Dict entry 0 has incompatible type "str": "int"; expected "int": "int"
 
name_to_phone_no: Dict[str, str] = {'Bob': '55534534', 'Ann': 55599412}  # error:
# Dict entry 1 has incompatible type "str": "int"; expected "str": "str"
```

  * For other python collections, there are also types: `Set`, `FrozenSet`, `DefaultDict`, `Counter`, `Deque`
  * Full list refers to [Python Typing](https://docs.python.org/3/library/typing.html)
  * Now we focus on another way to create complex types: `Union`

---

### 4.5. Union

  * `Union` is similar to `union` in `C/C++`
  * Syntax: `Union[Type1, Type2, Type3, Type4]`
  * Example

```python
from typing import Union
width1: Union[int, float] = 20  # no error
width2: Union[int, float] = 20.5  # no error
width3: Union[int, float] = '44'  # error:
# Incompatible types in assignment (expression has type "str",
#   variable has type "Union[int, float]")
class Animal:
    def eat(self): pass
class Dog(Animal): pass
class Cat(Animal): pass
class Lizard(Animal): pass
# only Cats and Dogs are allowed to eat :(
def restricted_eat(animal: Union[Dog, Cat]) -> None:
    animal.eat()
a_dog: Dog
restricted_eat(a_dog)  # no mypy error
a_cat: Cat
restricted_eat(a_cat)  # no mypy error
a_lizard: Lizard
restricted_eat(a_lizard)  #  error:
# Argument 1 to "restricted_eat" has incompatible type "Lizard";
#   expected "Union[Dog, Cat]"
```

---

### 4.6. `None` type and `Optional` type

  * `None` is used for missing value. 
  * `None` has the type `NoneType`, with the alias `None` itself.
  * The alias `None` is useful to express `type-T-or-no-value` semantics: `Union[T, None]`
    * `int-or-no-value`: `Union[int, None]`
  * `type-T-or-no-value` is so common that it also has an alias: `Optional[T]`
    * `int-or-no-value`: `Optional[int]`
  * Forgeting optionality of variables quite often cause bugs, when `mypy` really helps.

