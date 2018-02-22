# The Mighty 8 Ball

A mighty tool to answer all your question.

## What is an 8 Ball

```
λ py m8y_ball.py
As I see it, yes
```
So basically you get a random answer.

## Usage

### Cli

```
λ py m8y_ball.py -h
usage: m8y_ball.py [-h] [-i I] [-l] [input]

The classical magic 8-ball will now answer your questions.

positional arguments:
  input       predefined type

optional arguments:
  -h, --help  show this help message and exit
  -i I        input file (txt)
  -l, --list  list all predefined types

```

### Module

```python
import m8y_ball as ball

print(ball.answer())
```

## API

### answer()

Gives an mighty random answer.

### listt()

Lists all predefined types, equivalent to ```λ py m8y_ball.py -l```.

### answt(type)

Input ```type``` should be a type defined by ```listt()```.
Gives an answer based on a predifined type (s. ```listt()```), equivalent to ```λ py m8y_ball.py input```.

### answf(file)

Input ```file``` should be a file name or path.
Gives an answer based on a self declared answer file, equivalent to ```λ py m8y_ball.py -i I```.

### Answer files

```
λ cat answer.txt
42
l33t haxx0r
Can i haz cheesburgerz
```
```
λ py m8y_ball.py -i answer.txt
Can i haz cheesburgerz

```
An answer file is file with answers used to answer questions, it should contain one answer on one line.
These lines should be seperated by newlines (```\n```)

### Included Answers

* generic
* excuses
* financial
* inspirational
* sarcastic
