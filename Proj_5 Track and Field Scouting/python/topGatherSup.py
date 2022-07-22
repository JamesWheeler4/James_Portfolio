# Used (Updated 2022/03/31)
def topMarkCalc(x, y):  # input will be (event[0], mark[0])
    eventR = ('100 Meters', '200 Meters', '400 Meters', '800 Meters', '1500 Meters', '1600 Meters',
              '3000 Meters', '3200 Meters', '110m Hurdles - 39"', '300m Hurdles - 36"',
              '100m Hurdles - 33"',
              '300m Hurdles - 30"')
    eventF = ('Shot Put - 12lb', 'Shot Put - 4kg', 'Discus - 1.6kg', 'Discus - 1kg', 'Javelin - 800g',
              'Javelin - 600g', 'High Jump', 'Pole Vault', 'Long Jump', 'Triple Jump', 'Hammer - 16lb',
              'Hammer - 4kg')

    if y.strip()[-1] == 'c' or y.strip()[-1] == 'h':
        y = y[:-1]
    for i in eventR:
        if i == x:
            try:
                lst = y.split(':')
                markcomp = (int(lst[0]) * 60) + float(lst[1])
            except:
                markcomp = float(y)

    for i in eventF:
        if i == x:
            spl = y.split("'")
            inch = round(float(spl[1].strip()) / 12, 2)
            markcomp = int(spl[0]) + inch
    return round(markcomp, 2)


# Used
def topEventType(x):  # Determine what event type the each entry is to sort later
    eventT = ('100 Meters', '200 Meters', '400 Meters', '800 Meters', '1500 Meters', '1600 Meters',
              '3000 Meters', '3200 Meters', '110m Hurdles - 39"', '300m Hurdles - 36"', '100m Hurdles - 33"',
              '300m Hurdles - 30"')
    eventF = ('Shot Put - 12lb', 'Shot Put - 4kg', 'Discus - 1.6kg', 'Discus - 1kg', 'Javelin - 800g',
              'Javelin - 600g', 'High Jump', 'Pole Vault', 'Long Jump', 'Triple Jump', 'Hammer - 16lb',
              'Hammer - 4kg')

    for i in eventT:
        if i == x:
            return '1'

    for i in eventF:
        if i == x:
            return '2'


# Used
def topNameSwap(x):
    dict = {'100 Meters': '100m', '200 Meters': '200m', '400 Meters': '400m', '800 Meters': '800m',
            '1500 Meters': '1500m', '100m Hurdles - 33"': '100mh', '110m Hurdles - 39"': '110mh',
            'Shot Put - 12lb': 'shot', 'Shot Put - 4kg': 'shot', 'Discus - 1.6kg': 'discus',
            'Discus - 1kg': 'discus', 'Javelin - 800g': 'javelin', 'Javelin - 600g': 'javelin',
            'High Jump': 'hj', 'Pole Vault': 'pv', 'Long Jump': 'lj', 'Triple Jump': 'tj',
            'Hammer - 16lb': 'hammer', 'Hammer - 4kg': 'hammer', '3000 Meters': '3000m',
            '300m Hurdles - 36"': '300mh', '1600 Meters': '1600m', '3200 Meters': '3200m',
            '300m Hurdles - 30"': '300mh'}
    for k, v in dict.items():
        if k == x:
            x = v
    return x
