import json
from flask import Flask, render_template, Response, request
from flask_cors import CORS

from models import ProblemEncoder, ProblemSet, ProblemUpdateRequest
from repository import dump, read

data_file_path = "./problem_list.pickle"
problemSet: ProblemSet = read(data_file_path)
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
cors = CORS(app)


@app.route('/')
def homepage():
    return render_template(
        "main.html",
        problems=problemSet.get_sorted_problems(),
        leetcode_url="https://leetcode.com/problems",
        server_url="http://127.0.0.1:5000",
        statistic=problemSet.get_statistic(),
    )
@app.route('/health', methods=['GET'])
def health():
    return Response("OK", status=200)


@app.route('/problems', methods=['GET'])
def get_problems():
    return Response(json.dumps(problemSet.get_sorted_problems(), cls=ProblemEncoder), status=200, content_type='application/json')


@app.route('/problems/update', methods=['POST'])
def update_problems():
    try:
        requestBodyJson = request.get_json()
        requestBody: ProblemUpdateRequest = ProblemUpdateRequest(
            problem_id=int(requestBodyJson['problem_id']),
            status=1 if requestBodyJson['status'] else 0
        )
        problemSet.problems[requestBody.problem_id].status = requestBody.status
        dump(data_file_path, problemSet)
        return Response(str(requestBody.problem_id), mimetype='text/xml')

    except Exception as e:
        return Response("Invalid request body" + str(e), status=400)


if __name__ == "__main__":
    app.run()
