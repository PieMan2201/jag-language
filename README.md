jag-language
============

The language for beginners.

Jag is easy to read and write, and is meant to look like English. 
This makes it easy for people unfamiliar with programming concepts to get started.


Things you can do
=================

There are 9 things you can do in Jag.

You can set variables with the `set` command, like so:

```
set var1 to "hippos"
```

```
set var1 to var2
```

```
set var1 to var1 + 1
```

You can output things with the `speak` command, like so:

```
speak "hippos"
```

```
speak var1
```

```
speak 42
```

The `record` command is used to take input. You can use it in the following ways:

```
record var1
>>>[enter something here]
```

```
record "I need some input here! " to var1
>>>I need some input here! [enter something here]
```

Jag can convert as well. Here are some examples:

```
make var1 be "hippos" uppercase
#var1 now equals "HIPPOS"
```

```
make var1 be "VELOCIRAPTORS" lowercase
#var1 has been set to "velociraptors"
```

```
make var1 be "101" number
#var1 equals 101.0
```

```
make var1 be 202 string
#var1 is now "202"
```

There are some functions in Jag which you might not need to use very often, like `clear`,`pause`, and `sleep`. 

```
clear
#Clears screen
```

```
pause
>>>Press enter to continue 
```

```
sleep 10.5
#Don't do anything for ten and a half seconds.
```

Jag has `if` statements and comparisons.  

These comparisons are `equals`, `does not equal`, `is greater than`, and `is less than`.

Use them like this:

```
if var1 equals "hippos"
	[code]
end if
```

```
if 1 does not equal var1
	[code]
end if
```

```
if var1 is less than 7
	[code]
end if
```

```
if var1 is greater than 42
	[code]
end if
```

Finally, Jag has a `while` loop. You can make one like this:

```
while [comparison]
	[code]
end loop
```

While loops use the same comparisons that if statements do.

There are some things that were shown in the examples but not described. If you didn't understand them, here they are:

* Jag can do math with numbers and variables with number values (addition, subtraction, multiplication, and division).
* When putting code in a while loop or if statement, you must indent the code by one (1) tab.
* Jag only uses floating points so beginners won't be confused by trying to divide 1 by 2 and getting 0.


That's it! Have fun coding in Jag!
