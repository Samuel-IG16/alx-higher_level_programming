# 0x09. Python - Everything is object

## Table of contents
Files | Description
----- | -----------
[0-answer.txt](./0-answer.txt) | What function would you use to print the type of an object?
[1-answer.txt](./1-answer.txt) | How do you get the variable identifier (which is the memory address in the CPython implementation)?
[2-answer.txt](./2-answer.txt) | a = 89, b = 100. Do a and b point to the same object?
[3-answer.txt](./3-answer.txt) | a = 89, b = 89. Do a and b point to the same object?
[4-answer.txt](./4-answer.txt) | a = 89, b = a. Do a and b point to the same object?
[5-answer.txt](./5-answer.txt) | a = 89, b = a + 1. Do a and b point to the same object?
[6-answer.txt](./6-answer.txt) | s1 = "Holberton", s2 = s1, print(s1 == s2). What do these 3 lines print?
[7-answer.txt](./7-answer.txt) | s1 = "Holberton", s2 = s1, print(s1 is s2). What do these 3 lines print?
[8-answer.txt](./8-answer.txt) | s1 = "Holberton", s2 = "Holberton", print(s1 == s2). What do these 3 lines print?
[9-answer.txt](./9-answer.txt) | s1 = "Holberton", s2 = "Holberton", print(s1 is s2). What do these 3 lines print?
[10-answer.txt](./10-answer.txt) | l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 == l2). What do these 3 lines print?
[11-answer.txt](./11-answer.txt) | l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 is l2). What do these 3 lines print?
[12-answer.txt](./12-answer.txt) | l1 = [1, 2, 3], l2 = l1, print(l1 == l2). What do these 3 lines print?
[13-answer.txt](./13-answer.txt) | l1 = [1, 2, 3], l2 = l1, print(l1 is l2). What do these 3 lines print?
[14-answer.txt](./14-answer.txt) | l1 = [1, 2, 3], l2 = l1, l1.append(4), print(l2). What does this script print?
[15-answer.txt](./15-answer.txt) | l1 = [1, 2, 3], l2 = l1, l1 = l1 + [4], print(l2). What does this script print?
[16-answer.txt](./16-answer.txt) | def increment(n): n += 1; a = 1, increment(a), print(a). What does this script print?
[17-answer.txt](./17-answer.txt) | def increment(n): n.append(4); l = [1, 2, 3], increment(l), print(l). What does this script print?
[18-answer.txt](./18-answer.txt) | def assign_value(n, v): n = v; l1 = [1, 2, 3], l2 = [4, 5, 6], assign_value(l1, l2), print(l1). What does this script print?
[19-copy_list.py](./19-copy_list.py) | Python function def copy_list(l): that returns a copy of a list
[20-answer.txt](./20-answer.txt) | a = (). Is a a tuple?
[21-answer.txt](./21-answer.txt) | a = (1, 2). Is a a tuple?
[22-answer.txt](./22-answer.txt) | a = (1). Is a a tuple?
[23-answer.txt](./23-answer.txt) | a = (1, ). Is a a tuple?
[24-answer.txt](./24-answer.txt) | a = (1), b = (1), a is b. What does this script print?
[25-answer.txt](./25-answer.txt) | a = (1, 2), b = (1, 2), a is b. What does this script print?
[26-answer.txt](./26-answer.txt) | a = (), b = (), a is b. What does this script print?
[27-answer.txt](./27-answer.txt) | a = [1, 2, 3, 4], id(a), 139926795932424, a = a + [5], id(a). Will the last line of this script print 139926795932424?
[28-answer.txt](./28-answer.txt) | a = [1, 2, 3], id (a), 139926795932424, a += [4], id(a). Will the last line of this script print 139926795932424?
[100-magic_string.py](./100-magic_string.py) | Python function magic_string() that returns a string “Holberton” n times the number of the iteration
[101-locked_class.py](./101-locked_class.py) | Python class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name

## Task 32
```
a = 1
b = 1
```

Files | Description
----- | -----------
[103-line1.txt](./103-line1.txt) | How many int objects are created by the execution of the first line of the script?
[103-line2.txt](./103-line2.txt) | How many int objects are created by the execution of the second line of the script?

## Task 33
```
a = 1024
b = 1024
del a
del b
c = 1024
```

Files | Description
----- | -----------
[104-line1.txt](./104-line1.txt) | How many int objects are created by the execution of the first line of the script?
[104-line2.txt](./104-line2.txt) | How many int objects are created by the execution of the second line of the script?
[104-line3.txt](./104-line3.txt) | After the execution of line 3, is the int object pointed by a deleted?
[104-line4.txt](./104-line4.txt) | After the execution of line 4, is the int object pointed by b deleted?
[104-line5.txt](./104-line5.txt) | How many int objects are created by the execution of the last line of the script?

## Task 34
```
print("I")
print("Love")
print("Python")
```

Files | Description
----- | -----------
[105-line1.txt](./105-line1.txt) | Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory?

## Task 35
```
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```

Files | Description
----- | -----------
[106-line1.txt](./106-line1.txt) | How many string objects are created by the execution of the first line of the script?
[106-line2.txt](./106-line2.txt) | How many string objects are created by the execution of the second line of the script?
[106-line3.txt](./106-line3.txt) | After the execution of line 3, is the string object pointed by a deleted?
[106-line4.txt](./106-line4.txt) | After the execution of line 4, is the string object pointed by b deleted?
[106-line5.txt](./106-line5.txt) | How many string objects are created by the execution of the last line of the script?
