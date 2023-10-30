config = {
    # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8BMh4gKR',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8D1tQHxL',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8BLsb5DT',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwEYYGn',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwI64O2',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwEadtP',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8BLAmQWW',
    },

    # llm options
    "temperature": 0.0,
    "verbose": False,

    # config - agent
    'reconstruct': True,  # merge paragraph for reducing tokens
    'input_max_tokens_synthesis': None,      # max tokens for reconstruct
    'input_max_token_synthesis_type': 3500,  # max tokens for synthesis-type
    'input_max_tokens_property': 3500,       # max tokens for reconstruct

}
