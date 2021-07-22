import yaml
from sys import stderr
from os import scandir

DIRECTORIES = [ ("Application mobile", "mobile_app"), ("Logiciel commerçant", "shopkeeper_app"), ("Back-end", "back_end"), ("Terminal de paiement", "tpe"), ("Recherches", "research")]
REQUIRED_YAML_KEY = ["id", "title", "as", "iWantTo", "description", "definitionOfDone", "estimation"]
OUTFILE_NAME = "stories.md"

def yamlToLatex(file_path: str) -> str:
    with open(file_path, "r") as stream:
        content: dict = yaml.safe_load(stream)
    if all(map(lambda key: key in content, REQUIRED_YAML_KEY)):
        formatedDoD = ",".join([f"{{{dod}}}" for dod in content["definitionOfDone"]])

        return f'\\userStoryCard{{{content["id"]} - {content["title"]}}}{{{content["as"]}}}{{{content["iWantTo"]}}}{{{content["description"]}}}{{{formatedDoD}}}{{{content["estimation"]}}}'
    else:
        print(f"Missing key in {file_path}. Required keys are: {REQUIRED_YAML_KEY}", file=stderr)
        exit(1)


def compile():
    outfile = []

    for (dir_name, dir_path) in DIRECTORIES:
        outfile.append(f"## {dir_name}")
        for elem in sorted(scandir(dir_path), key=lambda x: x.name):
            if elem.is_file() and elem.path.endswith(".yaml"):
                try:
                    outfile.append(yamlToLatex(elem.path))
                except yaml.YAMLError as e:
                    print(e, file=stderr)
                    exit(1)

    with open(OUTFILE_NAME, 'w') as file:
        file.write('\n'.join(outfile))


if __name__ == "__main__":
    compile()
