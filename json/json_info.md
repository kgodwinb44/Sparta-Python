# JSON

## JavaScript Object Notation
- Lightweight data-interchange format
- Used to store and transport data
- It is a plain text format which allows for easy interchange between programming languages

### JSON Module Functions in Python

- **`json.load(fp)`**  
  Reads JSON data from a file-like object (`fp`) and returns a Python object.  
  _Example_: `data = json.load(open('data.json'))`

- **`json.loads(s)`**  
  Parses a JSON-formatted string (`s`) and returns a Python object.  
  _Example_: `data = json.loads('{"name": "Alice"}')`

- **`json.dump(obj, fp)`**  
  Serializes a Python object (`obj`) and writes it to a file-like object (`fp`) in JSON format.  
  _Example_: `json.dump(data, open('data.json', 'w'))`

- **`json.dumps(obj)`**  
  Serializes a Python object (`obj`) to a JSON-formatted string.  
  _Example_: `json_str = json.dumps({'name': 'Alice'})`