# CS50 Digital Signature
#### Video Demo:  <https://youtu.be/KfagMMqqT4Y>
#### Description:

The objective of this program is to make a digital signature in PDF files and validate them with the CS50 course signature.

The main condition is that the signature can't overlap the content of the PDF, so one needs to find a way to put the signature at the end of the content.

With this requirement, there are two problems to solve: the first is that the PDF content takes up almost all the space on the last page, and the signature needs to be on a new page to avoid overlapping the content. The second is that the content on the last page takes up part of the space, but there's room for the signature to be inserted.

The signature consists of student information such as first name, last name and a document, the hour, minute and second the signature was issued, and the name and logo of the course.

The signature is first created as an image before being displayed, and then it is calculated, based on the size of the content of the last page, whether it fits on the page or not.

The student's information is validated with a request so that it does not contain numbers, spaces, symbols, or unique characters.

Course selection is done through manual selection, where the user selects the number of the course they want to be displayed, avoiding typing errors on the part of the user.

In the PDF selection, the program restricts files only to PDFs using a validation so that the user does not insert other file types.

When placed, the code generates another PDF with the PDF name + signed to preserve the initial version of the file.

All this logic and functionality is in the program.py file, which is the soul of the project. The project also needs the logo image that will be displayed with the signature (CS50 course logos).

The file test_program.py is responsible for testing all functions used by the program to ensure its correct operation. They are: getUserInformation, getCourseInformation, createSignatureImage, getPdfName, and generateNewSignedPdf. Since most of these functions depend on input, it is necessary to mock their information to test them, and we do this using monkeypatch.

Some of these functions cannot be tested, but all possible functions are tested with all validations to ensure no exceptions occur during use.

#### Installation:
To run the program, you need to download all the libraries from the requirements.txt file using pip. You also need to download all the images from the CS50 course and place them in the assets folder. Finally, you need to place the PDF files that will be signed in the main folder at the same level as the program.

1. Clone the repository.
2. Download all CS50 images:

   - [Download CS50P Logo](CS50P.png)
   - [Download CS50X Logo](CS50X.png)
   - [Download CS50AI Logo](CS50AI.png)
   - [Download CS50W Logo](CS50W.png)
   - [Download CS50SQL Logo](CS50SQL.png)
   - [Download CS50C Logo](CS50C.png)

3. Insert images into the assets folder.
4. Download the requirements:

```
pip install -r requirements.txt
```

> [!WARNING]
> It is possible that the font may cause problems based on the operating system used.

#### How to run the program:

Run:

```
python program.py
```
