import time
from ImmunePacking import ImmunePacking


start_time = time.time()
immune_packing = ImmunePacking()
immune_packing.init_population()
immune_packing.start()

print('Work time:')
print(time.time() - start_time)
