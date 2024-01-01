# Python - Async

## async and await syntax
In Python, `async` and `await` are used to define and work with asynchronous code using the `asyncio` library. Asynchronous programming is a way to write non-blocking code, allowing multiple tasks to be executed concurrently. Here's a brief explanation of the syntax:

1. **`async` Function:**
   - Use the `async` keyword to define an asynchronous function. An asynchronous function can contain `await` expressions, and it is typically used with the `asyncio` module.

    ```python
    import asyncio

    async def async_function():
        print("Doing some asynchronous task")

    asyncio.run(async_function())
    ```

2. **`await` Expression:**
   - Inside an asynchronous function, you can use the `await` keyword before an asynchronous function call or a coroutine to pause execution until the awaited task is complete.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")

    asyncio.run(async_task())
    ```

3. **`async with` and `async for`:**
   - You can use `async with` for asynchronous context managers and `async for` for asynchronous iteration.

    ```python
    import asyncio

    async def async_with_example():
        async with some_async_context_manager() as result:
            print(result)

    async def async_for_example():
        async for item in some_async_iterable():
            print(item)
    ```

4. **Running Async Code:**
   - To run asynchronous code, use the `asyncio.run()` function. It was introduced in Python 3.7.

    ```python
    import asyncio

    async def main():
        # Your asynchronous code here

    asyncio.run(main())
    ```

Remember that using `async` and `await` is most beneficial when dealing with I/O-bound operations, like making web requests or working with databases, where waiting for a response should not block the entire program.

## How to execute an async program with asyncio
Executing an asynchronous program with `asyncio` involves creating an event loop, defining asynchronous functions (coroutines), and then running the event loop. Here's a step-by-step guide:

1. **Define Your Asynchronous Functions (Coroutines):**
   - Create one or more asynchronous functions using the `async def` syntax. These functions can contain `await` expressions.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")
    ```

2. **Create an Event Loop:**
   - An event loop is an essential part of asynchronous programming. It manages the execution of asynchronous tasks. You can create an event loop using `asyncio.get_event_loop()`.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")

    loop = asyncio.get_event_loop()
    ```

3. **Run Your Asynchronous Function(s) in the Event Loop:**
   - Use the `loop.run_until_complete()` method to run your asynchronous function(s) within the event loop.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_task())
    ```

4. **Complete the Loop and Close Resources:**
   - After running the asynchronous task(s), you should close the event loop to release resources.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_task())
    loop.close()
    ```

5. **Using `asyncio.run()` (Python 3.7 and later):**
   - For simpler usage, you can use the `asyncio.run()` function, which was introduced in Python 3.7. It creates a new event loop, runs the provided coroutine, and then closes the loop.

    ```python
    import asyncio

    async def async_task():
        print("Start")
        await asyncio.sleep(2)  # Asynchronously sleep for 2 seconds
        print("End")

    asyncio.run(async_task())
    ```

Keep in mind that this is a basic example. In real-world scenarios, you may have multiple asynchronous tasks running concurrently, and you would use features like `asyncio.gather()` to wait for multiple tasks to complete simultaneously.

## How to run concurrent coroutines
To run concurrent coroutines in Python, you can use `asyncio.gather()` or `asyncio.create_task()` to execute multiple coroutines concurrently within the same event loop. Here's an example using both approaches:

```python
import asyncio

async def coroutine_1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)
    print("Coroutine 1 completed")

async def coroutine_2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)
    print("Coroutine 2 completed")

async def main():
    # Using asyncio.gather() to run coroutines concurrently
    await asyncio.gather(coroutine_1(), coroutine_2())

    # Using asyncio.create_task() to run coroutines concurrently
    task1 = asyncio.create_task(coroutine_1())
    task2 = asyncio.create_task(coroutine_2())

    # You can do other work here while coroutines are running concurrently

    # Wait for both tasks to complete
    await task1
    await task2

# Run the main function
asyncio.run(main())
```

In this example:

1. `asyncio.gather(coroutine_1(), coroutine_2())`: This function gathers multiple coroutines and runs them concurrently. It returns a single coroutine that completes when all the coroutines passed to `gather()` have completed.

2. `asyncio.create_task(coroutine)`: This function creates a Task object for the given coroutine and schedules it to run in the background. It returns the Task object. You can create multiple tasks and let them run concurrently.

3. You can await the result of `asyncio.gather()` or each individual task using `await`.

Remember, using these methods is beneficial when coroutines are independent or can run concurrently without waiting for each other. If one coroutine needs the result of another, you might want to await them sequentially.

## How to create asyncio tasks
In Python's `asyncio` module, you can create tasks using the `asyncio.create_task()` function. Tasks allow you to run coroutines concurrently and manage their execution. Here's an example:

```python
import asyncio

async def coroutine_1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)
    print("Coroutine 1 completed")

async def coroutine_2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)
    print("Coroutine 2 completed")

async def main():
    # Create tasks using asyncio.create_task()
    task1 = asyncio.create_task(coroutine_1())
    task2 = asyncio.create_task(coroutine_2())

    # You can do other work here while tasks are running concurrently

    # Wait for both tasks to complete
    await task1
    await task2

# Run the main function
asyncio.run(main())
```

In this example:

1. `asyncio.create_task(coroutine_1())`: This function creates a Task object for `coroutine_1` and schedules it to run in the background.

2. `asyncio.create_task(coroutine_2())`: Similarly, this function creates a Task object for `coroutine_2`.

3. The created tasks (`task1` and `task2`) can be awaited to ensure that the main coroutine (`main()`) waits for their completion.

By using tasks, you can run multiple coroutines concurrently and potentially achieve better performance when dealing with independent asynchronous operations. Keep in mind that tasks are particularly useful when you have many coroutines to manage concurrently.

## How to use the random module
The `random` module in Python provides functions for generating random numbers. Here are some common use cases and examples of how to use the `random` module:

### 1. Generating Random Float:
```python
import random

random_float = random.random()  # Random float between 0 and 1
print(random_float)
```

### 2. Generating Random Integer within a Range:
```python
import random

random_integer = random.randint(1, 10)  # Random integer between 1 and 10 (inclusive)
print(random_integer)
```

### 3. Shuffling a List:
```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # Shuffles the elements of the list in-place
print(my_list)
```

### 4. Choosing a Random Element from a Sequence:
```python
import random

my_sequence = ["apple", "banana", "orange", "grape"]
random_element = random.choice(my_sequence)
print(random_element)
```

### 5. Generating Random Float within a Range:
```python
import random

random_float_range = random.uniform(2.5, 5.5)  # Random float between 2.5 and 5.5
print(random_float_range)
```

### 6. Randomly Sampling Elements from a Sequence:
```python
import random

my_sequence = ["red", "green", "blue", "yellow", "orange"]
random_sample = random.sample(my_sequence, 3)  # Randomly select 3 elements from the list
print(random_sample)
```

### 7. Setting a Random Seed (for reproducibility):
```python
import random

random.seed(42)  # Setting a seed for reproducibility
random_number_1 = random.random()
random_number_2 = random.random()

print(random_number_1, random_number_2)
```

By setting a seed using `random.seed()`, you ensure that the sequence of random numbers generated will be the same every time the program is run, which is useful for reproducibility in certain scenarios, such as debugging or testing.
