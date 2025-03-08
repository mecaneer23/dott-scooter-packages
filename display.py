from calculate import Package

dott = [
    Package(16, 0, 1),
    Package(18, 0, 0, 2),
    Package(19, 9, 0),
    Package(45, 6, 0),
    Package(79, 0, 0, 10),
    Package(0, 6, 1),
]

import numpy as np
import plotly.graph_objects as go

# Define x and z ranges
x_values = np.arange(1, 101)  # X from 1 to 100
z_values = np.arange(1, 101, 10)  # Z from 1 to 100 (step 10 for clarity)

# Create an empty figure
fig = go.Figure()

# Iterate over each cls object in dott
for idx, obj in enumerate(dott):
    for z in z_values:
        y_values = [obj.get_price(int(x), int(z)) for x in x_values]  # Compute Y for varying Z

        # Add a line for this function at this Z level
        fig.add_trace(go.Scatter3d(
            x=x_values, 
            y=[z] * len(x_values),  # Different Z levels
            z=y_values,
            mode='lines',
            name=f'obj: {obj}, z={z}',
            line=dict(color=f'hsl({idx * 360 / len(dott)}, 100%, 50%)', width=2)  # Unique color
        ))

# Update layout for better visualization
fig.update_layout(
    title="Interactive 3D Plot of get_price(x, z)",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Z",
        zaxis_title="Y (Price)"
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Show the interactive plot
fig.show()
