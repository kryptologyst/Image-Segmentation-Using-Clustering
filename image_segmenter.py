import cv2
import numpy as np
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore', category=RuntimeWarning)

def segment_image(image_path, k):
    """Loads an image, performs K-Means clustering, and returns the segmented image."""
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Image not found at {image_path}")
            return None, None
        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_shape = image_rgb.shape

        pixel_data = image_rgb.reshape((-1, 3)).astype(np.float32) / 255.0

        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(pixel_data)

        segmented_colors = kmeans.cluster_centers_ * 255.0
        segmented_img_data = segmented_colors[kmeans.labels_]

        segmented_img = segmented_img_data.reshape(original_shape).astype(np.uint8)
        
        return image_rgb, segmented_img

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
