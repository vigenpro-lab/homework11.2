# import json
#
#
# def load_candidates_from_json():
#     with open('candidates.json', 'r') as candidates:
#         return json.load(candidates)
#
#
# def get_candidate(candidate_id):
#     return load_candidates_from_json()[candidate_id - 1]
#
#
# def get_candidates_by_name(candidate_name):
#     return load_candidates_from_json()[candidate_name - 1]
#
#
# def get_candidates_by_skill(skill_name):
#     return load_candidates_from_json()[skill_name - 1]


import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_id == candidate['id']:
            del candidate['id']
            del candidate['gender']
            del candidate['age']
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_name in candidate['name'].lower().split():
            del candidate['id']
            del candidate['gender']
            del candidate['age']
            return candidate
    return None


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if skill_name in candidate['skills'].lower().split(", "):
            del candidate['gender']
            del candidate['age']
            result.append(candidate)
    return result


def get_names(candidates):
    result = []
    for candidate in candidates:
        result.append(candidate)
    return result