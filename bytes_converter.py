'''
@author: Abdelrahman Moez - aka Hydra
@script: bytes_converter.py
@description: This snippet converts given bytes into
@python version: 2.7
'''
GIGA_BYTE = 1073741824
MEGA_BYTE = 1048576
KILO_BYTE = 1024

def bytes_converter(bytes):
	
	bytes = float(bytes)
	
	num_of_gb = int(bytes/GIGA_BYTE)
	rem_bytes_1 = int(bytes-(num_of_gb*GIGA_BYTE))

	num_of_mb = int(rem_bytes_1/MEGA_BYTE)
	rem_bytes_2 = int(rem_bytes_1-(num_of_mb*MEGA_BYTE))

	num_of_kb = int(rem_bytes_2/KILO_BYTE)
	rem_bytes_3 = int(rem_bytes_2-(num_of_kb*KILO_BYTE))

	num_of_bytes = rem_bytes_3
	
	return (num_of_gb, num_of_mb, num_of_kb, num_of_bytes)

_bytes = 5457707520
print bytes_converter(_bytes)
# OUTPUT: (5, 84, 896, 512)
