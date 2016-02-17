def read_data(file_names):
    data = []
    for file_name in file_names:
        f = open(file_name,'r')
        data.append([line[:-1] for line in f])
        f.close()
    return data