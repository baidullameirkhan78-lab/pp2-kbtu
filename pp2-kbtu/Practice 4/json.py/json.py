# json.py

import json


def demo_loads_dumps():
    json_string = '{"name": "Ali", "age": 18, "city": "Almaty"}'

    data = json.loads(json_string)
    print("Name:", data["name"])

    json_output = json.dumps(data, indent=2)
    print("JSON output:")
    print(json_output)


def write_json_file():
    data = {
        "country": "Kazakhstan",
        "capital": "Astana",
        "population": 20000000
    }

    with open("example.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def read_json_file():
    with open("example.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print("Read from file:", data)


if __name__ == "__main__":
    demo_loads_dumps()
    write_json_file()
    read_json_file()
