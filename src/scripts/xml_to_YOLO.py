import os
import xml.etree.ElementTree as ET
import random
from PIL import Image

# Define the paths to your image and annotation folders
path_images = "/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/image02"
path_annotations = "/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/annotation"

# Create the "annotations" directory if it doesn't exist
output_annotations_dir = "/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/yolo"
os.makedirs(output_annotations_dir, exist_ok=True)

# Function to get the data from XML Annotation
def extract_info_from_xml(xml_file):
    root = ET.parse(xml_file).getroot()
    info_dict = {}
    info_dict['bboxes'] = []

    for elem in root:
        if elem.tag == "filename":
            info_dict['filename'] = elem.text
        elif elem.tag == "size":
            image_size = [int(subelem.text) for subelem in elem]
            info_dict['image_size'] = tuple(image_size)
        elif elem.tag == "object":
            bbox = {}
            for subelem in elem:
                if subelem.tag == "name":
                    bbox["class"] = subelem.text
                elif subelem.tag == "bndbox":
                    for subsubelem in subelem:
                        bbox[subsubelem.tag] = int(subsubelem.text)
            info_dict['bboxes'].append(bbox)
    
    return info_dict

# List of class names
class_names = ["APAL", "Pseudodiploria"]

# Convert the info dict to the required YOLO format and write it to disk
def convert_to_yolov5(info_dict):
    print_buffer = []

    for b in info_dict["bboxes"]:
        try:
            class_name = b["class"]
            if class_name not in class_names:
                raise KeyError("Invalid Class. Must be one from ", class_names)
            class_id = class_names.index(class_name)
        except KeyError as e:
            print(e)
            continue  # Skip this bounding box if the class is invalid
        
        # Map class names to numeric IDs
        if class_name == "APAL":
            class_id = 0
        elif class_name == "Pseudodiploria":
            class_id = 1
            
        b_center_x = (b["xmin"] + b["xmax"] - 1) / 2
        b_center_y = (b["ymin"] + b["ymax"] - 1) / 2
        b_width = (b["xmax"] - b["xmin"])
        b_height = (b["ymax"] - b["ymin"])

        image_w, image_h, _ = info_dict["image_size"]
        b_center_x /= image_w
        b_center_y /= image_h
        b_width /= image_w
        b_height /= image_h

        print_buffer.append("{} {:.3f} {:.3f} {:.3f} {:.3f}".format(class_id, b_center_x, b_center_y, b_width, b_height))

    save_file_name = os.path.join(output_annotations_dir, info_dict["filename"].replace("jpg", "txt").replace("JPG", "txt"))

    with open(save_file_name, "w") as file:
        file.write("\n".join(print_buffer))

# Get the annotations
annotations = [os.path.join(path_annotations, x) for x in os.listdir(path_annotations) if x.endswith(".xml")]
annotations.sort()

# Convert and save the annotations
for ann in annotations:
    info_dict = extract_info_from_xml(ann)
    convert_to_yolov5(info_dict)
