pip install mlrose

import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np

coords_list = [(41.40209235652407, 2.118936631204517),(41.37268741480335, 2.1877191438746575),(41.39081352872017, 2.150423800432648),(41.28860982570802, 2.077842119190889),(41.26635162858465, 1.9676264245849826),(41.373283740123114, 2.177236343971647),(41.3810334317756, 2.122847936003876),(41.39121866636425, 2.143526483783644),(41.2955322366412, 2.1243259996950523),(41.40427746558141, 2.1512244879953815)]
fitness_coords = mlrose.TravellingSales(coords = coords_list)

dist_list = [(0, 1, 8.2), (0, 2, 4.1231), (0, 3, 3.5), (0, 4, 20.1), \
             (0, 5, 24.9), (0, 6, 6.9), (0, 7, 3.6), (0, 8, 15.7), \
             (0, 9, 3.8), (1, 2, 5.4), (1, 3, 23.5), (1, 4, 31), \
             (1, 5, 2.2), (1, 6,8.3), (1, 7, 6), (1, 8, 17), \
             (1, 9, 5.9), (2, 3, 21.4), (2, 4, 26.4), (2, 5, 3.7), \
             (2, 6, 3.5), (2, 7, 0.9), (2, 8, 15), (2, 9, 2.2), \
             (3, 4, 11), (3, 5, 16), (3, 6, 16.6), (3, 7, 15.6), \
             (3, 8, 6.4), (3, 9, 18), (4, 5, 26), (4, 6, 21.2), \
             (4, 7, 26.9), (4, 8, 18), (4, 9, 29), (5, 6, 6.4), \
             (5, 7, 4), (5, 8, 15.1), (5, 9, 4.4), (6, 7, 3.5), \
             (6, 8, 11.9), (6, 9, 5.7), (7, 8, 14.4), (7, 8, 2.9), \
             (8, 9, 16.9)]

fitness_dists = mlrose.TravellingSales(distances = dist_list)

problem_fit = mlrose.TSPOpt(length = 10, fitness_fn = fitness_coords, maximize=False)
# SI el Maximize = FALSE, implica que se esta minimizando.

best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)

best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, max_attempts= 100, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)

best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.3, max_attempts= 100, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)

best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.4, max_attempts= 100, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)

best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.5, max_attempts= 100, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)

best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.1, max_attempts= 100, random_state = 2)

print('The best state found is: ', best_state)
print('The fitnessat the best state is: ', best_fitness)