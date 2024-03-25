from flask import Flask, Response
import dicttoxml

app = Flask(__name__)

# Определенный JSON-объект
json_data = {
    "fullname": "George",
    "characteristics": {"sex": "male", "age": 27},
    "skills": ["smart", "strong"],
    "experience": [
        {"position": "developer", "workplace": "netflix", "salary": "7000"},
        {
            "position": "engineer",
            "workplace": "facebook",
            "id_card": 56117,
            "Country": "Scotland",
        },
    ],
}


@app.route("/convert", methods=["GET"])
def convert_json_to_xml():
    # Конвертируем встроенный JSON в XML
    xml_data = dicttoxml.dicttoxml(json_data, custom_root="Person", attr_type=False)

    # Возвращаем XML
    return Response(xml_data, mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
