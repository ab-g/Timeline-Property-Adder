import os
import json


def get_first_scene_id(resource_pack_data):
    return resource_pack_data['scenes']['map'][0]['value']['id']['uuid']


def main(game_project_dir_path):
    resource_pack_file_path = os.path.join(game_project_dir_path, 'resource-pack.json')
    with open(resource_pack_file_path, 'r') as resource_pack_file:
        resource_pack_data = json.load(resource_pack_file)

    scene_id = get_first_scene_id(resource_pack_data)
    scene_file_path = os.path.join(game_project_dir_path, 'scenes/{0}.json'.format(scene_id))

    with open(scene_file_path, 'r') as scene_file:
        scene_data = json.load(scene_file)

    priority_level = 0
    for script in scene_data['scriptSystem']['scripts']:
        script_id = script['id']['uuid']
        script_file_path = os.path.join(game_project_dir_path, 'scripts/{0}.json'.format(script_id))
        script_class = script['@class']
        if script_class == 'TimeLineScript':
            with open(script_file_path, 'r') as script_file:
                script_data = json.load(script_file)
                script_data['priority'] = priority_level
                priority_level += 1
            with open(script_file_path, 'w') as script_file:
                json.dump(script_data, script_file, indent=4, sort_keys=False)


if __name__ == '__main__':
    main(sys.argv[1])
