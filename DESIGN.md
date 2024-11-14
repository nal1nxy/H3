## Analysis Class Design Document
- Developer: Nalin
- Date: 11/10/2024

### freq_of_lang Method Design
...
- Define a method `freq_of_lang()` with one parameter.
- The parameter is `self ` of datatype class instance.
- Define a local variable `language_freq`.
- Assign an empty dictionary to the variable `language_freq`.
- Use a `for` loop to iterate through the list of dictionaries `self.devs` using an iterator variable `dict` of datatype dictionary.
    - Define a local variable `language`.
    - Assign the value associated with the key `"LanguageAdmired"` in the dictonary `dict`to the variable `language`.
    - Define another local variable `lang_list`.
    - Assign, the `list` produced by using the `split` method on the variable `language` with `;` as the delimiter, to the variable `lang_list`.
    - Use another `for` loop to iterate `lang_list` using the iterator variable `lang` of datatype `string`.
        - If `lang` is not `"NA"`:
            - If `lang` is not in the dictionary `language_freq`:
                - Initialize the value associated with the key `lang` in the dictionary `language_freq` with `0`.
            - Increment the value associated with the key `lang` in the dictionary `language_freq` by `1`.
- Return the dictionary `language_freq`.


### lang_histogram Method Design
...
- Define a method `lang_histogram` with one parameter.
- The parameter is `self` of datatype class instance.
- Define a local variable `language_hist`.
- Assign an empty dictionary to the variable to the variable `language_hist`.
- Define another local variable `lang_freq`.
- Call the method `freq_of_lang()` on the instance of the class `self` and assign it's return value to the variable `lang_freq`.
- Use the `items()` method on the dictionary `lang_freq`.
- Use a `for` loop to iterate through the list `lang_freq.items()` with `lang`, `freq` as the iterator variables with `list` and `int` as datatypes respectively.
    - If `freq` is not in the dictionary `language_hist`:
        - Initialize the value associated with the key `freq` in the dictionary `language_hist` with an `empty list`.
    - Append `lang` to the list(value) associated with the key `freq` in the dictionary `language_hist`.
- Return the dictionary `language_hist`.

### write_lang_popularity Method Design
...
- Define a method `write_lang_histogram` with one parameter.
- The parameter is `self` of datatype class instance.
- Define a local varibale `language_hist`.
- Call the method `lang_histogram()` on the instance of the class `self` and assign it's return value to the variable `language_hist`.
- Using the `with` statement `open` the file `pop.csv` as `csv_file` in `write` mode using `utf-8` encoding with `newline` parameter with as `""`.
    - Define a local variable `file_writer`.
    - Use the `writer()` method in/from the package `csv` with `csv_file` as the parameter, assign this to the variable `file_writer`.
    - Use the `writerow()` method on the variable `file_writer` with the parameter as the list of `"Frequency"` and `"Language"`.
    - Use a `for` loop to iterate through the list `language_hist.items()` using the iterator variables `freq`, `Languages` with `int` and `list` as datatypes respectively.
        - Define a variable `langs`.
        - Use the `join()` method with `languages` as the parameter with `;` as the delimiter and assign this to the variable `langs`.
        - Use the method `writerow()` on the variable `file_writer` with the parameters as the list of `freq`, `langs`.

