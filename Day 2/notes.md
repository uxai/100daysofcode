# Data types

## Typecasting

Convert an integer to a string
```
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
```

Use `type()` to find out what type your variable is

## Rounding
Rounding can be used by `round()`, second parameter lets you choose the precision, for example `round(2.664532, 2)` will round and print to two decimal places.

Floor will be to round down to an integer, by method of `8 // 3` for example, will output an integer of 2.

## f-String

Instead of typecasting everything we can do:

```
score = 0
height = 1.8
print(f"your score is {score} and your height is {height} meters.")
```
This will convert everything as necessary in the background; reducing lots of manual labor and keeping legibility.

### Formatting
To format, a decimal to show two decimals even if it is `5.00`, we need to format. The snippet `total = "{:.2f}".format(total)` will take the value of `total` and convert it to a string that has two decimal places.