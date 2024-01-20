# Constrains (cantidad minima de producción de cada producto y de )
MIN_PRODUCT_A = 4
MAX_PRODUCT_B = 2
MIN_TOTAL_PRODUCTION = 6


# func fitness (función que permite evaluar cuanto de correcta esta la solución, es la función mas compleja de los problemas de optimización) schedule es la variable de entrada...(despues se hablara de ella)
def calculate_fitness(schedule):
  product_a = schedule.count('1') #Cuentan 0 y unos.
  product_b = schedule.count('0') #Cuentan 0 y unos.
  total_production = product_a + product_b
  profit = product_a * PROFIT_A + product_b * PROFIT_B

  #SE CHEQUEAN LAS CONSTRAINS
  if product_a < MIN_PRODUCT_A or product_b > MAX_PRODUCT_B or total_production < MIN_TOTAL_PRODUCTION:
    return 0 # DEVUEVE UN 0 PORQUE NO SE CUMPLEN LAS CONSTRAIN, Y AL SER UN PROBLEMA DE MAXIMIZACIÓN, SE PONE 0 Y ASI SE SABE QUE NO INTERESA TAL RESULTADO.
    #return 10000000000 #si min
  else:
    return profit


# GENERAR LA POBLACIÓN, ESTA VEZ EN VEZ DE SER UN VECTOR, VA A SER UN VECTOR(50 vectores) DE VECTORES (8 NUM por vector)...
population = []
for i in range(POPULATION_SIZE):
  schedule = ''
  for j in range(8):
    schedule += str(random.randint(0,1)) # para strings, el += sirve para concatenar
  population.append(schedule) # El .apend sirve para añadir a una lista (arredlo) en este caso se está AÑADIENDO el vector de 8 (schedule) a la matriz Population


for generation in range(GENERATIONS):

  fitness = [calculate_fitness(schedule) for schedule in population]

  parents = [population[i] for i in range(POPULATION_SIZE) if fitness[i] == max(fitness)]  # min si min

  population = []
  for i in range(POPULATION_SIZE):

    parent1 = random.choice(parents)
    parent2 = random.choice(parents)

 # En este caso en vez de sumar y dividir, simplemente coge valores de uno y los concatena con valores del otro
    crossover_point = random.randint(1, 7)
    schedule = parent1[:crossover_point] + parent2[crossover_point:]

    for j in range(8):
      if random.random() < MUTATION_RATE:
        schedule = schedule[:j] + str(1-int(schedule[j])) + schedule[j+1:]

    population.append(schedule)

best_schedule = population[fitness.index(max(fitness))] # min si min
print("Best schedule:", best_schedule)
print("Profit:", calculate_fitness(best_schedule))