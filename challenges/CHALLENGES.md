# Optional Challenges - Lab 6

**These challenges are optional.** Try them once Lab 6 passes every test. They are
not assessed, and they do not affect your lab result.

Each challenge has its own file. Write your program below the header.

| File | Challenge |
|---|---|
| `task_scheduler.py` | Challenge 1 - Task Scheduler |
| `discount_calculator.py` | Challenge 2 - Discount Calculator |

## Challenge 1: Task Scheduler

1. Create an empty list.
2. In a loop, ask for a task with the prompt `Task: ` and add it to the list.
   Stop when the user enters `done` (do not add `done`).
3. Add `"Complete project"` to the end of the list.
4. Insert `"Check email"` at the beginning of the list.
5. Remove `"Take break"` from the list.
6. Count how many times `"Review code"` appears and store it in a variable.
7. Sort the list alphabetically.
8. Print the list.
9. Print `Review code count: ` followed by the count.

You can assume the user always enters `Take break` as one of the tasks.

For example, entering `Write report`, `Review code`, `Take break`, `Review code`,
`Test feature`, `done` prints:

```
['Check email', 'Complete project', 'Review code', 'Review code', 'Test feature', 'Write report']
Review code count: 2
```

## Challenge 2: Discount Calculator

1. Create an empty list.
2. In a loop, ask for a price with the prompt `Price: `, convert it with
   `float()`, and add it to the list. Stop when the user enters `done`.
3. Ask for the discount with the prompt `Discount %: ` and convert it with
   `float()`.
4. Use a `for` loop over each index position in the list.
5. For the price at index `i`, the discount is the price times
   `discount_percent / 100`. Subtract the discount from the price and store the
   result back at index `i`.
6. After the loop, print the list.

For example, prices `100`, `50`, `200`, `75` with a discount of `20` prints
`[80.0, 40.0, 160.0, 60.0]`.

## Running your program

Open the challenge file and press the Run button in the top right corner of VS
Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B**, the same as for the lab. The Lab 6 results appear first.
Scroll down to the **OPTIONAL CHALLENGES** section for these.

`SKIP` means you have not started that challenge yet. It is not an error.

## Reminders

- These are optional. Finish Lab 6 first.
- Comment as you go.
- Output is matched exactly, the same as the lab. Copy the prompts exactly,
  including the space after the colon.
