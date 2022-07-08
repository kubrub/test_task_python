def task2(title_format, text_format, file_path):

    try:
        with open(file_path, 'r') as fp:
            arr_res = []
            lines = fp.readlines()
            for line in lines:
                line_index = lines.index(line)
                line = line.strip()
                string = "AEWI "
                if line.find(title_format) == -1:
                    return "Sorry, title format not found, please, try one more time"
                elif string.find(text_format) == -1:
                    return "Sorry, text format not found, please, try one more time"
                elif line.find(title_format) != -1 and line[0] == title_format[0] and (
                        text_format == 'A' or text_format == ''):
                    res = {'msg': line[0:9],
                           'type': line[8],
                           'offset': line_index,
                           'text': line[10:len(line)]}
                    arr_res.append(res)

                elif line.find(title_format) != -1 and line[0] == title_format[0] and text_format == line[8]:
                    res = {'msg': line[0:9],
                           'type': line[8],
                           'offset': line_index,
                           'text': line[10:len(line)]}
                    arr_res.append(res)
            return arr_res
    except EnvironmentError:
        return "Sorry, file not found, please, try one more time"
