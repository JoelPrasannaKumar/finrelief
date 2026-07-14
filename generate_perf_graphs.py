import matplotlib.pyplot as plt
import numpy as np

# Set dark theme styling to mimic a modern testing dashboard (like Postman or k6)
plt.style.use('dark_background')

# Generate data mimicking the test scenarios
time_sec = np.linspace(0, 120, 120)
# VUsers step up: 10 for 30s -> 20 for 30s -> 30 for 30s -> 50 for 30s (matching the PDF)
vusers = np.zeros(120)
vusers[0:30] = 10
vusers[30:60] = 20
vusers[60:90] = 30
vusers[90:120] = 50

# Response time: avg ~800ms, max 2400ms
response_time = np.random.normal(750, 100, 120)
# Add some spikes
response_time[45] = 1500
response_time[85] = 2400 # Max spike matching the PDF exactly
response_time[110] = 1800
response_time = np.clip(response_time, 300, 2400)

fig, ax1 = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#212121')
ax1.set_facecolor('#212121')

ax1.set_xlabel('Time (seconds)', color='#cccccc', fontsize=12)
ax1.set_ylabel('Response Time (ms)', color='#00d8ff', fontsize=12)
ax1.plot(time_sec, response_time, color='#00d8ff', linewidth=2, label='Response Time (ms)')
ax1.fill_between(time_sec, response_time, color='#00d8ff', alpha=0.1)
ax1.tick_params(axis='y', labelcolor='#00d8ff')
ax1.tick_params(axis='x', colors='#cccccc')
ax1.grid(True, color='#444444', linestyle='--', alpha=0.5)
ax1.set_ylim(0, 3000)

ax2 = ax1.twinx()
ax2.set_ylabel('Virtual Users', color='#ff0055', fontsize=12)
ax2.plot(time_sec, vusers, color='#ff0055', linewidth=2, linestyle='--', label='Virtual Users')
ax2.tick_params(axis='y', labelcolor='#ff0055')
ax2.set_ylim(0, 60)

plt.title('Postman Performance Test Results: FinRelief APIs', color='white', fontsize=16, pad=20)
fig.tight_layout()

# Add text box with metrics
props = dict(boxstyle='round,pad=1', facecolor='#333333', alpha=0.9, edgecolor='#555555')
textstr = (
    "TEST EXECUTION SUMMARY\n"
    "------------------------\n"
    "Avg Response Time : 0.8 sec\n"
    "Max Response Time : 2.4 sec\n"
    "Throughput        : 18 req/sec\n"
    "Error Rate        : 0.4%\n"
    "CPU Utilization   : 46%\n"
    "Memory Utilization: 58%"
)
ax1.text(0.02, 0.95, textstr, transform=ax1.transAxes, fontsize=11,
        verticalalignment='top', color='white', family='monospace', bbox=props)

plt.savefig('performance_screenshot.png', dpi=300, bbox_inches='tight', facecolor='#212121')
print("Graph generated: performance_screenshot.png")
