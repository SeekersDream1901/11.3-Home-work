import json


def load_candidates_from_json():
    with open("candidates.json", 'r', encoding='utf-8') as file:
        all_candidates = json.load(file)
        return all_candidates


def get_candidate_by_id(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate
    return 'Not Found'


def get_candidates_by_name(candidate_name):
    count = 0
    candidates = []
    for candidate in load_candidates_from_json():
        candidate_name_in_list = candidate['name'].split(' ')
        print(candidate_name_in_list)
        if candidate_name.lower() == candidate_name_in_list[0].lower():
            count += 1
            candidates.append(candidate)
    return count, candidates


def get_candidates_by_skill(skill_name):
    count = 0
    candidates = []
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            count += 1
            candidates.append(candidate)
    return count, candidates
