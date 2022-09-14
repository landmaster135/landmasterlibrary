# landmasterlibrary

<img width="20%" alt="landmasterlibrarylocal" src="./img/01-01_landmasterlibrary.png">

This library is create by kinkinbeer135ml.

# Installation

```bash
pip install git+https://github.com/landmaster135/landmasterlibrary.git
```

# Importation

```python
import * from landmasterlibrary
```

 # Modules

1. config.py
2. generaltool.py
3. morph_analysis.py
4. text_replacer.py

# Functions in each Module

## generaltool.py

- get_str_repeated_to_mark
- output_log
- get_str_from_list
- get_obj_from_yaml
- get_value_from_yaml
- get_src_path_from_test_path
- get_indices_by_seperators
- get_words_by_indices
- get_words_by_seperators
- remove_spaces_at_head_and_tail
- remove_tail_sapces
- remove_head_sapces
- get_functions_in_python_file
- get_words_in_lines_by_head_and_tail
- printfunc

### morph_analysis.py


## text_replacer.py

- make_voicedsound
- main

# Usage by `console_scripts`

<!-- You can use like these by `__name__ == "__main__"`. -->

You can use like these by `console_scripts`.

## 💼 &nbsp; generaltool

- printfunc

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder' 'png'
```

example

```bash
printfunc /usr/local/lib/python3.8/dist-packages/landmasterlibrary/generaltool.py '###'
```

->

```shell
============ functions list: start ============
### get_str_repeated_to_mark
### output_log
### get_str_from_list
### get_obj_from_yaml
### get_value_from_yaml
### get_src_path_from_test_path
### get_indices_by_seperators
### get_words_by_indices
### get_words_by_seperators
### remove_spaces_at_head_and_tail
### remove_tail_sapces
### remove_head_sapces
### get_functions_in_python_file
### get_words_in_lines_by_head_and_tail
### printfunc
============ functions list: end ============
```

***

# Diagram

```mermaid
classDiagram
  class generaltool{
    +get_str_repeated_to_mark()
    +output_log()
    +get_str_from_list()
    +get_obj_from_yaml()
    +get_value_from_yaml()
    +get_src_path_from_test_path()
    +get_indices_by_seperators()
    +get_words_by_indices()
    +get_words_by_seperators()
    +remove_spaces_at_head_and_tail()
    +remove_tail_sapces()
    +remove_head_sapces()
    +get_functions_in_python_file()
    +get_words_in_lines_by_head_and_tail()
    +printfunc()
  }
  class morph_analysis{
    +Tokenizer tokenizer
    +list sentences
  }
  class text_replacer{
    +bool is_wild
    +run()
  }
```
