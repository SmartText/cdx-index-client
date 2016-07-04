from cc_interface import get_cc_file

def read_file(file_path):
    import json

    file = open(file_path)
    for line in file.readlines():
        line = line[:-1]
        obj,json_data = line.split('{')
        json_data = '{%s' % json_data
        data = json.loads(json_data)
        s3_file = "common-crawl/crawl-data/%s" % data['filename'].split('/', 1)[1]
        print(s3_file)
        get_cc_file("%s" % s3_file)

def main(folder):
    from os import walk
    for parent,dirs,files in walk(folder):
        for file in files:
            path =  "%s/%s" % (parent, file)
            read_file(path)

if __name__ == "__main__":
    from sys import argv

    main(argv[1])
