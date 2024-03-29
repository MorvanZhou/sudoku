# A Sudoku generator and solver

This is a Sudoku game written in python, default to use Wave Function Collapse method.

## Install

```shell
pip install sudokum
```

# Generation

A sudoku can be generated with a `mask_rate`. A full solution is generated when passing `mask_rate=0`.

```python
import sudokum

g = sudokum.generate(mask_rate=0.7)
print(g)
"""
[[1 0 0 5 0 0 0 0 3]
 [0 3 7 0 0 1 0 0 4]
 [0 0 0 0 0 2 0 0 0]
 [0 0 0 0 9 4 0 0 0]
 [0 0 4 0 0 0 0 3 2]
 [0 0 0 3 2 5 0 0 0]
 [0 0 0 0 0 0 2 0 0]
 [7 4 0 0 0 0 0 0 0]
 [8 0 0 0 0 3 1 0 0]]
"""
```

To visualize the generating procedure, I have made a GUI for animating Wave Function Collapse in sudoku generation.

```python
import sudokum

sudokum.display_wfc()
```

![auto](https://github.com/MorvanZhou/sudoku/raw/main/demo/sudoku_auto.gif)

Or you can get you hand on it by running following code.

```python
import sudokum

sudokum.display_wfc(human=True)
```

![human](https://github.com/MorvanZhou/sudoku/raw/main/demo/sudoku_human.gif)

# Solving

By using `sudokum.solve()` function, it tries to solve the puzzle.

```python
import sudokum

g = sudokum.generate(mask_rate=0.7)
s = sudokum.solve(g)
print(s)
"""
[[1 2 8 5 4 7 6 9 3]
 [6 3 7 9 8 1 5 2 4]
 [4 9 5 6 3 2 7 1 8]
 [2 1 3 7 9 4 8 5 6]
 [5 7 4 1 6 8 9 3 2]
 [9 8 6 3 2 5 4 7 1]
 [3 5 1 4 7 6 2 8 9]
 [7 4 2 8 1 9 3 6 5]
 [8 6 9 2 5 3 1 4 7]]
"""
```

A solving max try number (default to 10) can set as following:

```python
import sudokum

s = sudokum.solve(g, max_try=3)
```

## Manually check solution

If you have your own solution, you can validate it by following function:

```python
import sudokum

ok, position_of_problems = sudokum.check(g)
```

# More Example

More use cases can be found in my [test files](https://github.com/MorvanZhou/sudoku/tree/main/tests).
