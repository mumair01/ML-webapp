# Standard imports
# Local imports
from app import App as ODQAAPI
# Third party imports
from flask import Flask, request, jsonify
from flask_cors import CORS

# ------------- Instantiations
app = Flask(__name__)
api = ODQAAPI()
# Adding all models to the API
api.register_model("distilbert-base-cased-distilled-squad",
                   ["question-answering"],
                   {"model_name": "distilbert-base-cased-distilled-squad",
                    "task": "question-answering"})


# ------------- Routes


@app.route('/execute', methods=['POST'])
def execute_model():
    try:
        kwargs = request.get_json()
        if not all(k in kwargs for k in ['model_name', 'task', 'execute_kwargs']):
            return {}, 404

        return {
            "output": api.execute_model(**kwargs)}, 200
    except Exception as e:
        return repr(e), 500


@app.route('/get_model_tasks', methods=['GET'])
def get_model_tasks():
    try:
        model_name = request.args.get('model_name')
        return {"tasks": api.get_model_tasks(model_name)}, 200
    except Exception as e:
        return repr(e), 500


@app.route('/get_models_for_task', methods=['GET'])
def get_models_for_task():
    try:
        task = request.args.get('task')
        return {task: api.get_models_for_task(task)}, 200
    except Exception as e:
        return repr(e), 500


@app.route('/get_models_by_task', methods=['GET'])
def get_models_by_task():
    try:
        return api.get_models_by_task(), 200
    except Exception as e:
        return repr(e), 500


# TODO: Switch to using flask run command from CLI later.
if __name__ == "__main__":
    app.run(debug=True)
