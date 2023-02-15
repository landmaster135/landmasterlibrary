
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

        # normal system
    def test_is_only_not_url_column_in_list_1_1(self):
        judge = Judge()
        cell_1 = gspread.Cell(2, config_obj["col_index_url"], "test1")
        cell_2 = gspread.Cell(35, config_obj["col_index_url"], "test2")
        cell_list = [copy.deepcopy(cell_1), copy.deepcopy(cell_2)]
        actual = judge.is_only_not_url_column_in_list(
            cell_list,
            config_obj["col_index_url"]
        )
        expected = False
        assert expected == actual

    # normal system
    def test_is_only_not_url_column_in_list_1_2(self):
        judge = Judge()
        cell_1 = gspread.Cell(2, 2, "test1")
        cell_2 = gspread.Cell(35, config_obj["col_index_url"], "test2")
        cell_list = [copy.deepcopy(cell_1), copy.deepcopy(cell_2)]
        actual = judge.is_only_not_url_column_in_list(
            cell_list,
            config_obj["col_index_url"]
        )
        expected = False
        assert expected == actual

    # normal system
    def test_is_only_not_url_column_in_list_1_3(self):
        judge = Judge()
        cell_1 = gspread.Cell(2, 2, "test1")
        cell_2 = gspread.Cell(35, 5, "test2")
        cell_list = [copy.deepcopy(cell_1), copy.deepcopy(cell_2)]
        actual = judge.is_only_not_url_column_in_list(
            cell_list,
            config_obj["col_index_url"]
        )
        expected = True
        assert expected == actual

    # abnormal system
    def test_is_only_not_url_column_in_list_2_1(self):
        judge = Judge()
        cell_1 = gspread.Cell(2, config_obj["col_index_url"], "test1")
        cell_2 = gspread.Cell(35, str("a"), "test2")
        cell_list = [copy.deepcopy(cell_1), copy.deepcopy(cell_2)]
        with pytest.raises(ValueError) as e:
            actual = judge.is_only_not_url_column_in_list(
                cell_list,
                config_obj["col_index_url"]
            )
        assert str(e.value) == config_obj["msg_obj_e0103"]

        # def test_authorize_gss_to_get_worksheet(self):
    #     judge = Judge()
    #     json_key_file_name = get_src_path_from_test_path(__file__, config_obj["json_key_fle_name"])
    #     gss_id = config_obj["gss_id"]
    #     sheet_name = config_obj["sheet_name"]
    #     worksheet = judge.authorize_gss_to_get_worksheet(json_key_file_name, gss_id, sheet_name)
    #     expected = config_obj["sheet_name"]
    #     actual = worksheet.title
    #     self.assertEqual(expected, actual)

    # normal system
    # def test_get_matched_cell_list_from_worksheet_by_match_value_1_1(self):
    #     judge = Judge()
    #     config_obj = get_obj_from_yaml(
    #         get_src_path_from_test_path(__file__, config_file_name)
    #     )
    #     expected = False
    #     self.assertEqual(expected, actual)



    # def test_get_list_by_seperating_keyword_1_1(self):
    #     judge = Judge()
    #     keyword = "python, node.js , gollila、 web"
    #     seperators = config_obj["seperators"]
    #     actual = judge.get_list_by_seperating_keyword(keyword, seperators)
    #     expected = ["", "", "", ""]
    #     self.assertEqual(expected, actual)
