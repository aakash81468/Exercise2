import itertools

def calculate_probability(N, letters, K):
    total_combinations = list(itertools.combinations(range(N), K))
    combinations_with_a = [comb for comb in total_combinations if 'a' in [letters[i] for i in comb]]
    probability = len(combinations_with_a) / len(total_combinations)
    return probability

# Read the input
N = int(input())
letters = input().strip()
K = int(input())

# Calculate and print the probability
probability = calculate_probability(N, letters, K)
print(f"{probability:.4f}")
