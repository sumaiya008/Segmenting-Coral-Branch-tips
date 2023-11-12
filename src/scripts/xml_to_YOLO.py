import xml.etree.ElementTree as ET
import os

def convert_annotation(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    yolo_lines = []
    image_width = int(root.find('.//size/width').text)
    image_height = int(root.find('.//size/height').text)

    for obj in root.iter('object'):
        class_name = obj.find('name').text
        # Replace class_id with the actual class index for each class
        class_id = 0  # Change this based on your class mapping

        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        ymin = float(bbox.find('ymin').text)
        xmax = float(bbox.find('xmax').text)
        ymax = float(bbox.find('ymax').text)

        x_center = (xmin + xmax) / (2.0 * image_width)
        y_center = (ymin + ymax) / (2.0 * image_height)
        box_width = (xmax - xmin) / image_width
        box_height = (ymax - ymin) / image_height

        yolo_lines.append(f"{class_id} {x_center} {y_center} {box_width} {box_height}")

    return yolo_lines

def main():
    xml_folder = "/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/annotation"
    yolo_folder = "/Users/sumaiyauddin/Documents/Semester03/CCNY-DSE-Capstone-Project-Segmenting-Coral-Branch-tips/data/external/Coral_images/yolo"

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(xml_folder, xml_file)
            yolo_lines = convert_annotation(xml_path)

            yolo_file = os.path.join(yolo_folder, os.path.splitext(xml_file)[0] + ".txt")
            with open(yolo_file, "w") as f:
                for line in yolo_lines:
                    f.write(line + "\n")

if __name__ == "__main__":
    main()


