import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Data extracted from mandelbrot.txt
nodes = [1, 2, 4, 8]
runtimes = [12.9433, 7.40265, 5.78687, 3.45724]
speedups = [50.41295496511709, 88.14546142259866, 112.75698261754626, 188.73725862248497]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Runtime plot
axes[0].plot(nodes, runtimes, marker='o')
axes[0].set_title('Runtime vs. Number of Nodes')
axes[0].set_xlabel('Number of Nodes')
axes[0].set_ylabel('Runtime (seconds)')
axes[0].grid(True)

# Speedup plot
axes[1].plot(nodes, speedups, marker='o', color='green')
axes[1].set_title('Speedup vs. Number of Nodes')
axes[1].set_xlabel('Number of Nodes')
axes[1].set_ylabel('Speedup (x)')
axes[1].grid(True)

plt.tight_layout()
plt.savefig('mandelbrot_performance.png')
print('Plot saved to mandelbrot_performance.png') 