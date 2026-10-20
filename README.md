# Lab 6 - List Practice

Follow these steps exactly, printing only when a step says to print.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Create an empty list.
3. Using a `while` loop, ask for items one at a time with the prompt `Input Item: ` and add each one to the list.
4. Stop the loop when `!` is entered. Do not add the `!` to the list.
5. Print the list.
6. Sort the list, then print it.
7. Print the 3rd item of the sorted list.
8. Print the 3rd last item of the sorted list.
9. Print a slice of the 4th through 6th items (use a slice, which prints as a list).
10. Remove the last item from the list, then print the list.
11. Ask `Remove item: `. If that item is in the list, remove it and print the list. If it is not in the list, print nothing.

Keep every item as a string (do not convert to numbers). Assume at least 6 items
are entered.

For example, the items `x`, `a`, `m`, `c`, `q`, `b`, `!`, then `c` for the
item to remove, print:

```
['x', 'a', 'm', 'c', 'q', 'b']
['a', 'b', 'c', 'm', 'q', 'x']
c
m
['m', 'q', 'x']
['a', 'b', 'c', 'm', 'q']
['a', 'b', 'm', 'q']
```

The prompts land on the same line as the next output, because the typed answers
do not appear in the test output.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Seven fruits, remove kiwi
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go. Number them to match the steps if that helps.
- Tests check your output exactly. Print the lists with `print(my_list)`, not item by item.
- Remember that the first item is index 0.

## Optional challenges

Finished early? Try the optional challenges in the `challenges` folder. Open `challenges/CHALLENGES.md` for instructions. They are not assessed and do not affect your lab result.
