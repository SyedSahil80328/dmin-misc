import scipy.stats as stats

def getCriticalValue(df, significanceLevel):
    return stats.chi2.ppf(1 - significanceLevel, df)

# Example usage
with open ("DataSheets.csv", "r") as file:
    data = file.readlines()
    observedFrequencies = list(map(float, data[0].strip().split(',')))
    expectedFrequencies = list(map(float, data[1].strip().split(',')))
    significanceLevel = float(data[2])
    h0 = data[3].strip()
    h1 = data[4].strip()

observations = len(observedFrequencies)
degreesOfFreedom = observations - 1
criticalValue = getCriticalValue(degreesOfFreedom, significanceLevel)

print(f"H0: {h0}.")
print(f"H1: {h1}.")

print(f"Critical Value: {criticalValue}.")

chiSquareValue = 0
for i in range(observations):
    chiSquareValue = chiSquareValue + ((observedFrequencies[i] - expectedFrequencies[i]) * (observedFrequencies[i] - expectedFrequencies[i])) / expectedFrequencies[i]

print(f"Chi Square value: {chiSquareValue}.")

acceptedHypothesis = h0 if chiSquareValue <= criticalValue else h1
print(f"Thus, it is accepted that {acceptedHypothesis}.")
