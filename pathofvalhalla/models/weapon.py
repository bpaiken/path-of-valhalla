class Weapon:
    def __init__(self, args):
        if 'name' in args: self._name = args['name']
        if 'attack' in args: self._name = args['attack']
        if 'stun' in args: self._name = args['stun']
        if 'speed' in args: self._name = args['speed']
        if 'weight' in args: self._name = args['weight']
        if 'critcal_chance' in args: self._name = args['critcal_chance']
        if 'critical_damage' in args: self._name = args['critical_damage']
        
