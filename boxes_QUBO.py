import dimod

# Boxes problem with gamma = 20
# INPUT your QUBO here
Q = {}

# Change the solver/sampler if you wish
exactsolver = dimod.ExactSolver()

# INPUT the offset on the next line
bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=HERE)

results = exactsolver.sample(bqm)

# First, print the results, showing the sums - this helps confirm the QUBO
# is correct
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)
