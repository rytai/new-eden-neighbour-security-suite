def parse_sde():
    with open('mapSolarSystemJumps') as f:

        f.readline()

        jumps = {}

        from_jump = None
        column = 1
        sentence = ''

        for line in f.readlines():

            for symbol in line[:-2]:
                # Separator
                if symbol == ',':

                    # Found from_solar_system jump
                    if column == 3:
                        from_jump = sentence

                    # Found to_solar_system jump
                    if column == 4:
                        to_jump = sentence
                        # Try if a jump already exists.
                        try:
                            jumps[from_jump].append(to_jump)
                        except:  # Create list containing this jump.
                            jumps[from_jump] = [to_jump]

                    sentence = ''
                    column += 1
                    if column > 6:
                        column = 1
                elif symbol == '"':
                    pass
                else:
                    sentence += symbol

            sentence = ''
            column = 1

    with open('mapSolarSystemJumps_parsed', 'w') as f:
        for from_, to_list in jumps.items():
            f.write(from_)
            f.write(str(to_list.__len__()))
            if to_list.__len__() > 9:
                print 'ERRORRRR'
            for to_ in to_list:
                f.write(to_)
            f.write('\n')

    return jumps

parse_sde()