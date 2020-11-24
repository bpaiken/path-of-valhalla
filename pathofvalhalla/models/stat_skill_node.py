from skill_node import SkillNode
# from types import SkillNodeType

class StatSkillNode(SkillNode):
    def __init__(self, args):
        self.value = args['value']
        self.stat = args['stat']
        
        # don't think I need this...
        # self._type = SkillNodeType.stat()
        