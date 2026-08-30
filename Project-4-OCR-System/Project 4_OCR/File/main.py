import cv2
import pytesseract
import os
import glob

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_folder = "Project 4_OCR/Images"
confidence_limit = 80

images = []

for file in glob.glob(image_folder + "/*"):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        images.append(file)

for image_path in images:

    print("\nProcessing:", os.path.basename(image_path))

    image = cv2.imread(image_path)

    if image is None:
        print("Could not load image")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    processed = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    output_name = "processed_" + os.path.basename(image_path)
    output_path = os.path.join(image_folder, output_name)

    cv2.imwrite(output_path, processed)

    data = pytesseract.image_to_data(
        processed,
        output_type=pytesseract.Output.DICT
    )

    words = []
    confidence_values = []

    for i in range(len(data["text"])):

        text = data["text"][i].strip()

        try:
            confidence = float(data["conf"][i])
        except ValueError:
            continue

        if text and confidence >= 0:
            words.append(text)
            confidence_values.append(confidence)

    print("Recognized Text:")
    print(" ".join(words))

    if confidence_values:

        average = sum(confidence_values) / len(confidence_values)

        print(f"Confidence: {average:.2f}%")

        if average >= confidence_limit:
            print("STATUS: PASS")
        else:
            print("STATUS: LOW CONFIDENCE")
    else:
        print("No text recognized.")

print("\nAll images processed.")