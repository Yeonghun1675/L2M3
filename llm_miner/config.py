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


config2 = {
    # # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8FGz4Qm5',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8FH8BaJv',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8FGT2QV5',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-0613:molsimllm::8FIKcQ7q',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8FIXDg4T',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8FJCz2id',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8FLN3ElN',
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


config3 = {
    # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FHUASXv',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FHuOS52',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:personal::8FGadJtH',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-0613:personal::8FJX3k4z',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FJa4ruc',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:personal::8FJjmFQL',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FKKRhMv',
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


config4 = {
    # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FIJsMyd',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FI6PBfY',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:personal::8FHRb8Lh',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-0613:personal::8FJQfESh',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FJU0Cda',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:personal::8FJQrcMc',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FJoAUP0',
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


config5 = {
    # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FIOBV3Y',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FIUWRIX',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:personal::8FHXeDWo',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-1106:personal::8IFpaI8e',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-1106:personal::8IG4dqZm',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-1106:personal::8IFvBimG',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:personal::8IXnfOqK',
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


config6 = {
    # default llms
    "model_name": "gpt-4",
    # "model_name": "gpt-3.5-turbo-16k",
    "simple_model_name": "gpt-3.5-turbo-16k",

    # fine-tuned llms (optional)
    "fine_tuning_models": {
        'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:personal::8FIxmEtn',
        'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:personal::8FJCnC1J',
        'ft_text_property_extract': None,
        'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:personal::8FIDDjSH',
        'ft_text_synthesis_extract': None,

        'ft_table_convert': 'ft:gpt-3.5-turbo-1106:personal::8IG6IKfj',
        'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:personal::8IXrdHZc',

        'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:personal::8IXtJ45R',
        'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:personal::8IY01MYa',
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


# config12 = {
#     # default llms
#     "model_name": "gpt-4",
#     # "model_name": "gpt-3.5-turbo-16k",
#     "simple_model_name": "gpt-3.5-turbo-16k",

#     # fine-tuned llms (optional)
#     "fine_tuning_models": {
#         'ft_text_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8BMh4gKR',
#         'ft_text_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8D1tQHxL',
#         'ft_text_property_extract': None,
#         'ft_text_synthesis_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8BLsb5DT',
#         'ft_text_synthesis_extract': None,

#         'ft_table_convert': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwEYYGn',
#         'ft_table_categorize': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwI64O2',

#         'ft_table_crystal_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8AwEadtP',
#         'ft_table_property_type': 'ft:gpt-3.5-turbo-0613:molsimllm::8BLAmQWW',
#     },

#     # llm options
#     "temperature": 0.0,
#     "verbose": False,

#     # config - agent
#     'reconstruct': True,  # merge paragraph for reducing tokens
#     'input_max_tokens_synthesis': None,      # max tokens for reconstruct
#     'input_max_token_synthesis_type': 3500,  # max tokens for synthesis-type
#     'input_max_tokens_property': 3500,       # max tokens for reconstruct
# }
