import random

trials = 100000
count = 0

for _ in range(trials):
    coin = random.choice(["Heads", "Tails"])
    die = random.randint(1, 6)
    
    if coin == "Heads" and die == 6:
        count += 1

experimental_probability = count / trials

print("Experimental Probability (Heads AND 6):", experimental_probability)
print("Theoretical Probability:", 1/12)
