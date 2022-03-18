from typing import Dict, List, Union
import yaml
from sys import stderr

FILES = [ ("Application mobile", "./mobile_app.yaml"), ("Logiciel commerçant", "./shopkeeper_app.yaml"), ("Back-end", "./back-end.yaml"), ("Terminal de paiement", "./tpe.yaml"), ("Recherches", "./research.yaml")]

REQUIRED_YAML_KEY = ["title", "groups"]
REQUIRED_GROUPS_YAML_KEY = ["name", "stories"]

OUTFILE_NAME = "cards.md"

TABLE_WIDTH = 15

def normalizeArray(arr: List[List[str]], placeholder: str):
    max_len = 0
    for line in arr:
        if len(line) > max_len:
            max_len = len(line)

    for line in arr:
        line += [placeholder for _ in range(max_len - len(line))]


def createCardTable(table: List[str], title: str, groups: List[Dict[str, Union[str, List[Dict[str, str]]]]]) -> List[str]:
    col_number = len(groups)
    col_width = TABLE_WIDTH / col_number

    table.append(f'\\begin{{longtable}}{{{"".join([f"p{{{col_width}cm}}" for _ in range(col_number)])}}}')
    table.append(f'\\caption{{Carte {title}}} \\\\')
    table.append("\\rowcolor{cardcolor}")
    table.append(f"\\multicolumn{{{col_number}}}{{c}}{{{title}}} \\\\")
    table.append(f"\\multicolumn{{{col_number}}}{{c}}{{}} \\\\")

    for column in groups:
        if not all(map(lambda key: key in column, REQUIRED_GROUPS_YAML_KEY)):
            print(f"Missing key in group. Required group's keys are: {REQUIRED_GROUPS_YAML_KEY}", file=stderr)
            exit(1)

    # sorry + not type safe lol
    final_table = [[f'\\cellcolor{{cardcolor}}{{{column["name"]}}}', *[f'\\cellcolor{{{story["state"]}}}{{{story["name"]}}}' for story in column["stories"]]] for column in groups]
    normalizeArray(final_table, '')

    # rotate 90° clock wise with hourglass pattern for chad
    final_table = [list(reversed(col)) for col in zip(*reversed(final_table))]

    table.append(f'{" & ".join(final_table[0])} \\\\ \\endfirsthead')
    table.append(f'\\multicolumn{{{col_number}}}{{c}} {{\\bfseries \\tablename \\thetable{{}} -- continued from previous page}} \\\\')
    table.append(f'{" & ".join(final_table[0])} \\\\ \\hline \\endhead')
    table.append(f'\\rowcolor{{white}} \\multicolumn{{{col_number}}}{{c}}{{\\bfseries Continue on next page}} \\\\ \\endfoot \\endlastfoot')

    for row in final_table[1:]:
        table.append(f'{" & ".join(row)} \\\\')
    table.append("\\end{longtable}")

    return table


def yamlToLatex(file_path: str) -> str:
    table = []

    with open(file_path, "r") as stream:
        content: dict = yaml.safe_load(stream)
    if all(map(lambda key: key in content, REQUIRED_YAML_KEY)):
        return "\n".join(createCardTable(table, content["title"], content["groups"]))
    else:
        print(f"Missing key in {file_path}. Required keys are: {REQUIRED_YAML_KEY}", file=stderr)
        exit(1)


def compile():
    outfile = []

    for (file_name, file_path) in FILES:
        outfile.append(f"## {file_name}\n")
        try:
            outfile.append(yamlToLatex(file_path))
        except yaml.YAMLError as e:
            print(e, file=stderr)
            exit(1)

    outfile.append('\n')
    with open(OUTFILE_NAME, 'w') as file:
        file.write('\n'.join(outfile))


if __name__ == "__main__":
    compile()
