import trimesh
import pandas as pd

# Load STL file from local path
mesh = trimesh.load_mesh('trimesh-main/models/featuretype.STL')

# Extract info
info = {
    'Number of Vertices': [len(mesh.vertices)],
    'Number of Faces': [len(mesh.faces)],
    'Volume': [mesh.volume],
    'Moment of Inertia': [mesh.moment_inertia.tolist()],
    'Bounding Box': [mesh.bounding_box.extents.tolist()],
    'Maximum Thickness (Z-axis)': [mesh.bounding_box.extents[2]]
}

# Convert to DataFrame
df = pd.DataFrame(info)

# Save as CSV and Excel
df.to_csv('stl_analysis.csv', index=False)
df.to_excel('stl_analysis.xlsx', index=False)  # Make sure openpyxl is installed

print("STL analysis completed and exported!")
print("1. Number of Vertices:", len(mesh.vertices))
print("2. Number of Faces:", len(mesh.faces))
print("3. Volume:", mesh.volume)
print("   Moment of Inertia:\n", mesh.moment_inertia)
print("4. Bounding Box (X, Y, Z):", mesh.bounding_box.extents)
print("5. Maximum Thickness (Z-axis):", mesh.bounding_box.extents[2])



