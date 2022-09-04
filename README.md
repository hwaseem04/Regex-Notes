# Regex-Notes

## **Regular Expressions (Regex)**
> Regular expressions are widely used in computer science for the purpose of pattern matching. Let say you are searching for a string which exactly matches certain pattern (or specification of your need), then regex comes handy here.

<br>

 This notes is based on python module `re` (stands for _regular expression_). Execute the below command to import the module.

```python
import re
```

<br>

## **Problem**
 Let us consider the case where you need to get user input as email id, and you need to accept only those emails which are valid (Valid in sense, not checking for domain names, rather we will be checking general syntax of a email id)
<br>

<br>

## 1) re.search( _pattern_ , _string_ [,_flags_]) 
>re.search is the most commonly used functionality in this module.

<br>
The following code will be subjected to change upon each new concepts.

<br>

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

```

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")

```
```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

```
```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(".+@.+\.in", email):
    print("Valid")
else:
    print("Invalid")

```

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search("^.+@.+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search("^\w+@\w+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search("^\w+@\w+(\w+\.)?\.in$", email):
    print("Valid")
else:
    print("Invalid")

```