from fpdf import FPDF
from datetime import datetime
import fitz
from PIL import Image, ImageDraw, ImageFont
import re
import os


class PDF(FPDF):
    def __init__(self):
        super().__init__()


def createSignatureImage(first, last, doc, date, hour, course):
    img = Image.new("RGB", (800, 190), "white")
    draw = ImageDraw.Draw(img)

    courseImageName = course.split(" - ")[0]

    logo = Image.open(f"assets/{courseImageName}.png").convert("RGBA")
    logo.thumbnail((140, 140))

    img.paste(logo, (10, 20), logo)

    font = ImageFont.truetype("arial.ttf", 18) 

    draw.text((160, 25), f"{course}", font=font, fill="black")
    draw.text((160, 50), f"{first} {last} - {doc}", font=font, fill="black")
    draw.text((160, 75), f"Signed on: {date} - {hour}", font=font, fill="black")

    img.save("signature.png")


def getUserInformation():
    while True:
        firstName = input("Enter your first name: ").strip().capitalize()
        if not firstName:
            print("First name cannot be empty")
            continue

        if not re.match(r"^[A-Za-z].*[A-Za-z]$", firstName):
            print("First name invalid")
            continue

        lastName = input("Enter your last name: ").strip().capitalize()
        if not lastName:
            print("Last name cannot be empty")
            continue

        if not re.match(r"^[A-Za-z].*[A-Za-z]$", lastName):
            print("Last name invalid")
            continue

        document = input("Enter your document: ").strip()
        if not re.match(r"^[A-Za-z0-9].*[A-Za-z0-9]$", document):
            print("Document cannot be empty.")
            continue

        break

    date = datetime.now().strftime("%d/%m/%Y")
    hour = datetime.now().strftime("%H:%M:%S")

    return firstName, lastName, document, date, hour


def getCourseInformation():

    switch = {
        "1": "CS50P - Introduction to Programming with Python",
        "2": "CS50W - Web Programming with Python and JavaScript",
        "3": "CS50AI - Introduction to Artificial Intelligence with Python",
        "4": "CS50SQL - Introduction to Databases with SQL",
        "5": "CS50C - Introduction to Cybersecurity",
        "6": "CS50X - Introduction to Computer Science"
    }

    while True:
        print("\nSelect the CS50 course:")
        print("1 - CS50P")
        print("2 - CS50W")
        print("3 - CS50AI")
        print("4 - CS50SQL")
        print("5 - CS50C")
        print("6 - CS50X")

        choice = input("\nEnter the number of the course: ").strip()

        if choice in switch:
            return switch[choice]
        
        else:
            print("\nInvalid option. Please try again.")


def getPdfName():
    pdfName = input("\nEnter the pdf file: ").lower()

    if not pdfName.endswith(".pdf"):
        raise ValueError("Not a pdf file")

    if not os.path.exists(pdfName):
        raise FileNotFoundError("File not found")

    return pdfName


def generateNewSignedPdf():
    pdfName = getPdfName()
    outputName = f"signed {pdfName}"

    doc = fitz.open(pdfName)
    page = doc[-1]
    text = page.get_text()
    lines = len(text.splitlines()) if text else 0

    if len(doc) == 1 or lines > 30:
        doc.insert_page(-1)
        sig_page = doc[-1]
        rect = fitz.Rect(100, 60, 560, 180)
        sig_page.insert_image(rect, filename="signature.png")
    else:
        rect = fitz.Rect(100, 730, 560, 850)
        page.insert_image(rect, filename="signature.png")

    doc.save(outputName, deflate=True, garbage=4)
    doc.close()

    os.remove("signature.png")
    print("\nDocument assigned")


def main():
    print("\nWelcome to CS50P signature generator\n")
    first, last, doc, date, hour = getUserInformation()
    course = getCourseInformation()
    createSignatureImage(first, last, doc, date, hour, course)
    generateNewSignedPdf()


if __name__ == "__main__":
    main()
