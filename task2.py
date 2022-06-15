def task2(title_format, text_format, file_path):
    arr_res = []
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(title_format) != -1 and line[0] == title_format[0] and (
                    text_format == 'A' or text_format == ''):
                res = {'msg': line[0:9],
                       'type': line[8],
                       'offset': lines.index(line),
                       'text': line[10:len(line)]}
                arr_res.append(res)

            elif line.find(title_format) != -1 and line[0] == title_format[0] and text_format == line[8]:
                res = {'msg': line[0:9],
                       'type': line[8],
                       'offset': lines.index(line),
                       'text': line[10:len(line)]}
                arr_res.append(res)

    return arr_res