# Image Segmentation using K-Means Clustering

This project demonstrates image segmentation using K-Means clustering to group pixels based on color similarity. The application simplifies an image by reducing its color palette to a specified number of dominant colors (K).

It includes both a command-line script for quick segmentation and a graphical user interface (GUI) for a more interactive experience.

## Features

- **K-Means Clustering**: Segments images by color into K clusters.
- **Command-Line Interface**: Run segmentation directly from the terminal.
- **Graphical User Interface**: An easy-to-use interface to load images, adjust K, and save results.
- **Modular Code**: The core segmentation logic is separated from the user interfaces.

## Project Structure

```
.
├── 0051.py                # Command-line script for segmentation
├── gui.py                 # GUI application for interactive segmentation
├── image_segmenter.py     # Core image segmentation logic
├── sample_image.jpg       # A sample image to test the application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files to be ignored by Git
```

## Setup

1.  **Clone the repository** (or download the source code).

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the application in two ways:

### 1. Graphical User Interface (GUI)

To launch the interactive GUI, run:

```bash
python3 gui.py
```

**GUI Features**:
- **Load Image**: Open an image file from your computer.
- **Clusters (K) Slider**: Adjust the number of color clusters in real-time.
- **Save Segmented Image**: Save the resulting image to your computer.

### 2. Command-Line Interface

To use the command-line script, run `0051.py` with the following arguments:

```bash
python3 0051.py [image_path] [-k K]
```

- `image_path` (optional): Path to the input image. Defaults to `sample_image.jpg`.
- `-k K` (optional): The number of clusters (K). Defaults to `4`.

**Examples**:

- Run with the default sample image and K=4:
  ```bash
  python3 0051.py
  ```

- Run with a custom image and K=8:
  ```bash
  python3 0051.py /path/to/your/image.jpg -k 8
  ```
