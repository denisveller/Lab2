import VL53L0x

VL = VL53L0x.VL53L0X()

measured = VL.read_range()
print(measured)