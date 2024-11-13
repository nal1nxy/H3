"""
File: test_lang_histogram.py
Developers: Nalin Yetukuri
Date: 11/10/2024
"""
import pytest
from analysis import Analysis


def test_lang_histogram_10():
    """
    Test the method by giving devops10.csv file as input to the Analysis class
    """
    test_file = "./devops10.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.lang_histogram()
    expected = {
        2: ['Bash/Shell (all shells)', 'Lua'],
        1: ['Go', 'C#', 'PowerShell', 'SQL', 'C++', 'Swift', 'R'],
        5: ['HTML/CSS', 'JavaScript'],
        3: ['Java'],
        4: ['Python', 'TypeScript']
        }
    assert actual == expected


def test_lang_histogram_1():
    """
    Test the method by giving devops1.csv file as input to the Analysis class
    """
    test_file = "./devops1.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.lang_histogram()
    expected = {1: ['Assembly', 'C#', 'C++', 'SQL']}
    assert actual == expected


def test_lang_histogram_5():
    """
    Test the method by giving devops5.csv file as input to the Analysis class
    """
    test_file = "./devops5.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.lang_histogram()
    expected = {
        3: ["C#", "SQL"],
        2: ["C++", "Bash/Shell (all shells)"],
        1: [
            "HTML/CSS",
            "Java",
            "JavaScript",
            "Python",
            "Go",
            "Assembly",
            "C",
            "MATLAB",
            "PowerShell",
        ],
    }
    assert actual == expected


pytest.main()
