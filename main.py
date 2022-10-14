import requests


class Package:
    __data = {
        "name": "string",
        "epoch": 0,
        "version": "string",
        "release": "string",
        "arch": "string",
        "disttag": "string",
        "buildtime": 0,
        "source": "string"
    }

    def __init__(self, data):
        self.__data['name'] = data['name']
        self.__data['epoch'] = data['epoch']
        self.__data['version'] = data['version']
        self.__data['release'] = data['release']
        self.__data['arch'] = data['arch']
        self.__data["disttag"] = data['disttag']
        self.__data["buildtime"] = data['buildtime']
        self.__data["source"] = data['source']

    def __hash__(self):
        return hash(self.__data['name'])

    def __eq__(self, other):
        if self.__data['name'] == other.__data['name'] :
            return True
        else:
            return False

    def __repr__(self):
        return str({
            self.__data['name'],
            self.__data['version'],
            self.__data['release']
        })

    def __str__(self):
        return str({
            self.__data['name'],
            self.__data['version'],
            self.__data['release']
        })


def get_all_packages():
    response_sisyphus = requests.get('https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus').json()
    response_p10 = requests.get('https://rdb.altlinux.org/api/export/branch_binary_packages/p10').json()
    set_sisyphus = set(Package(response_sisyphus['packages'][i]) for i in range(0, len(response_sisyphus['packages'])))
    set_p10 = set(Package(response_p10['packages'][i]) for i in range(0, len(response_p10['packages'])))

    print(f'{set_p10 - set_sisyphus=}')


get_all_packages()
