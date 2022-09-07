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
---

### **Question**
 Let us consider the case where you need to get user input as email id, and you need to accept only those emails which are valid (Valid in sense, not checking for domain names, rather we will be checking general syntax of a email id more strictly). 
<br>

## 1) re.search( _pattern_ , _string_ [,_flags_]) 
>re.search is the most commonly used functionality in this module. _flags_ is optional. Let us solve the above question with this.

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
| (?: ...)          |  Non capturing version of above one|

Dont worry about the 3rd one for now, will let you know in a moment.

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

---

In re.search() there is one other amazing functionality involving `()` and `(?:)`.

> What if you, not just want to match a pattern but also want to extract specific information from the matched pattern?

Offcourse with usual python coding you can attain that, but re.search() offers more functionality. Anyway lets see below both traditional pythonic way and regex way for one such example.

**Consider the Question below**
* You want to get user input their name, but along with their first and last name. Users input their name mostly in either of the below formats
    * FirstName LastName
    * LastName, FirstName
* We need to write a code where we can get their proper names irrespective of the above formats.

<br>

The solution in usual pythonic way
```python
name = input("What's your name? ").strip()
if "," in name:
    last,first = name.split(", ") # Assuming barely that user will give space after comma (i.e lastname, firstname)
    name = f"{first} {last}"
# If no comma is there we can directly print it.
print(name)
```

But there are few issues in the above code :
* What if user types with a space after comma? i.e `lastname,firstname`. The split function cant split anything and throws error because we are unpacking it with two variables.
* What if someone has name like `Robert Downy Jr` where they vaguely give input as `Downy, Robert, Jr`. It will also pop out error, as we are unpacking only two items in split function.

<br>

Let us see regex solution

```python
import re
name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name) :
    print(matches)
    last, first = matches.groups()
    #last = matches.group(1)
    #first = matches.group(2)
    name = f"{first} {last}"

print(name)
```

There are a couple of things going on above, let me break down one by one.
* Python supports Walrus operator from python 3.8 onwards. It does both assignment job and checks for boolean value of the variable in LHS.
<br>
* In the above regex pattern 
    * `^(.+)` matches 0 or more charcters except newline in beginning
    * `, *` maches for a comma and whitespace _(0 or more white space)_
    * `(.+)$` matches 0 or more charcters except newline in the end
<br>
* So far, in the above codes we checked just the boolean value of `re.search()`, if its true then we declared our pattern is matched with input string, else not. But with return value of `re.search()`, one other interesting thing can be achieved.
<br>
* When we use `()` in our regex pattern it captures whatever string input matched within in. What it means is that, in the above code `(.+)` this matches any character _(0 or more repetations)_. So the first and second `()` captures each of the string matched to `.+` from the input. 
<br>
* And the captured string can be obtained by grouping the captured string(In some sort of order, so that we can access them with some index) using `groups()`  or `group()` as done above.
<br>
* Unlike usual python conventions of index starting at 0, here inorder to acces string matched inside first `()` we have to access them with index 1, i.e `matches.group(1)`.
<br>
* And then we are using usual [f strings](https://docs.python.org/3/tutorial/inputoutput.html "f Strings Documentation") to get the right format.
<br>

> Example : If the input is `Khan,Sal`. Then `first = Sal` and `last = Khan`.

**What if you dont need to capture anything unnecessarily in `re.search()`, here comes the non capturing version which I alluded you above `(?:some_regexpattern)`. For the above code if we dont want to capture then the regex will be `re.search(r"^(?:.+), *(?:.+)$", name)`.**

---

A lot of stuff, isn't it ?
But `re.search` is not the only function in `re` module.
* `re.match()` - Similar to `re.search()`, except you dont need to explicitly provide `^` to specify beginning. 
* `re.fullmatch` - Similar to `re.search()`, except you dont need to explicitly provide `^` and `$`to specify beginning and ending.

>*__SelfNote__* :  
* `..*` is same as `.+`
* `re.IGNORECASE` is a flag which avoids checking case sensitivity in user input. 
---
---

## 2) re.sub()
