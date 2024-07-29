# Flask API
## Description
This is a simple Flask API that returns a list of item ids based on a key.

## Usage
To run the API, execute the following command, the demo data is loaded from the `demo.tsv` file.
```sh
python demo.py
```

the API has the following endpoint for demo purposes,
```sh
curl -X POST -H "Content-Type: application/json" -d '{"key": "key1"}' http://127.0.0.1:5000/itemids
{
  "value": [
    1,
    4,
    2,
    8
  ]
}
```
