import random
POPULATION_SIZE = 100
genes='abcdefghijklmnopqrstuvwxyz '
target='badri loves genetic algorithm'

def mutated_genes():
		gene=random.choice(genes)
		return gene

def create_gnome(): 
		gnome_len = len(target) 
		return [mutated_genes() for x in range(gnome_len)]

class Individual:
	def __init__(self,chromosome):
		self.chromosome=chromosome
		self.fitness=self.cal_fitness()

	def cal_fitness(self):
		fitness=0
		for i,j in zip(self.chromosome,target):
			if i!=j:fitness+=1
		return fitness

	def mutated_genes(self):
		gene=random.choice(genes)
		return gene
	def create_gnome(self): 
		gnome_len = len(target) 
		return [self.mutated_genes() for x in range(gnome_len)]
	def mate(self,par2):
		child_chromosome=[]
		for gp1,gp2 in zip(self.chromosome,par2.chromosome):
			prob=random.random()
			if prob<0.45:
				child_chromosome.append(gp1)
			
			elif prob<0.90:
				child_chromosome.append(gp2)

			else:
				child_chromosome.append(self.mutated_genes())
		return Individual(child_chromosome)

# x=create_gnome()
# print(x)
# print(len(target),len(x))

generation=1
found=False
population=[]

for i in range(POPULATION_SIZE):
	gnome=create_gnome()
	population.append(Individual(gnome))

while not found:
	population = sorted(population, key = lambda x:x.fitness)
	if population[0].fitness<=0:
		found=True
		break

	new_generation=[]
	s = int((10*POPULATION_SIZE)/100) 
	new_generation.extend(population[:s])

	s = int((90*POPULATION_SIZE)/100) 

	for i in range(s): 
		parent1 = random.choice(population[:50])
		parent2 = random.choice(population[:50])
		child = parent1.mate(parent2)
		new_generation.append(child)
	population = new_generation
	print("Generation: {}\tString: {}\tFitness: {}".
	format(generation, "".join(population[0].chromosome),population[0].fitness))
	generation += 1

print("Generation: {}\tString: {}\tFitness: {}".
format(generation, "".join(population[0].chromosome),population[0].fitness))