# Regex-Notes

<!--- 
> Following tutorial is a summary of this [CS50 lecture](https://www.youtube.com/watch?v=hy3sd9MOAcc&t=4218s "CS50P - Lecture 7 - Regular Expressions") <br>
-->

> For official documentation, visit [Python Regular Expressions](https://docs.python.org/3/library/re.html "Regular Expressions")

<br>

## **Regular Expressions (Regex)**


> Regular expressions are widely used in computer science for the purpose of pattern matching. Let say you are searching for a string which exactly matches certain pattern (or specification of your need), then regex comes handy here.

<br>

 This notes is based on python module `re` (stands for _regular expression_). Execute the below command to import the module.

```python
import re
```

<br>

## **Problem**
 Let us consider the case where you need to get user input as email id, and you need to accept only those emails which are valid (Valid in sense, not checking for domain names, rather we will be checking general syntax of a email id more strictly)
<br>

<br>

## 1) re.search( _pattern_ , _string_ [,_flags_]) 
>re.search is the most commonly used functionality in this module. _flags_ is optional.

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
In the above code I have passed `@` as the pattern to match in `re.search()`. What this means is that any string which has `@` will be displayed as **Valid**. Let us improvise it a bit using following special characters in _re_ literature.

<br>

| Special Characters | Meaning  |
| ------------------ | -------- |
| .                  |  Match any character except newline character     |
| *                  |  Allow 0 or more repetition of previous character |
| +                  |  Allow 1 or more repetition of previous character | 
| ?                  |  Allow 0 or 1 repetition of previous character    | 
| {m}                |  Allow m repetitions of previous character        | 
| {m,n}              |  Allow m - n repetitions of previous character    | 

<br>

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

```
In the above code, notice I have used `.+` before and after `@`, i.e `.+@.+`<br>
What this means is at I am trying to match a string that should have _1 or more_(specified by `+`) _characters, except newline_ (specified by `.`). 

<br>

But this is not just enough, if we input something like `hello@@some` is going to still print as VALID email as we havent set any restriction for **domain** syntax, number of **@** etc. There are still lot of other issues which I will deal one by one.

---
<br>

Let us now first set a restriction for the ending of email address (Something specific to INDIA, i.e `.in`)
```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(r".+@.+\.in", email):
    print("Valid")
else:
    print("Invalid")

```

In the above code notice I have used `\.in` which mean I am trying to match for a string which exactly has something like **.in** in it. (NOTE : I am not doing anything to specify that the matching string **must** end with **.in**, which I will show in a moment)
<br>

>**_Few points to note:_**
* I am using `\.` because to avoid confusion with special character `.`, hence my regex looks for a exact `.` in the input string.
* I am using `r" "` i.e rawstring, inorder to avoid python to misinterpret anything inside it with escape sequence. It is advisable to use rawstring whenever you use `\` in regex for programmer's convenience. 
    * In a Raw String escape sequences are not taken into account.
* Still I havent restricted repetation of `@`. And still string input like `asdf %%some@@something.in ada` is valid, as we have'nt laid a strict starting and ending condition (so as to start with **proper username** and end with just **.in**).
---
<br>

>Let us now see how we can set restriction for beginning and ending of the input string.

| Special Character | Meaning |
| ----------------- | ------- |
| ^                 | Specifies the begininning |
| $                 | Specifies the end         |

The Description which I have used above will be different from that of the official documentation. But it conveys the same meaning.
```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(r"^.+@.+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

In the above code `^` & `$` specifies the beginning and ending of the pattern which we are looking for. So the beginning condition as per our pattern above is that we are looking for _1 or more characters_ . 

Hence the string input `asdf %%some@@something.in ada` is invalid as we have ` ada` after `.in`. 

But still `asdf %%some@@something.in` input is valid because we have'nt set any condition for the characters that are allowed for username(i.e characters before `@`), hence characters like `%`, *whitespaces*, even `@` are still allowed. Let us finetune it further. 

---
<br>

| Special Character | Meaning |
| ----------------- | ------- |
| []                 | Specifies the set of characters allowed |
| [^]                | Specifies the set of characters not allowed |

* `[a-zA-Z0-9_\.]` Something like this specifies that the allowed characters must be Alphanumeric or underscores or periods (remember the usecase of `\.` which I described above).

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_]+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

Description of `^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.in$` is provided below : 
* `^[a-zA-Z0-9_\.]+` : It allows atleast _one or more_ Alphanumeric or underscores or period characters in the beginning of the string before `@` (i.e for username in email).
* `[a-zA-Z0-9_]+\.in$` : It allows atleast _one or more_ Alphanumeric or underscores  in the string after `@`(i.e for domain name), and must end with `.in`.
* Hence it also restricts number of `@` which can be given in the input.

<br>

**For the above _regex pattern_ few invalid inputs are**
* someword hi@hello.in - Because there is whitespace character
* h%i@hello.in - Because `%` is used
* hi@@hello.in - Because multiple `@` is used
* @hello.in - Because 0 characters before `@`
* hi@.in - Because 0 characters between `@` and `.in`

---
<br>
The above regex pattern can be more succinctly written with the help of below special characters

<br>

| Special Character | Meaning |
| ----------------- | ------- |
| \d                |  Only decimal digit allowed|
| \D                |  Except a Decimal digits all other characters are allowed|
| \s                |  Only whitespace characters like space, tab are allowed |
| \S                |  Except a whitespace characters all other characters are allowed|
| \w                |  Only AlphaNumeric and underscores are allowed|
| \W                |  Except AlphaNumeric and underscores all other characters are allowed|

<br>

```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(r"^\w+@\w+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

In the above code instead of `[a-zA-Z0-9_]` I have used `\w` which almost conveys the same meaning except that `\w` doesnt allow periods. 

There is one other way to specify that as well by **grouping** and by using `|` **or** operator, which I will discuss later in the tutorial.

As for as now our regex pattern doesnt allow **periods** with `\w`.

---
<br>

What if someone's email has multiple domain like **snuchennai.edu.in**, we need to modify our regex pattern to allow such possibilities as well. We can do that with following additional special characters.

| Special Character | Meaning |
| ----------------- | ------- |
| A\|B              |  Either pattern A or patter B allowed|
| (...)             |  Parenthesis can be used to group special characters|


```python
import re

# Using split to just trim of any trailing whitespaces
email = input("Email : ").split()  

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.in$", email):
    print("Valid")
else:
    print("Invalid")

```

In the above code `(\w+\.)?` specifies we can have _0 or 1 repetitions(recall usage of `?` in above table)_ of `\w+\.` as it is grouped using `()`.

Hence our pattern accepts domains like `.in` _(i.e with 0 repetation of `\w+\.`)_ **or** `.edu.in` _(i.e with 1 repetation of `\w+\.`)_.

Also notice the usage of `(\w|\.)` (read as *word character or period*) which now allows usage of **periods** as well in username.
