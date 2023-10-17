from flask import Flask, request, render_template
from datetime import datetime
import os
import pdb  # Import the pdb module

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    answers = request.form.getlist("answer[]")

    # Basic validation: Check if answers are provided
    if not answers:
        print("Please provide answers.")
        pdb.set_trace()  # Set a breakpoint here

    # Generate a timestamp for the file name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"results_{timestamp}.txt"

    try:
        # Define an absolute file path
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "results")

        # Save the answers to the file
        with open(os.path.join(file_path, file_name), "w") as file:
            for a in answers:
                file.write(f"Answer: {a}\n")
                file.write("\n")
        print(f"Answers saved to file: {file_name}")
    except Exception as e:
        app.logger.error(f"Error while saving results: {str(e)}")
        print(
            f"An error occurred while saving results. Please check the logs for details."
        )

    return "Results saved successfully!"


if __name__ == "__main__":
    app.run(debug=True)
