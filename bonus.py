import random
import numpy as np

# number of agents
n = 20

agents = []
for ii in range(n):
    # create an agent, who starts with no cash, and as an active trader
    agents.append({'money': 0})

    if ii < n - 1:
        # assign the first n-1 agents the fruit corresponding to their id
        # this doesn't bias anything, since the values are random, and no agent is preferred
        agents[ii]['fruit'] = ii
    else:
        # leftover agents are assigned a none fruit
        agents[ii]['fruit'] = None

    # agents are assigned a random value between 1 and 0 for each fruit
    # the assumption is made that the distribution of fruit utilities is uniform
    # and that that values of the good have no relationship to eachother
    # i.e. a person who things a banana is worth $10 might also overvalue other fruit in the real world
    agents[ii]['values'] = []
    for jj in range(n - 1):
        agents[ii]['values'].append(random.random())

unsteady = True
Alice = n-1
trades_count = 0

starting_value = 0
for agent in agents:
    if agent['fruit'] is not None:
        starting_value += agent['values'][agent['fruit']]

while unsteady:
    shuffled = list(range(len(agents)))
    random.shuffle(shuffled)
    # We are only going three people deep, and the example is this:
    # Alice buys from Bob, who buys from carol

    # Alice makes the first transaction she can find,
    # allowing bob to check with Carol before deciding if its worth it


    # I do not endorse the premise that economic activity generates real value
    # Eat the rich.

    unsteady = False

    for Bob in shuffled:
        if not Bob == Alice:
            fruit = agents[Bob]['fruit']
            alice_value = agents[Alice]['values'][fruit]
            bob_value_1 = agents[Bob]['values'][fruit]
            sale_price_1 = (alice_value + bob_value_1) / 2

            if alice_value > bob_value_1:
                print(f"{Alice} traded with {Bob}")
                agents[Alice]['money'] -= sale_price_1
                agents[Bob]['money'] += sale_price_1

                agents[Alice]['fruit'] = agents[Bob]['fruit']
                agents[Bob]['fruit'] = None
                Alice = Bob
                unsteady = True
                trades_count +=1
                break

            elif alice_value < bob_value_1:
                bob_loss = bob_value_1 - sale_price_1
                for Carol in shuffled:
                    if (not Carol == Alice) and (not Carol == Bob):
                        fruit_2 = agents[Carol]['fruit']
                        bob_value_2 = agents[Bob]['values'][fruit_2]
                        carol_value = agents[Carol]['values'][fruit_2]
                        sale_price_2 = (bob_value_2 +carol_value)/2

                        bob_gain = bob_value_2 - sale_price_2

                        if bob_gain + bob_loss > 0:
                            print(f"{Alice} traded with {Bob} who traded with {Carol}")
                            agents[Alice]['money'] -= sale_price_1
                            agents[Bob]['money'] += sale_price_1

                            agents[Alice]['fruit'] = agents[Bob]['fruit']
                            agents[Bob]['fruit'] = None

                            agents[Bob]['money'] -= sale_price_2
                            agents[Carol]['money'] += sale_price_2

                            agents[Bob]['fruit'] = agents[Carol]['fruit']
                            agents[Carol]['fruit'] = None
                            Alice = Carol
                            unsteady = True
                            trades_count += 2
                            break
                break
final_value = 0
for agent in agents:
    if agent['fruit'] is not None:
        final_value += agent['values'][agent['fruit']]

print(f"Trades: {trades_count}")
print(f"Starting value: {starting_value}")
print(f"Final value: {final_value}")
print('Done.')
