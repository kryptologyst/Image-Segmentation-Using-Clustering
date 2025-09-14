import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from image_segmenter import segment_image

class ImageSegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Segmentation Tool")

        self.image_path = None
        self.original_image = None
        self.segmented_image = None

        # Create main frame
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Controls Frame ---
        controls_frame = tk.Frame(main_frame)
        controls_frame.pack(fill=tk.X, pady=5)

        self.btn_load = tk.Button(controls_frame, text="Load Image", command=self.load_image)
        self.btn_load.pack(side=tk.LEFT, padx=5)

        self.k_slider = tk.Scale(controls_frame, from_=2, to_=16, orient=tk.HORIZONTAL, label="Clusters (K)", length=200)
        self.k_slider.set(4)
        self.k_slider.pack(side=tk.LEFT, padx=5)
        self.k_slider.bind("<ButtonRelease-1>", self.apply_segmentation)

        self.btn_save = tk.Button(controls_frame, text="Save Segmented Image", command=self.save_image, state=tk.DISABLED)
        self.btn_save.pack(side=tk.RIGHT, padx=5)

        # --- Image Display Frame ---
        image_frame = tk.Frame(main_frame)
        image_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.panel_original = tk.Label(image_frame, text="Original Image", relief=tk.SUNKEN, borderwidth=1)
        self.panel_original.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.panel_segmented = tk.Label(image_frame, text="Segmented Image", relief=tk.SUNKEN, borderwidth=1)
        self.panel_segmented.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            self.image_path = path
            self.apply_segmentation()

    def apply_segmentation(self, event=None):
        if not self.image_path:
            return

        k = self.k_slider.get()
        original, segmented = segment_image(self.image_path, k)

        if original is not None and segmented is not None:
            self.original_image = original
            self.segmented_image = segmented
            self.display_images()
            self.btn_save.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Failed to segment the image.")

    def display_images(self):
        # Display original image
        img_orig = Image.fromarray(self.original_image)
        img_orig.thumbnail((400, 400))
        self.photo_orig = ImageTk.PhotoImage(img_orig)
        self.panel_original.config(image=self.photo_orig)

        # Display segmented image
        img_seg = Image.fromarray(self.segmented_image)
        img_seg.thumbnail((400, 400))
        self.photo_seg = ImageTk.PhotoImage(img_seg)
        self.panel_segmented.config(image=self.photo_seg)

    def save_image(self):
        if self.segmented_image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg")])
            if save_path:
                try:
                    # Convert from RGB (Pillow) to BGR (OpenCV) for saving
                    img_to_save = cv2.cvtColor(self.segmented_image, cv2.COLOR_RGB2BGR)
                    cv2.imwrite(save_path, img_to_save)
                    messagebox.showinfo("Success", f"Image saved to {save_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSegmentationApp(root)
    root.mainloop()
