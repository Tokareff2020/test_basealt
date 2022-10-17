import requests


class Package:

    def __init__(self, data):
        self.__data = dict()
        self.__data['name'] = data['name']
        self.__data['epoch'] = data['epoch']
        self.__data['version'] = data['version']
        self.__data['release'] = data['release']
        self.__data['arch'] = data['arch']
        self.__data["disttag"] = data['disttag']
        self.__data["buildtime"] = data['buildtime']
        self.__data["source"] = data['source']

    def __repr__(self):
        return str((
            self.__data['name'],
            self.__data['version'],
            self.__data['release'],
            self.__data['arch'],
            self.__data["disttag"],
            self.__data["source"]
        ))

    def __hash__(self):
        return hash(self.__data['name'] + self.__data['version'] + self.__data['release'] + self.__data['arch'] +
                    self.__data["disttag"] + self.__data["source"])

    def __eq__(self, other):
        if self.__data['name'] == other.__data['name'] and self.__data['version'] == other.__data['version'] and\
                self.__data['release'] == other.__data['release'] and self.__data['arch'] == other.__data['arch']:
            return True
        return False


    def __str__(self):
        return str((
            self.__data['name'],
            self.__data['version'],
            self.__data['release']
        ))


def get_packages_branch(branch_name: str) -> set:
    response = requests.get(f'https://rdb.altlinux.org/api/export/branch_binary_packages/{branch_name}').json()
    return set(Package(response['packages'][i]) for i in range(0, len(response['packages'])))


def get_uniq_packages_branch(branch_name_1: str, branch_name_2: str) -> set:
    set_branch_name_1, set_branch_name_2 = get_packages_branch(branch_name_1), get_packages_branch(branch_name_2)
    return set_branch_name_2 - set_branch_name_1


def get_packages_version_release(branch_name_1: str, branch_name_2: str) -> set:
    set_branch_name_1, set_branch_name_2 = get_packages_branch(branch_name_1), get_packages_branch(branch_name_2)
    intersection_list = set_branch_name_2 & set_branch_name_1
    return intersection_list


print(get_uniq_packages_branch('sisyphus', 'p10'))
print(get_packages_version_release('sisyphus', 'p10'))

