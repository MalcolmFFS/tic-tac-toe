# tic-tac-toe
Just a python based, tty tic-tac-toe game for coding practice.

The game is scalable and will make a board of a size submitted by the user.
The win condition is a minimal of 3 sequential marks for smaller board sizes. For larger board sizes, the win condition is half the size given by the user, or half the size + 1 if the number given is odd. 

This program is functional, but not full featured as far as what I believe to be in my skill range, or close but that could be a learning opportunity.

Future intentions when/if I get the time for busywork practice code:
 - OOP: sadge
 - Dirty Lanes: (I really don't look forward to doing this since implementing `check_all_diagonals_1()`) The game can go on for too long at larger board sizes, if I start checking that win conditions (lanes) are no longer achievable (dirty), once all are dirty, end the game early instead of waiting for the entire board to be filled to declare a draw.
 - Bot Player / Single-Player Mode: Once I have the concept of dirty lanes setup, it is a much smaller task to make a bot player so this can be a single-player game. The bot would not make plays in unwinnable lanes, adding some difficulty above random marks. The bot would also make plays in "high value" lanes, meaning lanes that it already has a mark on, preferrably identifying which lane has the most marks. I expect I'll be able to piggy-back off dirty lanes code for most of this.
 - ~~Table Input~~(Done)
 
## Intent In Writing
I'm new to Python, and am generally just trying to learn to code in a professional way. I've been "learning" Python for over a year, but mostly at a pace of 1 week on, 4 months off. I consider my "I'm ready to actually practice Python" date as being September 18th, 2019 - this was when I finished the non-project portions of "Python Crash Course" by Eric Matthes, and can actually claim I had the functional basics of the language down.

Here I'm defining "professional" as scalable, lean functions, a relatively clean flow of code for readers and keeping it pythonic.

The main challenges for myself here was making everything scalable. From board construction to win condition checking. The main thing I personally needed to avoid was massive if/elif/else tables checking every possible position on the board.

It was not my intent to focus on the CX aspect of the code writing, as that's not something I can apply much to my current or short-term intended jobs. I am using this as a programming logic challenge.
