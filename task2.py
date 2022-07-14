import re


def check(file_path, txt):
    with open(file_path) as dataf:
        return any(txt in line for line in dataf)


def task2(title_format, text_format, file_path):
    try:
        with open(file_path, 'r') as fp:
            arr_res = []
            lines = fp.readlines()
            string = "AEWI "
            if string.find(title_format) == -1:
                return 'Sorry, title format not found'

            for line in lines:
                line_index = lines.index(line) + 1
                line = line.strip()
                if check(file_path, text_format):
                    if title_format == 'A' or title_format == '':
                        res = re.match(text_format + r"\d{5}", line)
                        if res is not None:
                            res1 = {'msg': line[0:9],
                                    'type': line[8],
                                    'offset': line_index,
                                    'text': line[10:len(line)]}
                            arr_res.append(res1)
                    else:
                        res = re.match(text_format + r"\d{5}" + title_format, line)
                        if res is not None:
                            res1 = {'msg': line[0:9],
                                    'type': line[8],
                                    'offset': line_index,
                                    'text': line[10:len(line)]}
                            arr_res.append(res1)
                else:
                    return 'Sorry, text format not found'
            if len(arr_res) == 0:
                return 'Sorry, no information found'
            return arr_res
    except EnvironmentError:
        return "Sorry, file not found, please, try one more time"