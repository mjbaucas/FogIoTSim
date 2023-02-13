import matplotlib.pyplot as plt

sizes = ["1", "2", "4", "8", "16", "32"]
plt.grid(visible=True, color='gray', linestyle=':')
plt.plot(sizes, [5523.80, 5125.47, 5056.50, 5205.75, 4837.5, 4685.75], label="Cloud Setup", color="green", marker="*")
plt.plot(sizes, [6000, 6234.31, 6317.45, 6166.50, 5711.57, 4937.59], label="Fog Setup", color="red", marker="o")

plt.legend(loc='best')
plt.xlabel('Packet Size (KB)')
plt.ylabel('Average Packet Count')
plt.savefig("throughput.png")