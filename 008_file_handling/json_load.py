import json

file_ko_path = "/Users/nehishahirachan/Desktop/python-class/.vscode/extensions.json"
with open(file_ko_path, "r") as fp:
    # content = json.load(fp)
    # print(content["recommendations"][0])

    text_ko_content = fp.read()
    content_ko_dictionary = json.loads(text_ko_content)
    print(content_ko_dictionary["recommendations"][0])


