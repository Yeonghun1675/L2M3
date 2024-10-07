import os
import argparse
import openai


def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as outfile:
        outfile.write(content)


# File upload
def file_upload(jsonl_file):
    print("-- Upload file -------------------------------")
    with open(jsonl_file, "rb") as file:
        response = openai.File.create(file=file, purpose="fine-tune")
    file_id = response["id"]
    print(f"File uploaded successfully with ID: {file_id}")

    return file_id


# Job upload
def job_upload(file_id, model_name):
    print("-- Upload job -------------------------------")
    response = openai.FineTuningJob.create(
        training_file=file_id,
        model=model_name,
        #        hyperparameters={"n_epochs": value,},
    )
    job_id = response["id"]
    print(f"Fine-tuning job created successfully with ID: {job_id}")

    return job_id


# Retrieve_job
def retrieve_job(job_id):
    response = openai.FineTuningJob.list_events(id=job_id, limit=50)
    events = response["data"]
    events.reverse()
    for event in events:
        print(event["message"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--model", default="gpt-3.5-turbo", type=str)
    parser.add_argument("-f", "--file", type=str)
    parser.add_argument("-a", "--api-key")

    args = parser.parse_args()

    openai.api_key = args.api_key
    file_id = file_upload(args.file)
    job_id = job_upload(file_id, args.model)
    retrieve_job(job_id)
    # print(openai.FineTuningJob.retrieve(job_id))
