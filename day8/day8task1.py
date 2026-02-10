import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

meanscores = scores.mean(axis=0)

centeredscores = scores - meanscores

print("Original Scores:\n", scores)
print("\nMean of Each Subject:\n", meanscores)
print("\nCentered (Normalized) Scores:\n", centeredscores)
