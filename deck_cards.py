'''
create a card of deck with for loop
'''


alpha_numeric = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
objects = ['oros', 'copas', 'espadas', 'bastos']

deck = []

for alf_num in alpha_numeric:
    for obj in objects:
        card = f'{alf_num} de {obj}'
        deck.append(card)

#print(deck)
# print order by alpha_numeric
for i in range(0, 40, 4):
    print(f'{deck[i]} {deck[i+1]} {deck[i+2]} {deck[i+3]}')