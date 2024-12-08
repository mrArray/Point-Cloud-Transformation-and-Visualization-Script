
# Name : Nura Dahiru Musa
#  Student ID:  2415066021	
#  University:  Wuhan Textile University,
#  Faculty :  School of Computer Science and Artificial Intelligence
#  Major:  Computer Science and Technology
#  Submission Date:  07-12-2024


import open3d as o3d
import numpy as np


def loadVisualizePointC(modelFilePath):
    """
    Loads and visualizes a point cloud from the given file path.
    :param modelFilePath: Path to the .ply or .pcd file
    """
    print(f"Loading point cloud from: {modelFilePath}")
    pcd = o3d.io.read_point_cloud(modelFilePath)  # Load the point cloud
    if pcd.is_empty():
        print("Error: Failed to load the point cloud or file is empty.")
    else:
        print("Point cloud loaded successfully.")
    
    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

def RotatePointC(pcd, angle_degrees, axis):
    """
    Rotates a given point cloud by the specified angle about a defined axis.
    :param pcd: The point cloud to rotate.
    :param angle_degrees: The rotation angle in degrees.
    :param axis: Axis of rotation ('x', 'y', or 'z').
    """
    print(f"Rotating the point cloud by {angle_degrees} degrees about the {axis}-axis")
    
    angle_radians = np.radians(angle_degrees)  # Convert degrees to radians
    if axis == 'x':
        R = pcd.get_rotation_matrix_from_xyz((angle_radians, 0, 0))
    elif axis == 'y':
        R = pcd.get_rotation_matrix_from_xyz((0, angle_radians, 0))
    elif axis == 'z':
        R = pcd.get_rotation_matrix_from_xyz((0, 0, angle_radians))
    else:
        raise ValueError("Invalid axis! Use 'x', 'y', or 'z'.")
    
    pcd.rotate(R, center=pcd.get_center())
    print("Rotation applied successfully.")

def ScalePointC(pcd, scale_factor):
    """
    Scales the point cloud uniformly.
    :param pcd: The point cloud to scale.
    :param scale_factor: Scaling factor.
    """
    print(f"Scaling the point cloud by a factor of: {scale_factor}")
    pcd.scale(scale_factor, center=pcd.get_center())
    print("Scaling applied successfully.")

def translatePointC(pcd, translation_vector):
    """
    Translates the point cloud by a specified vector.
    :param pcd: The point cloud to translate.
    :param translation_vector: Vector to translate the point cloud (x, y, z).
    """
    print(f"Translating the point cloud with vector: {translation_vector}")
    pcd.translate(translation_vector)
    print("Translation applied successfully.")


#Main execution
if __name__ == "__main__":
    # Replace with your actual file path
    modelFilePath = "models/Car body.ply"
    
    # Load and visualize initial point cloud
    loadVisualizePointC(modelFilePath)

    # Ensure point cloud is loaded before applying transformations
    point_cloud = o3d.io.read_point_cloud(modelFilePath)
    
    # Check if point cloud loaded correctly
    if not point_cloud.is_empty():
        # Apply transformations
        RotatePointC(point_cloud, angle_degrees=30, axis='z')
        ScalePointC(point_cloud, scale_factor=1.5)
        translatePointC(point_cloud, translation_vector=np.array([0.5, 0.5, 0]))
        
        # Visualize after transformations
        print("\nVisualizing the transformed point cloud...")
        o3d.visualization.draw_geometries([point_cloud])
    else:
        print("Failed to load the point cloud. Exiting.")
