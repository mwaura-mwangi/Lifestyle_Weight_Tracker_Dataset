import os
import numpy as np
import pandas as pd
import dtale
import time

# Load the data
df = pd.read_csv("lifestyle weight tracker.csv")

# Start D-Tale on localhost to avoid "Site can't be reached"
d = dtale.show(df, host='localhost')

# Open the browser
d.open_browser()

print(f"Server is running at: {d.main_url}")
print("Check your browser! Press Ctrl+C in this terminal to exit.")

# avoid browser window breaking
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping the data viewer...")
