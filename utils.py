import json


def load_candidates(path):
    """Загружает список кандидатов из файла"""
    with open(path, 'r', encoding='utf-8') as file:
        list_candidates = json.load(file)
        file.close()
        return list_candidates


# noinspection PyGlobalUndefined
def get_by_id(id_):
    """Возвращает кандидатов по номеру"""
    global picture_link
    list_candidates = load_candidates('candidates.json')
    single_candidate = {}
    for candidate in list_candidates:
        if candidate["id"] == id_:
            single_candidate = candidate
        else:
            pass
    return single_candidate


def get_by_skill(skill_name):
    """Возвращает кандидатов по навыкам"""
    list_candidates = load_candidates('candidates.json')
    list_candidate_by_skills = []
    for candidate in list_candidates:
        list_skills = (candidate["skills"]).split(', ')
        if skill_name.lower() in list_skills or skill_name.title() in list_skills:
            list_candidate_by_skills.append(candidate)
        else:
            pass
    return list_candidate_by_skills


    """Возвращает кандидатов по имени"""
    list_candidates = load_candidates('candidates.json')
    candidate_by_name = {}
    for candidate in list_candidates:
        if name.lower() == candidate['name'].lower():
            candidate_by_name = candidate
        else:
            pass
    return candidate_by_name
