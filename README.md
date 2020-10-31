# Python Problems

### Probelem - 1. Loop control statements - Cat cafés
Kitty wants to visit a cat café! Help her find the one with the largest number of cats.

###### Input format

Each string contains a café's name followed by a space and the number of cats in it, e.g. Paws 11, Kittens 9.

The names would be one-word only. Read input lines until you get a string MEOW (without any number).

###### Output format

The café with the maximum number of cats.

    Sample Input 1:

    Paws 11
    Kittens 9
    MEOW

    Sample Output 1:

    Paws

[Solution](./Cat-Cafes.py)

### Probelem - 2. String formatting - Film

Write a program that gets information about a movie from the input and presents in the following format:

    movie (dir. director) came out in year

###### The input format:

3 lines: first the title of the movie, then the name of the director and then the year of its release.

    Sample Input 1:

    Fight Club
    David Fincher
    1999
    Sample Output 1:

    Fight Club (dir. David Fincher) came out in 1999

[Solution](./film.py)

### Probelem - 3. String formatting  Tax brackets

In progressive tax systems, tax rates change according to the income. Tax brackets are divisions that regulate those changes.

Here's an example of tax brackets in a certain tax system:

    0 — 15,527: 0% tax

    15,528 — 42,707: 15% tax

    42,708 — 132,406: 25% tax

    132,407 and more: 28% tax

Suppose we use a simplified version of taxation and apply one tax rate to the entire amount of money.

Write a program that calculates the tax that a person's going to pay based on their income.

###### The input format:

The value of someone's taxable income (in dollars).

###### The output format:

The tax for {income} is {percent}%. That is {calculated_tax} dollars!

__*Round your calculated_tax to the nearest integer.*__


    Sample Input 1:

    14378
    Sample Output 1:

    The tax for 14378 is 0%. That is 0 dollars!
    Sample Input 2:

    99999
    Sample Output 2:

    The tax for 99999 is 25%. That is 25000 dollars!

[Solution](./Tax-Brackets.py)