from skill_node import SkillNode, StatSkillNode
from types import SkillNodeType

class SkillTree:
    def __init__(self, json_input = None):
        if json_input: self._input = json_input
        if json_input['clusters']: self._clusters = json_input['clusters']
        self._node_tree = self.build_node_tree(self._clusters)

    def build_node_tree(self, clusters):
        # want node tree to take the form of dictionary w/ { nodeId: node }
        # this will allow us to quickly/easily access nodes as needed, without having to search through an array
        node_tree = {}
        for cluster in clusters:
            if 'skill_nodes' in cluster: skill_nodes = cluster['skill_nodes']
            for node_object in skill_nodes:
                node = self.build_skill_node(node_object)
                if node:
                    node_tree[node.id] = node
                # end node loop
            # end cluster loop
        return node_tree

    def build_skill_node(self, node_object):
        node_type = node_object['type']
        if node_type == SkillNodeType.stat():
            return StatSkillNode(node_object)

        elif node_type == SkillNodeType.gear():
            # todo
            pass

        elif node_type == SkillNodeType.notable():
            # todo
            pass

        elif node_type == SkillNodeType.origin():
            # todo
            pass
        
        else: 
            return None
