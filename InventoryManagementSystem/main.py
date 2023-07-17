from cpu import CPU
from hdd import HDD
from ssd import SSD

cpu = CPU('Intel Core i9-9900K', 'Intel', 8, 'LGA 1151', 95, total=5)
hdd = HDD('Seagate Barracuda', 'Seagate', 1000, '2.5"', 7200, total=3)
ssd = SSD('Samsung 970 EVO', 'Samsung', 500, 'PCIe NMVe 3.0 x4', total=10)

cpu.claim(2)
hdd.claim(1)
ssd.claim(3)

print(cpu.allocated)
print(hdd.allocated)
print(ssd.allocated)

cpu.freeup(1)
hdd.freeup(1)
ssd.freeup(2)

print(cpu.allocated)
print(hdd.allocated)
print(ssd.allocated)

cpu.died(1)
hdd.purchased(2)
ssd.purchased(4)

print(cpu.total)
print(hdd.total)
print(ssd.total)

print(cpu)
