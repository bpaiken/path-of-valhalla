import json
# import models.skill_node
from models.types import SkillNodeType
# from models.skill_node import StatSkillNode
from models.skill_tree import SkillTree

def main():
    # print("hello valhalla")

    data = None
    with open("../data/skill_tree.json", "r") as read_file:
        data = json.load(read_file)

    print(type(data))

    skill_tree = SkillTree(data)

# skill_dictionary = {}
# skill_nodes = data['clusters'][1]['skill_nodes']
# for node in skill_nodes:
#     if(node['type'] == SkillNodeType.stat()):
#         snode = StatSkillNode(node)
#         skill_dictionary[node['id']] = snode
#     pass

# print(skill_dictionary['stomp|1'].links)

if __name__ == '__main__' : main()