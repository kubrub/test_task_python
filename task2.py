import re


def task2(title_format, text_format, file_path):
    try:
        with open(file_path, 'r') as fp:
            arr_res = []
            lines = fp.readlines()
            string = "AEWI "
            if string.find(title_format) == -1:
                print('title format not found')

            for line in lines:
                line_index = lines.index(line)
                line = line.strip()
                if title_format == 'A' or title_format == '':
                    res = re.match(text_format + r"\d{5}", line)
                    if res is not None:
                        res1 = {'msg': line[0:9],
                                'type': line[8],
                                'offset': line_index,
                                'text': line[10:len(line)]}
                        arr_res.append(res1)
                elif title_format == 'I':
                    res = re.search(text_format + r"\d{5}" + title_format, line)
                    if res is not None:
                        res1 = {'msg': line[0:9],
                                'type': line[8],
                                'offset': line_index,
                                'text': line[10:len(line)]}
                        arr_res.append(res1)
                elif title_format == 'E':
                    res = re.search(text_format + r"\d{5}" + title_format, line)
                    if res is not None:
                        res1 = {'msg': line[0:9],
                                'type': line[8],
                                'offset': line_index,
                                'text': line[10:len(line)]}
                        arr_res.append(res1)
                elif title_format == 'W':
                    res = re.search(text_format + r"\d{5}" + title_format, line)
                    if res is not None:
                        res1 = {'msg': line[0:9],
                                'type': line[8],
                                'offset': line_index,
                                'text': line[10:len(line)]}
                        arr_res.append(res1)
            return arr_res
    except EnvironmentError:
        return "Sorry, file not found, please, try one more time"