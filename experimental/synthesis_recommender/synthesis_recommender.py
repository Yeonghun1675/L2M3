import openai
import json
from typing import List, Dict, Any
from omegaconf import OmegaConf


config = OmegaConf.load("config.yaml")
openai.api_key = config.openai_api_key


SYSTEM_PROMPT = """You act like a MOF synthesis expert. I will give you precursors of MOF and you have to suggest the appropriate synthesis conditions for this MOF. You have to suggest the synthesis conditions in JSON format and contain these categories : ['precursor', 'synthesis_method', 'solvent', 'temperature', 'time', 'pressure', 'cooling', 'pH_adjustment', 'washing', 'filtration', 'drying']."""


def make_message(precursor: List[str]) -> Dict[str, Any]:
    # if isinstance(precursor, str):
    #    precursor = json.loads(precursor)

    message = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": precursor},
    ]
    return message


def get_answers(model: str, message: List[Dict[str, str]], temperature=0.0) -> tuple:
    completion = openai.ChatCompletion.create(
        model=model, messages=message, temperature=temperature
    )
    prediction = json.loads(completion.choices[0].message["content"])
    # true = json.loads(message["messages"][2]["content"])

    return prediction


def main(question, config: OmegaConf):
    ft_model = config.fine_tuned_model
    temperature = config.temperature
    input_as_text = config.input_as_text
    llm_model = config.llm_model

    if input_as_text:
        raise NotImplementedError("input_as_text: This function is not implemented now")
    else:
        pass

    message = make_message(question)
    prediction = get_answers(ft_model, message, temperature=temperature)

    if config.output_as_text:
        raise NotImplementedError(
            "output_as_text: This function is not implemented now"
        )
    return prediction


if __name__ == "__main__":
    if config.input_as_text:
        question = input("Question: ")
    else:
        question = input("Precursor list: ")
    prediction = main(question, config)
    print(prediction)
