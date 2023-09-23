config = {
    # default llms
    "model_name": "gpt-4",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::80Qa4CA7',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::81XcMVpc',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:molsimllm::80Qd6Ylb',
        'ft_text_synthesis_extract': None,
        'ft_table_convert': 'ft:gpt-3.5-turbo-0613:molsimllm::80ONu8vL',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::80nXElRv',
        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:molsimllm::81ALrhlf',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::81pfyxT4',
    },

    # llm options
    "temperature": 0.0,
    "verbose": False,   

    # config - agent
    'reconstruct': True,  # merge paragraph for reducing tokens
    'input_max_tokens_synthesis': None,
    'input_max_tokens_property': 3500,

}
