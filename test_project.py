import pytest
from project import getUserInformation, getPdfName, getCourseInformation
from unittest.mock import patch 

def test_getUserInformation_valid(monkeypatch):
    inputs = iter(["Enzo", "Quatrochi", "123456789"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    first, last, doc, date, hour = getUserInformation()

    assert first == "Enzo"
    assert last == "Quatrochi"
    assert doc == "123456789"

def test_getUserInformation_retry_invalid(monkeypatch): 
    inputs = iter(["Enz0", "", "", "Enzo", "Q", "", "Quat@ochi", "", "", "Enzo", "Quatrochi", "abc123"]); 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)); 

    first, last, doc, date, hour = getUserInformation(); 

    assert first == "Enzo"; 
    assert last == "Quatrochi"; 
    assert doc == "abc123"

def test_getPdfName_valid(monkeypatch):
    test_pdf_name = "c-espaco.pdf"
    monkeypatch.setattr("builtins.input", lambda _: test_pdf_name)
    with patch("os.path.exists", return_value=True):
        assert getPdfName() == test_pdf_name

def test_getPdfName_invalid_extension(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "arquivo.txt")
    with pytest.raises(ValueError):
        getPdfName()

def test_getPdfName_file_not_found(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "arquivo.pdf")
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            getPdfName()

def test_get_course_information_valid_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")  
    assert getCourseInformation() == "CS50P - Introduction to Programming with Python"

def test_get_course_information_valid_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")  
    assert getCourseInformation() == "CS50W - Web Programming with Python and JavaScript"

def test_get_course_information_valid_3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")  
    assert getCourseInformation() == "CS50AI - Introduction to Artificial Intelligence with Python"

def test_get_course_information_valid_4(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")  
    assert getCourseInformation() == "CS50SQL - Introduction to Databases with SQL"

def test_get_course_information_valid_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")  
    assert getCourseInformation() == "CS50C - Introduction to Cybersecurity"

def test_get_course_information_valid_6(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "6")  
    assert getCourseInformation() == "CS50X - Introduction to Computer Science"