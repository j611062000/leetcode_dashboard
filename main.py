from flask import Flask, render_template, Response, request
from models import ProblemSet, ProblemUpdateRequest
from repository import dump, read

data_file_path = "./problem_list.pickle"
problemSet: ProblemSet = read(data_file_path)
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template(
        "main.html",
        problems=problemSet.get_sorted_problems(),
        leetcode_url="https://leetcode.com/problems",
        server_url="http://127.0.0.1:5000",
        statistic=problemSet.get_statistic(),
    )


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
        print(requestBodyJson['status'], requestBody.status, problemSet.problems[requestBody.problem_id].status, requestBody.problem_id)
        return Response(str(requestBody.problem_id), mimetype='text/xml')

    except Exception as e:
        return Response("Invalid request body" + str(e), status=400)

   


if __name__ == "__main__":
    app.run()
