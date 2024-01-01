# Python - Variable Annotations

- Learning Objectives

## Type annotations in Python 3
In Python 3, type annotations provide a way to specify the expected types of variables, function parameters, and return values. While Python is a dynamically typed language, type annotations allow you to add hints about the types of variables to make your code more readable and to enable static type checking tools.

Here are some common use cases for type annotations in Python 3:

1. **Variable Annotations:**
   ```python
   age: int = 25
   name: str = "John"
   ```

2. **Function Annotations:**
   ```python
   def greet(name: str) -> str:
       return "Hello, " + name
   ```

3. **Default Values and Annotations:**
   ```python
   def repeat_message(message: str, times: int = 3) -> str:
       return message * times
   ```

4. **List and Dictionary Annotations:**
   ```python
   from typing import List, Dict

   def process_numbers(numbers: List[int]) -> List[int]:
       return [n * 2 for n in numbers]

   def create_person(name: str, age: int) -> Dict[str, Union[str, int]]:
       return {'name': name, 'age': age}
   ```

5. **Annotations with `Any` Type:**
   It's possible to use `Any` if a variable can have any type:
   ```python
   from typing import Any

   def my_function(arg1: Any, arg2: Any) -> Any:
       return arg1 + arg2
   ```

6. **Type Aliases:**
   You can use `Type` aliases to simplify complex types:
   ```python
   from typing import List, Tuple

   Coordinates = Tuple[float, float]

   def move_to(coordinate: Coordinates) -> None:
       pass
   ```

7. **Combining Annotations and Docstrings:**
   ```python
   def calculate_area(length: float, width: float) -> float:
       """
       Calculate the area of a rectangle.

       Parameters:
       - length (float): The length of the rectangle.
       - width (float): The width of the rectangle.

       Returns:
       - float: The area of the rectangle.
       """
       return length * width
   ```

8. **Type Checking Tools:**
   Tools like `mypy` can be used to perform static type checking based on the annotations.

Remember, Python type annotations are not enforced at runtime and are mainly used for documentation and static analysis by tools. The actual enforcement of types depends on external tools or frameworks you may choose to use (e.g., `mypy`, `pyright`, `Pyre`, etc.).

## How you can use type annotations to specify function signatures and variable types
Type annotations in Python can be used to specify function signatures and variable types. They help communicate the expected types of inputs and outputs, and they can also be utilized by static analysis tools for type checking. Here are examples of how you can use type annotations for functions and variables:

### Function Signatures:

1. **Basic Function with Annotations:**
   ```python
   def add_numbers(x: int, y: int) -> int:
       return x + y
   ```

2. **Function with Default Values:**
   ```python
   def greet(name: str, greeting: str = "Hello") -> str:
       return greeting + ", " + name
   ```

3. **Function with a List Argument and Return Type:**
   ```python
   from typing import List

   def process_numbers(numbers: List[int]) -> List[int]:
       return [n * 2 for n in numbers]
   ```

4. **Function with Tuple Return Type:**
   ```python
   from typing import Tuple

   def divide_and_remainder(x: int, y: int) -> Tuple[int, int]:
       quotient = x // y
       remainder = x % y
       return quotient, remainder
   ```

### Variable Annotations:

1. **Basic Variable Annotations:**
   ```python
   age: int = 25
   name: str = "John"
   ```

2. **Variable with Union Type:**
   ```python
   from typing import Union

   result: Union[int, str] = 42  # result can be either int or str
   ```

3. **List Variable Annotation:**
   ```python
   numbers: List[int] = [1, 2, 3, 4]
   ```

4. **Dictionary Variable Annotation:**
   ```python
   from typing import Dict

   person: Dict[str, Union[str, int]] = {'name': 'John', 'age': 25}
   ```

### Type Aliases:

You can use type aliases to make complex types more readable:

```python
from typing import Tuple

Coordinates = Tuple[float, float]

def move_to(coordinate: Coordinates) -> None:
    pass
```

### Docstrings with Annotations:

You can also provide more detailed information about the function and its parameters in the docstring along with annotations:

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - float: The area of the rectangle.
    """
    return length * width
```

Remember that Python's type annotations are optional and not enforced at runtime. They serve as a tool for documentation and can be used by external tools for type checking. Static type checkers like `mypy` can be employed to analyze your code based on these annotations.

## Duck typing
Duck typing is a concept in programming languages, including Python, where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit inheritance or class definition. The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In duck typing, the focus is on the object's capabilities rather than its type or class hierarchy. If an object supports the required methods or properties, it can be used for a particular purpose, regardless of its actual type.

In Python, duck typing is often associated with the philosophy expressed in the Zen of Python, which includes the principle:

> "It is better to ask for forgiveness than permission."

This means that, in Python, it is often more common to try to use an object for a particular operation and catch exceptions if it doesn't support the required methods, rather than checking the object's type explicitly before performing an operation.

Here's a simple example in Python that illustrates duck typing:

```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Duck:
    def sound(self):
        return "Quack!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
duck = Duck()

print(make_sound(dog))  # Outputs: Woof!
print(make_sound(cat))  # Outputs: Meow!
print(make_sound(duck))  # Outputs: Quack!
```

In this example, the `make_sound` function does not care about the specific types of the objects (`Dog`, `Cat`, or `Duck`). It relies on the fact that each object passed to it has a `sound` method, and it calls that method without checking the type explicitly.

Duck typing allows for more flexible and dynamic code, as objects can be used based on their behavior rather than their formal type. However, it also requires careful consideration to ensure that objects passed to functions or methods indeed support the expected behavior.

## How to validate your code with mypy
`mypy` is a static type checker for Python that allows you to catch type-related errors before running your code. Here are the steps to validate your code with `mypy`:

### 1. Install `mypy`:

You can install `mypy` using pip:

```bash
pip install mypy
```

### 2. Add Type Annotations to Your Code:

Before running `mypy`, make sure your code has appropriate type annotations. Type annotations provide information about the expected types of variables, function parameters, and return values. Here's a simple example:

```python
# example.py

def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(10, 20)
print(result)
```

### 3. Run `mypy`:

Navigate to the directory containing your Python files and run `mypy` on your script:

```bash
mypy example.py
```

`mypy` will analyze your code and report any type-related errors or inconsistencies. If your code is free of type errors, `mypy` will produce no output.

### 4. Handling Imports and External Libraries:

If your code uses external libraries, you may need to install type hints for those libraries. Many popular libraries provide separate packages with type annotations. For example, if you use the `requests` library, you can install the `types-requests` package for type hints:

```bash
pip install types-requests
```

### 5. Configuration File (Optional):

You can create a `mypy.ini` configuration file to customize `mypy` behavior. It allows you to set options, ignore specific files or lines, and configure other aspects of the type checking process. Here's a simple `mypy.ini` file:

```ini
[mypy]
python_version = 3.8
warn_unused_configs = True
```

### 6. Integrating with Your IDE (Optional):

Some integrated development environments (IDEs) offer built-in support for `mypy`. Configuring your IDE to use `mypy` can provide real-time feedback as you write code. Popular IDEs like VSCode, PyCharm, and others have extensions or settings to enable `mypy` integration.

By following these steps, you can use `mypy` to validate your code and catch potential type-related errors early in the development process. Incorporating static type checking with `mypy` can lead to more robust and maintainable Python code.
