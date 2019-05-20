import difflib
import logging
from typing import List

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)


def read_file(file_name: str) -> str:
    logging.info('Reading input file')
    with open(file_name, 'r') as input_file:
        file_content = input_file.read()

    logging.info('file content successfully read')
    return file_content


def compare_by_strings(input_text: str, pattern: str) -> List[str]:
    logging.info('comparison by strings')

    common_strings = []

    input_rows = input_text.split('\n')
    pattern_rows = pattern.split('\n')

    for i in range(len(input_rows)):
        for j in range(len(pattern_rows)):

            if pattern_rows[j] == input_rows[i]:
                common_strings.append(input_rows[i])

    return common_strings


def get_rows_if_contain(input_text: str, pattern: str) -> List[str]:
    logging.info('comparison by words')

    alike_lines = []

    input_rows = input_text.split('\n')
    pattern_rows = pattern.split('\n')

    for i in range(len(input_rows)):
        for j in range(len(pattern_rows)):

            if pattern_rows[j] in input_rows[i]:
                alike_lines.append(input_rows[i])

    return alike_lines


def compare_match_in_percentage(left_text: str, right_text: str) -> List[str]:
    logging.info('comparing match in percentage')

    alike_lines = []

    input_rows = left_text.split('\n')
    pattern_rows = right_text.split('\n')

    for i in range(len(input_rows)):
        for j in range(len(pattern_rows)):

            sequence = difflib.SequenceMatcher(isjunk=None, a=input_rows[i], b=pattern_rows[j])
            difference = sequence.ratio() * 100
            difference = round(difference, 1)

            if difference > 50:
                result_row = 'input: ' + input_rows[i] + ' pattern: ' + pattern_rows[j] + f' score: {difference}'
                alike_lines.append(result_row)

    return alike_lines


def zen_run():
    patterns = read_file('patterns.txt')
    input_text = read_file('input.txt')

    string_comparison_results = compare_by_strings(input_text, patterns)
    print(f'string comparison results: \n{string_comparison_results}')

    string_contains_results = get_rows_if_contain(input_text, patterns)
    print(f'string contains results: \n{string_contains_results}')

    alike_percentage = compare_match_in_percentage(input_text, patterns)
    print(f'alike percentage: \n{alike_percentage}')


zen_run()
