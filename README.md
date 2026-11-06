
# Mad Libs – String Concatenation in Python

## Description
A simple Python project demonstrating string concatenation and f-strings. The program collects words from the user and inserts them into a funny sentence.

## Concepts Learned
- String concatenation using `+`.
- Using `.format()` to insert variables.
- Using f-strings.
- Collecting user input using `input()`.

## String Concatenation Examples

```python
youtuber = "Kylie Yang"

print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")
```

## Program Code

```python
adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because\
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
```

## How It Works
1. The program asks the user for an adjective.
2. It asks for two verbs.
3. It asks for a famous person's name.
4. The f-string inserts the answers into the sentence.
5. The completed Mad Lib is displayed.

## How to Run
1. Save the code as `madlib.py`.
2. Open a terminal in the project folder.
3. Run `python madlib.py`.
4. Enter the requested words.

## Example Output

```text
Adjective: amazing
Verb1: code
Verb2: dance
Famous person: Messi

Computer programming is so amazing! It makes me so excited all the time because I love to code. Stay hydrated and dance like you are Messi!
```

## Key Takeaway
String concatenation joins strings together. F-strings provide an easy way to insert variables directly into strings using `{}`.
