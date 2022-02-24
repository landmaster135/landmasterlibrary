# landmasterlibrary

This library is create by kinkinbeer135ml.

***

## Install

```bash
pip install git+https://github.com/landmaster135/landmasterlibrary.git
```

## Import

To activate me, input this in python file.

```python
import * from landmasterlibrary
```

 ## Modules

1. input_controller.py
2. dir_editor.py
3. text_editor.py
4. file_list_getter.py
5. pdf_rotater.py
6. ImageEditor.py

## Usage

You can use like these by `__name__ == "__main__"`.

### text_editor

write_text()

```bash
python text_editor.py '/Users/landmaster/Downloads/test_folder/test.txt'
```

### file_list_getter

extract_playlist_from_text()

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

extract_file_name_book()

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

edit_file_name()

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder'
```

get_file_list()

```bash
python file_list_getter.py '/Users/landmaster/Downloads/test_folder' 'png'
```

### pdf_rotater

make_vertical()

```bash
python pdf_rotater.py '/Users/landmaster/Downloads/test_folder'
```

### image_editor

select_area()

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder'
```

trim_image()

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder' 'jpg'
```

remove_duplication()

```bash
python image_editor.py
```

extract_image()

```bash
python image_editor.py '/Users/landmaster/Downloads/test_folder/test_movie.mp4'
```

***

##### **_Module_Diagram.drawio** shows diagram of this library.
