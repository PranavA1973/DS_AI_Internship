import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.exponential(scale=2, size=100000)

print("Population Mean:", np.mean(population))
print("Population Std Dev:", np.std(population))

def generate_sample_means(population, sample_size, num_samples=1000):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size)
        means.append(np.mean(sample))
    return np.array(means)


means_5 = generate_sample_means(population, 5)

plt.figure()
plt.hist(means_5, bins=30, density=True)
plt.title("Distribution of Sample Means (n=5)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

print("n=5 Mean of Sample Means:", np.mean(means_5))
print("n=5 Std Dev of Sample Means:", np.std(means_5))


means_30 = generate_sample_means(population, 30)

plt.figure()
plt.hist(means_30, bins=30, density=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

print("n=30 Mean of Sample Means:", np.mean(means_30))
print("n=30 Std Dev of Sample Means:", np.std(means_30))

means_100 = generate_sample_means(population, 100)

plt.figure()
plt.hist(means_100, bins=30, density=True)
plt.title("Distribution of Sample Means (n=100)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()

print("n=100 Mean of Sample Means:", np.mean(means_100))
print("n=100 Std Dev of Sample Means:", np.std(means_100))

print("\nTheoretical Standard Errors:")
print("n=5   :", np.std(population) / np.sqrt(5))
print("n=30  :", np.std(population) / np.sqrt(30))
print("n=100 :", np.std(population) / np.sqrt(100))
