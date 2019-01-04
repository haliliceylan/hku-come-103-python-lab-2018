# LAB 11 Answers
## Attention !
**These are my answers, they may be false.**
# TRUE / FALSE QUESTIONS
- **T** | You can have more than one except clause in a try/except statement.
- **T** | The ZeroDivisionError exception is raised when the program attempts to perform the calculation x/y if y = 0.
- **T** | An exception handler is a piece of code that is written using the try/except statement.
- **F** | The else suite in a try/except statement executes only if a statement in the try suite raises an exception.
- **F** | The finally suite in a try/except statement executes only if no exceptions are raised by statements in the try suite.
- **F** | Lists in Python are immutable.
- **F** | The index of the first element in a list is 1, the index of the second element is 2, and so forth.
- **T** | The index -1** **identifies the last element in a list.
- **T** | In slicing, if the end index specifies a position beyond the end of the list, Python will use the
length of the list instead.

# COMPLETION QUESTIONS
## Fill in the blanks.
- A(n) **try/except** block includes one or more statements that can potentially raise an exception.
- The built-in function **len** returns the length of a sequence.
- A(n) **slice** is a span of items that are taken from a sequence.
- Lists are **mutable**, which means their elements can be changed in a program.
- The **Value Error** exception is raised when a search item is not in the list being searched.

# ALGORITHM WORKBENCH QUESTIONS

**a.** What will the following code display?
```
try:
    x = float('abc123')
    print('The conversion is complete.')
except IOError:
    print('This code caused an IOError.')
except ValueError:
    print('This code caused a ValueError.')
print('The end.')
```
**Answer**
```
This code caused a ValueError.
The end.
```
**b.** Assume the names variable references a list of strings. Write code that
determines whether 'Ruby' is in the names list. If it is, display the message 'Hello Ruby'. Otherwise, display the message 'No Ruby'.

**Answer**
```
names = ["Halil","Isabella","Emma","Hannah","Ruby"]
if "Ruby" in names:
    print("Hello Ruby")
else:
    print("No Ruby")
```
**c.** Assume the numbers variable references a list of strings. Write code that
determines that determines the average of the numbers and displays the result
with two digits after decimal point.
```
numbers = ["19","20","18","13","98"]
total = 0
for x in numbers:
    x = int(x)
    total += x
avg = total/len(numbers)
print("Average is",format(avg,".2f"))
```
**d.** What will the following code display?
```
try:
    x = float(abc123)
    print(x)
    except ValueError:
    print('This code caused a ValueError.')
except TypeError:
    print('This code caused a TypeError.')
except NameError:
    print('This code caused a NameError.')
print('The end.')
```
**Answer**
```
    except ValueError:
         ^
SyntaxError: invalid syntax
```
# MULTIPLE CHOICE QUESTIONS
## You can look at the questions on pdf
3. B
4. B
5. B
6. D
7. D
8. D
9. B