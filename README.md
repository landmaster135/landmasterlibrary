# landmasterlibrary

This library is create by kinkinbeer135ml.

# Installation

```bash
pip install git+https://github.com/landmaster135/landmasterlibrary.git
```

# Importation

To activate me, input this in python file.

```python
import * from landmasterlibrary
```

 # Modules

1. config.py
2. dir_editor.py
3. export_sqlite_to_csv.py
4. file_list_getter.py
5. generaltool.py
6. image_editor.py
7. input_controller.py
8. morph_analysis.py
9. pdf_rotater.py
10. text_editor.py
11. text_replacer.py

# Functions in each Module

## export_sqlite_to_csv.py

- export_to_csv

## file_list_getter.py

- extract_playlist_from_text
- extract_file_name_book
- confirm_execution
- edit_file_name
- get_file_list
- main

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

## image_editor.py

- select_area
- update
- trim_image
- judge_match_rate_by_feature_point
- judge_match_rate_by_pixel_match
- remove_duplication
- extract_image
- get_times_of_movie_in_folder
- extract_sound_to_text
- resize_img
- get_statistics
- get_youtube_statistics
- main

## input_controller.py

- check_whether_sjis_exists
- repeat_input_with_multi_choices
- main

### morph_analysis.py


## pdf_rotater.py

- make_vertical
- main
## text_editor.py

- write_playlist
- write_csv
- write_text
- main

## text_replacer.py

- make_voicedsound
- main

# Usage by `console_scripts`

<!-- You can use like these by `__name__ == "__main__"`. -->

You can use like these by `console_scripts`.

## dir_editor.py

- write_text

```bash
python dir_editor.py '/Users/landmaster/Downloads/test_folder/test.txt'
```

## 🗄 &nbsp; export_sqlite_to_csv.py

- write_text

```bash
python dir_editor.py '/Users/landmaster/Downloads/test_folder/test.txt'
```

## 🗂 &nbsp; file_list_getter


- extract_playlist_from_text

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

- extract_file_name_book

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

- edit_file_name

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

- get_file_list

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder' 'png'
```

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

## 🎞 &nbsp; image_editor

- select_area

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder'
```

- trim_image

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder' 'jpg'
```

- remove_duplication

```bash
python image_editor.py
```

- extract_image

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder/test_movie.mp4'
```

## 📑 &nbsp; pdf_rotater

- make_vertical

```bash
python pdf_rotater.py '/Users/landmaster/Downloads/test_folder'
```

## 📝 &nbsp; text_editor

- write_text

```bash
python text_editor.py '/Users/landmaster/Downloads/test_folder/test.txt'
```

***

# Diagram

**_Module_Diagram.drawio** shows diagram of this library.
