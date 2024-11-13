## Analysis Class Design Document
- Developer: Nalin
- Date: 11/10/2024

### freq_of_lang Method Design

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


### (replace with method name) Method Design
...

### (replace with method name) Method Design

