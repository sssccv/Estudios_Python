import random
import time
print("****Cuando aparezca la señal, presiona cualquier botón****")
random_time= random.uniform(0,8)
time.sleep(random_time)
time_start=time.time()
input("AHORA******")
time_end=time.time()
print(f"Tardaste {time_end-time_start:.3f}s en reaccionar")

