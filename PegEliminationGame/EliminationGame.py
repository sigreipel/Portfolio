# Svetlana Greipel
# Peg Elimination Game
from PegEliminationGame import AIRules

m = AIRules.Rules()
m.load_from_file("square.txt")

col = 0
row = 0
x = ""
print(m)
while x != "q" and m.winning_condition() != True:
    x = input("Enter an integer x (q for quit) ")
    if x == "q":
        break
    y = input('Enter an integer for y ')
    z = input('Enter w: up a: left s: down or d: right ')

    m.peg_eliminator(int(x), int(y), z)
    print(m)
    m.clean_board()
