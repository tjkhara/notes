# Regular Expressions

Example 1:

Mobile numbers with 10 digits and first digit should be 6,7,8,9

Group of strings following a particular pattern then user regular expression.

Regular expressions are a declarative mechanism.

### What are the important application areas for regular expressions?

Theory of computation a large part is regular expressions.

Form input checking.

    pattern = re.compile(r'\d\d\d[-*.]\d\d\d[-*.]\d\d\d\d')

This will only match either a - or a * or a . after three digits. Point of confusion for many people is that this should match more than one character.
But only one character is matched.


The - is a special character as well. When placed at the beginning or the end it looks for the literal dash character.
But, when placed between values it specifies a range of values.
    
    pattern = re.compile(r'[1-5]')

This will match digits between 1 and 5.

We can do the same thing for letters as well. The following will match lowercase letters.


    pattern = re.compile(r'[a-z]')


### Matching uppercase or lowecase letters we can put the ranges back to back


    pattern = re.compile(r'[a-zA-Z]')

### The ^

Outside a character set the ^ will look for the start of the string
But, inside the character set it is a negation


    pattern = re.compile(r'^[a-z]')

### How to do a negative search

	pattern = re.compile(r'[^a-zA-Z]')

This will search for all the characters that are not in a-z or A-Z

This will match everything that is not a lowercase or an uppercase letter.

### What if we want to match the following words?

cat, mat, hat

but we don't want to match bat

	pattern = re.compile(r'[^b]at')

The way to think about this expression [^b]at is that everything that is not a b followed by at.

### Using quantifiers to match more than one character at once

	pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

This above pattern will match any character after the digits.

Note that this is different from the following:

pattern = re.compile(r'\d\d\d[.]\d\d\d[.]\d\d\d\d')

Because here only the . will be matched.


We can use quantifiers like this:

	pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

### Next example Mr Mrs etc

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

	pattern = re.compile(r'Mr\.')

This will find Mr.

#### How do we say that the period after the Mr is optional?

	pattern = re.compile(r'Mr\.?')

The ? tells the search that there can be 0 or 1 periods.

	pattern = re.compile(r'Mr\.?\s')

Now after the optional period we are searching for a space

Then after the space we are looking for capital letters like this

	pattern = re.compile(r'Mr\.?\s[A-Z]')

After this we can add \w+

This means any word character 1 or more times

	pattern = re.compile(r'Mr\.?\s[A-Z]\w+')

This is matching the following:

Mr. Schafer
Mr Smith

But it is not matching Mr. T

The better solution might be to use the * quantifier which matches 0 or more

	pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

This matches the following:

Mr. Schafer
Mr Smith
Mr. T

### Now we have to think about how to search for Ms or Mrs or Mrs.

The solution here would be to use a group

Groups allow us to match several different patterns.

To create a group we use ()

	pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

This expression means that after the M there can be an r or an s or an rs

Mr
Ms
Mrs

We are already checking for the 0 or more instances of a .

This can also be written as

	pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

Groups can also be used to capture sections of the matched regular expressions.


## findall

	sentence = 'Start a sentence and then bring it to an end'

	pattern = re.compile(r'[a-z]')

	matches = pattern.findall(sentence)

	for match in matches:
		print(match)

findall will return a list of strings.

or

it will return the groups if you are matching for groups.

	pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

In the above pattern if you do

	matches = pattern.findall(sentence)

	for match in matches:
		print(match)

It will only return the group.

If there are multiple groups, it will return a list of touples.


## match

Match does not return an iterable. It just returns the first match.

This only searches at the **beginning** of the string

	sentence = 'Start a sentence and then bring it to an end'

	pattern = re.compile(r'Start')

	matches = pattern.match(sentence)

	print(matches)

This will give the result Start.

But, if you try to search sentence you will not find it.

## search - to search the entire string

	sentence = 'Start a sentence and then bring it to an end'

	pattern = re.compile(r'sentence')

	matches = pattern.search(sentence)

	print(matches)

This will also only print out the **first match** but it will search the entire string.

## Case insensitive search and adding a flag to the pattern

	sentence = 'Start a sentence and then bring it to an end'

	pattern = re.compile(r'[Ss][Tt][Aa][Rr][Tt]')

	# instead of the above do the following

	pattern = re.compile(r'start', re.IGNORECASE)

	matches = pattern.search(sentence)

	print(matches)

### shorthand for this is

	pattern = re.compile(r'start', re.I)