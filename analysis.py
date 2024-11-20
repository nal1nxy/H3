"""
Practice with classes, files, and nested structures.

File: analysis.py
Initial developers: COMP 801 instructors
Data source: https://insights.stackoverflow.com/survey
Developer:Nalin Yetukuri
Date: 11/10/2024
"""

import csv


class Analysis:
    """
    Analyze developer data from the Stack Overflow 2024 survey.
    """
    def __init__(self, file_path):
        """
        Initialize instance variable `self.devs` list with dictionary objects.
        A dictionary object has:
            keys: strings from the fields in the 1st row of the CSV file
            values: strings with information corresponding to the keys

        :param file_path: str, path of CSV file, relative to `analysis.py`
            module. The file has a heading 1st row, followed by rows that have
            data about developers collected by 2024 Stach Overflow survey
            hhttps://survey.stackoverflow.co/2024:
                one respondent per row and one column per answer.
        :return: Analysis object
        """
        self.devs = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=',', quotechar='"'
                )
                self.devs = list(csv_reader)
        except IOError as err:
            print(err)

    def __str__(self):
        """
        Returns string representation of the list `self.devs`. The elements
        of the list are dictionaries. Each dictionary corresponds to a row
        in the text file located at `file_path`.
        """
        return self.devs

    def freq_of_lang(self):
        """
        Count the frequency of each programming language in the `self.devs`
        list of dictionaries. The programming language is the value of the
        key 'LanguageWorkedWith'.

        :return: dict, keys are programming languages, values are the number of
            times the language appears in the `self.devs` list
        """

        language_freq = {}
        for dictionary in self.devs:
            language = dictionary["LanguageAdmired"]
            lang_list = language.split(";")
            for lang in lang_list:
                if lang != "NA":
                    if lang not in language_freq:
                        language_freq[lang] = 0
                    language_freq[lang] = language_freq[lang] + 1
        return language_freq

    def lang_histogram(self):
        """
        Return the reverse of the dictionary returned by the `freq_of_lang`
        where the keys are the frequency of each language and the values are
        the list of languages that have that frequency.
        """

        language_freq = self.freq_of_lang()
        language_hist = {}
        for lang, freq in language_freq.items():
            if freq not in language_hist:
                language_hist[freq] = []
            language_hist[freq].append(lang)
        return language_hist

    def write_lang_popularity(self):
        """
        Write the histogram of programming languages to a text file. The
        file has two columns: the frequency of the programming language and
        the programming language itself.
        """
