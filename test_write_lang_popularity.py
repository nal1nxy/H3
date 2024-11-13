"""
File: test_wirte_lang_popularity.py
Developers: Nalin Yetukuri
Date: 11/10/2024
"""

import pytest
from analysis import Analysis


def test_write_lang_popularity_10():
    """
    Test the method by giving devops10.csv file as input to the Analysis class
    """
    test_file = "./devops10.csv"
    a_obj = Analysis(test_file)
    a_obj.write_lang_popularity()
    with open("pop.csv", encoding="utf-8", mode="r") as f:
        actual = f.readlines()
        expected = [
                'Frequency,Language\n',
                '2,Bash/Shell (all shells);Lua\n',
                '1,Go;C#;PowerShell;SQL;C++;Swift;R\n',
                '5,HTML/CSS;JavaScript\n',
                '3,Java\n',
                '4,Python;TypeScript\n'
            ]
        print(actual)
        print(expected)
        assert actual == expected


def test_write_lang_popularity_1():
    """
    Test the method by giving devops1.csv file as input to the Analysis class
    """
    test_file = "./devops1.csv"
    a_obj = Analysis(test_file)
    a_obj.write_lang_popularity()
    with open("pop.csv", encoding="utf-8", mode="r") as f:
        actual = f.readlines()
        expected = ["Frequency,Language\n", "1,Assembly;C#;C++;SQL\n"]
        print(actual)
        print(expected)
        assert actual == expected


def test_write_lang_popularity_5():
    """
    Test the method by giving devops5.csv file as input to the Analysis class
    """
    test_file = "./devops5.csv"
    a_obj = Analysis(test_file)
    a_obj.write_lang_popularity()
    with open("pop.csv", encoding="utf-8", mode="r") as f:
        actual = f.readlines()
        expected = [
            "Frequency,Language\n",
            "3,C#;SQL\n",
            "2,C++;Bash/Shell (all shells)\n",
            "1,HTML/CSS;Java;JavaScript;Python;Go;Assembly;C;\n"
            "MATLAB;PowerShell\n",
        ]
        print(actual)
        print(expected)
        assert actual == expected


pytest.main()
