# Input: Budget and quantity of components
budget = float(input())
num_gpus = int(input())
num_cpus = int(input())
num_ram = int(input())

# Fixed and derived prices
GPU_UNIT_PRICE = 250
total_gpu_price = num_gpus * GPU_UNIT_PRICE

# CPU price is 35% of total GPU cost
cpu_unit_price = total_gpu_price * 0.35
total_cpu_price = num_cpus * cpu_unit_price

# RAM price is 10% of total GPU cost
ram_unit_price = total_gpu_price * 0.10
total_ram_price = num_ram * ram_unit_price

total_price = total_gpu_price + total_cpu_price + total_ram_price

# Applying 15% discount if GPUs are more than CPUs
if num_gpus > num_cpus:
    total_price *= 0.85

# Final budget check
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
