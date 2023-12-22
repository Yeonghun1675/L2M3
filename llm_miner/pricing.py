from pydantic import BaseModel
from typing import Dict, Literal, Any

from langchain.chains import LLMChain

from llm_miner.utils import num_tokens_from_string


PRICES = {
    'gpt-4': {'input':0.03, 'output':0.06},
    'gpt-4-1106-preview': {'input': 0.01, 'output': 0.03},
    'gpt-3.5-turbo': {'input':0.0015, 'output':0.002},
    'gpt-3.5-turbo-16k': {'input':0.003, 'output':0.004},
    'davinci-002': {'input':0.002, 'output':0.002},
    'babbage-002': {'input':0.0004, 'output':0.0004},
    'ft:gpt-3.5-turbo': {'input': 0.012, 'output': 0.016},
    'ft:davinci': {'input': 0.012, 'output': 0.012},
    'ft:babbage': {'input': 0.0016, 'output': 0.0016},
}


class Step(BaseModel):
    name_step: str
    name_model: str
    type: Literal['input', 'output']
    tokens: int = 0
    number: int = 0

    def clear_tokens(self) -> None:
        self.tokens = 0
        self.number = 0

    def update_token(self, n_tokens: int) -> None:
        self.tokens += n_tokens
        self.number += 1

    @property
    def price(self) -> float:
        pricing = self.tokens * PRICES[self.name_model][self.type] / 1000
        return pricing


class TokenChecker(BaseModel):
    steps: Dict[str, Step] = dict()

    def set_step(self, name_step: str, name_model: str) -> None:
        if name_step.startswith('input-'):
            type = 'input'
            s_name_step = name_step.replace('input-', '')
        elif name_step.startswith('output-'):
            type = 'output'
            s_name_step = name_step.replace('output-', '')
        else:
            raise ValueError(f'`name_step` must start with `input-` or `output-`, not {name_step}')

        step = Step(name_step=s_name_step, name_model=name_model, type=type)
        self.steps[name_step] = step

    def update_token(self, text: str, name_step: str, name_model: str) -> None:
        if name_step not in self.steps:
            self.set_step(name_step, name_model)
        
        n_tokens = num_tokens_from_string(text, name_model)
        self.steps[name_step].update_token(n_tokens)

    def clear(self) -> None:
        self.steps.clear()

    def print(self) -> None:
        for step in self.steps.values():
            print(f'{step.name_step} ({step.type}) : {step.tokens} tokens (total: {step.number})')

    @property
    def price(self) -> float:
        total_price = 0
        for step in self.steps.values():
            pricing = PRICES[step.name_model][step.type]
            total_price += step.tokens * pricing / 1000
        return total_price
    

def parse_model_name(model_name: str) -> str:
    model_name = str(model_name)
    if model_name.startswith('ft:gpt-3.5-turbo'):
        return 'ft:gpt-3.5-turbo'
    elif model_name.startswith('ft:davinci'):
        return 'ft:davinci'
    elif model_name.startswith('ft:babbage'):
        return 'ft:babbage'
    else:
        return model_name


def update_token_checker(
    name_step: str,
    chain: LLMChain,
    token_checker: TokenChecker, 
    llm_kwargs: Dict[str, Any],
    llm_output: str,
) -> None:
    prompt = chain.prompt.format_prompt(**llm_kwargs).to_string()
    token_checker.update_token(
        text=prompt,
        name_step=f'input-{name_step}',
        name_model=parse_model_name(chain.llm.model_name)
    )
    token_checker.update_token(
        text=llm_output,
        name_step=f'output-{name_step}',
        name_model=parse_model_name(chain.llm.model_name)
    )
