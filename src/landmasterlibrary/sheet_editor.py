
class SheetEditor:
    def to_alpha_under_3digits(self, number : int) -> str:
        """
        Number of cell this method can format is 26 x 26 x 27 = 18252.
        """
        number_of_alphabet = 26
        h = int((number - 1 - number_of_alphabet) / (number_of_alphabet * number_of_alphabet))
        i = int((number - 1) / number_of_alphabet) - h * number_of_alphabet
        j = number - (i * number_of_alphabet) - (h * number_of_alphabet * number_of_alphabet)
        alpha = ''
        for k in h, i, j:
            if k != 0:
                alpha += chr(k + 64)
        return alpha

    def get_cell_in_a1_notation(self, row_index : int, col_index : int) -> str:
        con_index_alpha =self.to_alpha_under_3digits(col_index)
        cell = "{1}{0}".format(str(row_index), str(con_index_alpha))
        return cell

    def get_range_in_a1_notation(self, start_row_index : int, start_col_index : int, num_rows : int, num_cols : int) -> str:
        start_cell = self.get_cell_in_a1_notation(start_row_index, start_col_index)
        end_row_index = start_row_index + num_rows - 1
        end_col_index = start_col_index + num_cols - 1
        end_cell = self.get_cell_in_a1_notation(end_row_index, end_col_index)
        return "{}:{}".format(start_cell, end_cell)

    def format_cell_position_in_formula(self, formula : str, dest_row_index : int, dest_col_index : int, mark_of_cell_position : str = "CELLPOSITION") -> str:
        dest_cell_in_a1_notation = self.get_cell_in_a1_notation(dest_row_index, dest_col_index)
        formula_formatted = formula.replace(mark_of_cell_position, dest_cell_in_a1_notation)
        return formula_formatted

    def authorize_gss_to_get_worksheet(self, credential_json_file_name : str, gss_id : str, sheet_name : str):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_json_file_name, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open_by_key(gss_id).worksheet(sheet_name)
        print(worksheet)
        print(type(worksheet))
        print(vars(worksheet))
        return worksheet

    def get_matched_cell_list_from_worksheet_by_match_value(self, worksheet, value : str) -> list:
        class_name = self.__class__.__name__
        function_name = sys._getframe().f_code.co_name
        cell_list = worksheet.findall(value)
        output_log(
            class_name,
            function_name,
            f"{get_str_repeated_to_mark('a')}"
        )
        for cell in cell_list:
            print(vars(cell))
        return cell_list

    def get_record_list_by_all_keyword_hit(self, record_list : list, keyword_list : list, get_target_cols : list, search_target_cols : list = [3, 4, 5, 6, 7, 8]) -> list:
        class_name = self.__class__.__name__
        function_name = sys._getframe().f_code.co_name
        hit_record_list = []
        lowered_keyword_list = self.get_all_lowered_case_list(keyword_list)

        # 全体一致の場合はこっち
        hit_count_required = len(keyword_list)
        for record in record_list:
            hit_count = 0
            for i in search_target_cols:
                if len(record) <= i:
                    break
                lowered_value = record[i].lower()
                if lowered_value in lowered_keyword_list:
                    hit_count += 1
                if hit_count == hit_count_required:
                    hit_record_list.append(record)
                    break
        output_log(
            class_name,
            function_name,
            f"{get_str_repeated_to_mark('a')}"
        )
        return hit_record_list


    def get_record_list_from_worksheet_orienting_range(self, worksheet, start_row : int, start_col : int, num_cols : int) -> list:
        class_name = self.__class__.__name__
        function_name = sys._getframe().f_code.co_name
        sheetEditor = SheetEditor()
        row_count = self.get_row_count_in_sheet(worksheet)
        output_log(
            class_name,
            function_name,
            "{}".format(get_str_repeated_to_mark("a"))
        )
        target_range_in_a1_notation = sheetEditor.get_range_in_a1_notation(start_row, start_col, row_count - 1, num_cols)
        output_log(
            class_name,
            function_name,
            "{}".format(get_str_repeated_to_mark("b"))
        )
        record_list = worksheet.get(target_range_in_a1_notation)
        output_log(
            class_name,
            function_name,
            "{}".format(get_str_repeated_to_mark("c"))
        )
        return record_list

    def get_record_list_by_each_keyword_hit(self, record_list : list, keyword_list : list, get_target_cols : list, search_target_cols : list = [3, 4, 5, 6, 7, 8]) -> list:
        class_name = self.__class__.__name__
        function_name = sys._getframe().f_code.co_name
        hit_record_list = []
        lowered_keyword_list = self.get_all_lowered_case_list(keyword_list)

        # 部分一致の場合はこっち
        for record in record_list:
            for i in search_target_cols:
                if len(record) <= i:
                    break
                lowered_value = record[i].lower()
                if lowered_value in lowered_keyword_list:
                    hit_record_list.append(record)
                    break
        output_log(
            class_name,
            function_name,
            f"{get_str_repeated_to_mark('a')}"
        )
        return hit_record_list


    def get_all_lowered_case_list(self, target_list : list) -> list:
        lowered_list = []
        for item in target_list:
            lowered_list.append(item.lower())
        return lowered_list

    def get_row_count_in_sheet(self, worksheet, basis_col_index : int = 1) -> int:
        class_name = self.__class__.__name__
        function_name = sys._getframe().f_code.co_name
        row_count = len(worksheet.col_values(basis_col_index))
        output_log(
            class_name,
            function_name,
            "{}: row count is {}".format(
                get_str_repeated_to_mark("a"),
                f"{str(row_count)}"
            )
        )
        return row_count

    def is_only_not_url_column_in_list(self, cell_list : list, col_index_url : int) -> bool:
        config_file_full_name = get_src_path_from_test_path(__file__, config_file_name, src_folder_name)
        config_obj = get_obj_from_yaml(config_file_full_name)
        try:
            pattern = "[0-9]+"
            is_only_not_url_column = True
            for cell in cell_list:
                reResult = re.match(pattern, str(cell.col))
                if reResult == None:
                    raise ValueError(config_obj["msg_obj_e0103"])
                if cell.col == col_index_url:
                    is_only_not_url_column = False
        except ValueError as e:
            raise
        return is_only_not_url_column
