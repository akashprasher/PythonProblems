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

[Solution](./Solution%20Files/Cat-Cafes.py)

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

[Solution](./Solution%20Files/film.py)

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

[Solution](./Solution%20Files/Tax-Brackets.py)

### Probelem - 4. String formatting - How long is that word?

Write a program that calculates the length of a word from the input and prints it out together with the word in the format word has N letters. There will always be more than one letter in the word.

*Hint: Write a program that calculates the length of a word from the input and prints it out together with the word in the format word has N letters. There will always be more than one letter in the word.*

    Sample Input 1:

    serendipity
    Sample Output 1:

    serendipity has 11 letters

[Solution](./Solution%20Files/Lenth-of-word.py)

### Probelem - 5. Find the Runner-Up Score!

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

###### Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

###### Constraints
    2 <= n <= 10
    -100 <= A[i] <= 100

###### Output Format

Print the runner-up score.

Sample Input 0

    5
    2 3 6 6 5

Sample Output 0

    5

[Solution](./Solution%20Files/Runner-up-score.py)

### Problem - 6. For loop - The average of all numbers
Write the code that reads 2 numbers from the keyboard, a and b. As an output, it shows the mean of all numbers that lie on the interval between a and b, and can be divided by 3.

What does it mean? In the example, you are to calculate the mean of the numbers in the range [-5; 12][−5;12]

The numbers divided by 3 without the remainder are: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. There are six of them, and the mean is 4.5.

The input interval always contains at least one dividend of 3. Remember to include the values of a and b in your calculations.

Sample Input 1:

    -5
    12

Sample Output 1:

    4.5

[Solution](./Solution%20Files/The-average-of-all-numbers.py)

### Problem - 7. If statement - Cook book
Any recipe starts with a list of ingredients. Below is an abstract of a cookbook with the ingredients for some dishes. Write a program that tells you what recipe you can make based on the ingredient you have.

###### The input format:

A name of some ingredient.

###### The output format:

A message that says "food time!" where "food" stands for the dish that contains this ingredient. For example, "pizza time!". If the ingredient is featured in several recipes, write about all of them in the order they're featured in the cook book.

Sample Input 1:

    basil
Sample Output 1:

    pasta time!
Sample Input 2:

    flour
Sample Output 2:

    apple pie time!
    chocolate cake time!

[Solution](./Solution%20Files/Cook-book.py)

### Problem - 8. Monte Carlo simulation
Suppose that three random numbers are generated. Determine the probability that the numbers are in decreasing order using a Monte Carlo Simulation
