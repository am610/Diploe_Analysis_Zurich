import pandas as pd
import numpy as np

# Step 1: Read the files (assuming space-separated values)
file1 = pd.read_csv(
    "FITOPT000_MUOPT000.FITRES", sep="\s+", comment="#"
)  # Contains CID, HOST_RA, HOST_DEC
file2 = pd.read_csv(
    "hubble_diagram.txt", sep="\s+", comment="#"
)  # Contains CID and other columns

print("Shape of FITOPT ", np.shape(file1))
print("Shape of HD     ", np.shape(file2))


# Step 2: Perform a left merge based on 'CID'
merged_df = pd.merge(file2, file1[["CID", "HOST_RA", "HOST_DEC"]], on="CID", how="left")

print("Shape of MERGED ", np.shape(merged_df))


# Step 3: Fill missing values in HOST_RA and HOST_DEC with 'xx'
# merged_df['HOST_RA'].fillna('xx', inplace=True)
# merged_df['HOST_DEC'].fillna('xx', inplace=True)

# Step 4: Save the result to a new file (you can overwrite hubble_diagram.txt if needed)
merged_df.to_csv("output_hubble_diagram.txt", sep=" ", index=False)

print("Data merged and saved to output_hubble_diagram.txt")
