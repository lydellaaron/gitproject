import time
import sys

def custom_progress_bar(total_steps):
    for i in range(total_steps + 1):
        progress = (i / total_steps) * 100
        sys.stdout.write("\r[{:<50}] {:.1f}%".format("=" * int(progress / 2), progress))
        sys.stdout.flush()
        time.sleep(0.5)  # Simulating work

total_steps = 10
custom_progress_bar(total_steps)
print("\nTask complete!")
