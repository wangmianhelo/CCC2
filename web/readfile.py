def map(name):
    lines = ''
    datafile = ''
    with open(name) as f:
        for line in f.readlines():
            line = line.strip()
            if line.__contains__('='):
                line = line.split()

                data = line[3:]

                datafile = "".join(data)


            else:
                if line.startswith('{'):
                    lines = line + lines

        return datafile + lines

if __name__ == '__main__':
    data = map('static/js/us-states.js')
    print(data)