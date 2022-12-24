import random
from deap import base, creator, tools, toolbox, num_bits

#Define the evaluation function
def evaluation_funct(individual):
    target_sum = 15
    return len(individual) - abs (sum(individual) - target_sum),

#Toolbox with the right parameters -
def create_toolbox(num_bits):
    creator.create("FitnessMAX", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

#initialize the toolbox
    toolbox = base.toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
	toolbox.attr_bool, num_bits)
toolbox.register("Populations", tools.initRepeat, list, toolbox.individual)

#Register the evaluation operator -
toolbox.register("evaluate", evaluation_funct)

#Register the crossover operator - 
toolbox.register("mate", tools.cxTwoPoint)

#Register a mututation operator -
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.05)

#Define the operator for breeding - 
toolbox.register("selection", tools.selTournament, tournsize = 3)
#return toolbox
if __name__ == "__main__":
    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)
    populations = toolbox.populations(n= 500)
    probabiliti_crossing, probabiliti_mutating = 0.5, 0.2
    num_generations = 10
    print('\nEvolution Process Started')

#Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, populations))
for ind, fit in zip(populations, fitnesses):
    ind.fitness.values = fit
print('\nEvaluated', len(populations), 'individual')

#Create and Iterate through generations -
for g in range(num_generations):
    print("\n- Generation", g)

#Selecting the next generation individuals -
offspring = toolbox.select(populations, len(populations))

#clone selected individuals - 
offspring = list(map(toolbox.clone, offspring))

#Apply crossover and mutation on the offspring -
for child1, child2 in zip(offspring[::2], offspring[1::2]):
    if random.random() < probabiliti_crossing:
        toolbox.mate(child1, child2)

#Delete the fitness value of the child
del child1.fitness.values
del child2.fitness.values

#Apply mutation -
for mutant in offspring:
    if random.random() < probabiliti_mutating:
        toolbox.mutate(mutant)
        del mutant.fitness.values

#Evaluate the individuals with an invalid fitness -
invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
fitnesses = map(toolbox.evaliuate, invalid_ind)
for ind, fit in zip(invalid_ind, fitnesses):
    ind.fitness.values = fit
print('Evaluated', len(invalid_ind), 'individuals')

#Replace population with next generation individuals -
populations[:] = offspring

#Print the statistics for the current population/generation
fits = [ind.fitness.values[0] for ind in populations]
length = len(populations)
mean = sum(fits) / length
sum2 = sum(x*x for x in fits)
std = abs(sum2 / length - mean**2)**0.5
print('Min =', min(fits), 'Max =', max(fits))
print('Average =', round(mean, 2), ', STANDARD DEVIATION =', round(std, 2))
print("\n- Evolutions Ends")