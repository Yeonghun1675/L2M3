config = {
    # default llms
    "model_name": "gpt-4",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    'ft_text_categorize_model': 'ft:gpt-3.5-turbo-0613:personal::7ycNfB2h',

    # llm options
    "temperature": 0.0,
    "verbose": False,   

    # config - agent
    'reconstruct': True,  # merge paragraph for reducing tokens
    'input_max_tokens_synthesis': None,
    'input_max_tokens_property': 3500,

}
