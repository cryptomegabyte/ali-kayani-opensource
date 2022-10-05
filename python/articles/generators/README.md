# Generators

In computer science generators are used to control iteration behaviour of a loop. All generators are also iterators. Generators remember their internal state. Generators return interators.

That might be a bit of a mouthful, as always let's look at a practical example to aid our understanding.

# App

We're going to create an application that calculates the `fibonacci` sequence. If you don't know what the fibonacci sequence is, please use a search engine to look it up.

## Algorithm

- Define a function which takes in a number.
- Define two start values a,b. `a=0` `b=1`.
- Define an empty array called result.
- The number given to the function will be used to generate a sequence of integers.
- Iterate through that sequence. Within each iteration:
    - Add a to the result array
    - Change the value of a `a = b`.
    - Change the value of b `b = a + b`

## Folder structure

```bash
app/
|--tests/
|----__init__.py
|----test_fibonacci.py
|--src/
|--__init__.py
|--fibonacci.py
|--requirements.txt
```

