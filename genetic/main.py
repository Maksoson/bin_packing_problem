import time
from GeneticPacking import GeneticPacking


start_time = time.time()
genetic_packing = GeneticPacking()
genetic_packing.init_population()
genetic_packing.start()

print('Work time:')
print(time.time() - start_time)
