# Shape Sudoku Solver

This software solves Shape Sudokus using image recognition and a custom Python algorithm.

## What's Shape Sudoku?

Shape Sudoku is a variation of the classic logic game Sudoku. Instead of numbers, you fill the grid with different shapes according to these rules:

- A shape can't appear more than once in any row.
- A shape can't appear more than once in any column.
  
Some shapes are already placed on the grid, and one space has a question mark. Your challenge is to determine which shape should replace the question mark while following the rules.

### Example
<img width="399" alt="Shape Sudoku example" src="https://github.com/o-Ian/deductive_logical_resolver/assets/49800676/8656b313-bef9-456d-9b5e-9ca7b5e92d3c">

## Where to find shape sudokus to solve?
There's planty of youtube videos in that matter (most of them will work in our software), there's also books with shape sudokus. You just have to search for "Deductive Logical Thinking" or  "Shape Sudoku" on the web and you will find enough material.

## Requirements

The shape sudoku you want to solve must meet the following requirements:

- The possible shapes in the given sudoku are:
  
  <img width="520" alt="Screenshot 2024-07-04 at 00 27 16" src="https://github.com/o-Ian/deductive_logical_resolver/assets/49800676/eac194d2-66de-4806-81d7-a45a8720674b">
  
- A precise screenshot of the shape sudoku was taken, the screenshot shows ONLY the sudoku, with no other unwanted elements.
  
NOTE 1: If the provided sudoku has any shape other than these ones, the software won't be able to recognize it, thus not being able to solve it.

NOTE 2: The color of the shapes does not matter; they can be black and white, all the same color, or different colors than the provided in the examples.

NOTE 3: The shape sudoku does not need to have a question mark symbol as part of the grid.

## How to use it
1. Take a screenshot of the Shape Sudoku you want to solve.
2. Place the screenshot in the 'gridRecognition/entireGrids/' folder, the application will automatically get the last screenshot placed into the folder to work with.
3. Set the variable grid_size to the number of rows and columns in your Sudoku.
4. Set the variable possible_elements_default with a list of all possible shapes in your Sudoku (these shapes must be recognizable by the software, see above).
5. Run the main.py file.


## Response
The response you'll get will be something like this:

```
The grid image used was: gridRecognition/infFiles/entire_grids/img.png

['square', 'circle', 'star', 'triangle', 'plus']
['triangle', 'plus', 'circle', 'star', 'square']
['star', 'square', 'plus', 'circle', 'triangle']
['circle', 'triangle', 'square', 'plus', 'star']
['plus', 'star', 'triangle', 'square', 'circle']

The answer is: star
```
FYI: The application will convert the symbols into their corresponding text.


## Contact me

For any queries, feel free to contact me:

- [LinkedIn](https://choosealicense.com/licenses/mit/)
