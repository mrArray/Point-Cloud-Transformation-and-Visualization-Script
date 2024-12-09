
# Point Cloud Transformation and Visualization Script

This repository contains a Python script for loading, visualizing, and applying transformations to point cloud data using the Open3D library. The script demonstrates key operations like rotation, scaling, and translation on 3D point cloud data.

## Features

1. **Load and Visualize Point Cloud**: Supports `.ply` or `.pcd` file formats for point cloud data.
2. **Apply Transformations**:
   - **Rotation**: Rotate point cloud around the x, y, or z axis.
   - **Scaling**: Scale point cloud uniformly by a specified factor.
   - **Translation**: Translate point cloud along a specified vector.

## Requirements

- Python 3.6+
- Open3D
- NumPy

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrArray/Point-Cloud-Transformation-and-Visualization-Script
   cd point-cloud-transformation
   ```
2. Install the required dependencies:
   ```bash
   pip install open3d numpy
   ```

## Usage

1. Replace `modelFilePath` in the script with the path to your `.ply` or `.pcd` file:
   ```python
   modelFilePath = "path/to/your/pointcloud.ply"
   ```
2. Run the script:
   ```bash
   python main.py
   ```

3. The script performs the following steps:
   - Loads and visualizes the initial point cloud.
   - Applies the following transformations:
     - Rotates the point cloud 30 degrees about the z-axis.
     - Scales the point cloud by a factor of 1.5.
     - Translates the point cloud by `[0.5, 0.5, 0]`.
   - Visualizes the transformed point cloud.

## Functions

### `loadVisualizePointC(modelFilePath)`
Loads and visualizes a point cloud from the given file path.

### `RotatePointC(pcd, angle_degrees, axis)`
Rotates a given point cloud by the specified angle about the defined axis.

### `ScalePointC(pcd, scale_factor)`
Scales the point cloud uniformly by the given factor.

### `translatePointC(pcd, translation_vector)`
Translates the point cloud by a specified vector.

## Example Input File
The script supports `.ply` or `.pcd` files. Make sure the file exists and is correctly formatted.

## Acknowledgments
This project is developed by **Nura Dahiru Musa**, a Computer Science and Technology major at Wuhan Textile University, as part of an academic submission.

- **Student ID**: 2415066021
- **Faculty**: School of Computer Science and Artificial Intelligence
- **Submission Date**: December 7, 2024

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
