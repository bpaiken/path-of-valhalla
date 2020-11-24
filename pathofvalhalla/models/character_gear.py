from armor import Armor

class CharacterGear:
    def __init__(self, args):
        if 'cloak' in args: self._cloak = Armor(args['cloak'])
        else: self._cloak = None # todo: check is this needed/does this do anything in python?
        if 'helmet' in args: self._helmet = Armor(args['helmet'])
        else: self._helmet = None
        if 'torso' in args: self._torso = Armor(args['torso']) 
        else: self._torso = None
        if 'bracers' in args: self._bracers = Armor(args['bracers'])
        else: self._bracers = None
        if 'pants' in args: self._pants = Armor(args['pants']) 
        else: self._pants = None

    def set_cloak(self):
        print('not yet implemented')

    def set_helmet(self):
        print('not yet implemented')
    
    def set_torso(self):
        print('not yet implemented')
    
    def set_bracers(self):
        print('not yet implemented')
    
    def set_pants(self):
        print('not yet implemented')