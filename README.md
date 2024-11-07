> **COMP-801 Integrated Computing Practicum**
# Homework 3

## Due Dates
- Assigned Week 11
- Due:
  - **h3start**: Due by Wednesday midnight before Week 12 class
    - Uplodad to Canvas the PDF of the DESIGN.md
    - Push to the remote the changes made to the local repo.
  - **h3final**: Due by Friday midnight, Week 12
    - Push the remote all the changes made to the local repo. 

## Requirements
- Analyze the data in the *LanguageAdmired* column to find out the popularity of the programming langauges used by the developers who participated in the Stack Overflow 2024 survey. 
- Decompose the analysis into the following subproblems:
  - Collect all lanaguages and their frequency of use into a dictionary. 
  - Reverse the language frequency dictionary such that the frequencies are keys and the corresponding values are list of languages
  - Write to a CSV file the content of the reversed langauge frequency histogram such that each line has:
    - frequency value, followed by
    - double quoted string that has the lanaguages separated by ; (semicolon)
- Write testing functions for each of the subproblems above using relevant content in the devops10.csv file. 
- Design three methods, one for each of the subproblems described above. 
- Implement and test the methods.

----
**h3start**

## Getting Started
1. Clone the remote repo into your **comp801/homework** direcotry (see instructions in preivous assignemnts)
2. Open **h3** folder in VS Code
  - Install Rainbow CSV to view the content of the CSV files in a more structured way in VS Code.
  - Examine the data carefully. 
  - Learn about Rainbow CSV's RBSQ query language (similar to SQL-lite) to investigate CSV data.
3. In your **comp801** folder, create **h3data** subfolder and copy ALL the CSV file from **h3** folder into **h3data** folder
  - Open Excel and import the CSV devops10.csv file.
  - Use Excel Data tool of filtering to examine the content of the file. 3. Read the code in `analysis.py` and `client.py`. 
  - Learn about the `csv` module ans its methods from https://docs.python.org/3/library/csv.html 
  - Run `client.py`
4. Create 3 testing modules, named as follows, each with a single testing function (with the same name):
  - `test_lang_histogram.py`
  - `test_freq_of_lang.py`
  - `test_write_lang_popularity.py`
5. Create the `DESIGN.md` file
6. Check errors reported in the VS Code **Problems** tab
  - Fix formatting errors with the Black Formatter tools and manually, if needed. 

## Evaluation h3start (60 pts)

### Documentation, 6 pts and 1 commit

- All or nothing
- The project `DESIGN.md` and 5 modules:
  - `client.py`, `analysis.py`
  - 3 testing modules corresponding to the 3 methods you'll test, design, and implement.
- Enter your name as the developer of the program in EACH of the 6 files.
- Write complete docstrings for each module.
- Version control documentation (1 commit)

### Testing functions implementation, 15 pts and 3 commits

- 3 testing functions
  - 5 pts for correctly implementing each testing function
  - 3 commits, at minimum, 1 commit per testing function

### Code analysis and styling, 7 pts

- All or nothing
- Fix all reported **Problems** of the testing modules
  - Use Black Formatter
  - Make manual changes to fix remaining errors.

### DESIGN.md, 18 pts and 3 commits

- 3 designs, 6 pts each
- All method designs MUST use the accumulation pattern
- Version control: 3 commits, at minimum 1 commit per design

### Incremental development h3start, 14 pts
Minimum 7 commits, 2 pts per commit

## Guidelines h3start

1. **Document** ALL modules 
2. **Understand** each subproblem
3. Write **testing functions**
  - Run the functions
    - `assert` statements should fail, but all syntax errors are fixed.
  - **Code analysis and styling**: fix all styling errors.
4. **Design** each method and DO NOT attempt any coding. 

## Collaboration

- With the CAs or course instructors ONLY
- No collaboration with peers or other people is allowed, EXCEPT for the CAs and course instructors
- No other sources of content (internet, GPT tools, etc.) are allowed.
- You are NOT allowed to give your work on this assignment to somebody else, or to do it for someone else


## Submission h3start

- The commit history of the development process for **h3start** is pushed to GitHub
- The PDF of `DESIGN.md` is uploaded to the submission link in Canvas.


----
**h3final (40 pts)**

## Requirements

- Continue the work on h3 repository by implementing, testing, and debugging the `Analysis` methods
- Apply version control
- Resolve all the **Problems** reported in VS Code by running the code analysis tools.

## Evaluation h3final

### Implementation, 21 pts and 3 commits

- 3 methods, 7 pts each
- Write the method docstrings:
  - descriptive sentence
  - parameters (if other than `self`)
  - return value
- Follow the design and write the code

### Incremental development**, 9 pts

- 3 methods, 3 commits, 3 pts each

### Code analysis and styling, 10 pts
 
- All or nothing requirement
- Fix all code analysis and errors using Black Formatter and manually, when needed.

## Guidelines h3final

1. **Write code** incrementally, one method at a time. 
2. Run the tests, debug and fix errors as you go.
3. **Code analysis and styline**: fix all errors. 

## Collaboration 

- With the CAs or course instructor only
- No collaboration with peers or other people is allowed, EXCEPT for the CAs and course instructors
- No other sources of content (internet, GPT tools, etc.) are allowed.
- You are NOT allowed to give your work on this assignment to somebody else, or to do it for someone else 

## Submission h3final

- The commit history of the development process for **h3final** is pushed to GitHub
- The PDF of `DESIGN.md` is uploaded to the submission link in Canvas.





