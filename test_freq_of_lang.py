"""
File: test_freq_of_lang.py
Developers: Nalin Yetukuri
Date: 11/10/2024
"""

import pytest
from analysis import Analysis


def test_freq_of_lang_10():
    """
    Test the method by giving devops10.csv file as input to the Analysis class
    """
    test_file = "./devops10.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.freq_of_lang()
    expected = {
        "Bash/Shell (all shells)": 2,
        "Go": 1,
        "HTML/CSS": 5,
        "Java": 3,
        "JavaScript": 5,
        "Python": 4,
        "TypeScript": 4,
        "C#": 1,
        "PowerShell": 1,
        "SQL": 1,
        "C++": 1,
        "Lua": 2,
        "Swift": 1,
        "R": 1,
    }
    assert actual == expected


def test_freq_of_lang_1():
    """
    Test the method by giving devops1.csv file as input to the Analysis class
    """
    test_file = "./devops1.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.freq_of_lang()
    expected = {"Assembly": 1, "C#": 1, "C++": 1, "SQL": 1}
    assert actual == expected


def test_freq_of_lang_5():
    """
    Test the method by giving devops5.csv file as input to the Analysis class
    """
    test_file = "./devops5.csv"
    a_obj = Analysis(test_file)
    actual = a_obj.freq_of_lang()
    expected = {
        "C#": 3,
        "C++": 2,
        "HTML/CSS": 1,
        "Java": 1,
        "JavaScript": 1,
        "Python": 1,
        "Bash/Shell (all shells)": 2,
        "Go": 1,
        "SQL": 3,
        "Assembly": 1,
        "C": 1,
        "MATLAB": 1,
        "PowerShell": 1,
    }
    assert actual == expected


pytest.main()
