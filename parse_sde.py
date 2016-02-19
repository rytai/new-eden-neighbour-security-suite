with open('mapSolarSystemJumps') as f:

    f.readline()

    jumps = {}

    from_jump = None
    column = 1
    sentence = ''

    for line in f.readlines():


        for symbol in line[:-2]:
            if symbol == ',':
                column += 1
                if column > 6:
                    column = 1

                if column == 3:
                    from_jump = sentence

                if column == 6:
                    to_jump = sentence
                    jumps[from_jump] = to_jump

                sentence = ''
            else:
                sentence+=symbol

print jumps.items()