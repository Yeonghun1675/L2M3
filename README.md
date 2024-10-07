<div align="center">
<h1> ⛏L2M3: Large Language Models Material Miner </h1> 
</div>

![](./figures/Figures_scheme.jpg)

## Summary
This project focuses on efficiently collecting experimental Metal-Organic Framework (MOF) data from scientific literature to overcome the challenges of accessing elusive data and to improve the quality of information available for machine learning applications in materials science. By leveraging a chain of advanced Large Language Models (LLMs), we developed a systematic approach to extract and organize MOF data into a structured and usable format. Our methodology successfully compiled information from over 40,000 research articles, resulting in a comprehensive, ready-to-use dataset. This dataset includes MOF synthesis conditions and properties, extracted from both **tables and text data**, which were subsequently analyzed. 


## Process

![](./figures/Figures_process.jpg)

Our L2M3 empolys 3 specialized agent:
- **Categorization**: the agent that classifies the table and texts based on whether they describe a property, a synthesis condition, or contain no relevant information.
- **Inclusion**: the agent that determine the specific information present.
- **Extraction**: the agent that extract information as JSON type.

## Installation

**NOTE**: This package is primarily tested on Linux system. We strongly recoomend using Lunux for installation.
**NOTE2**: This package require python >= 3.9

```bash
$ git clone https://github.com/Yeonghun1675/L2M3.git
$ cd L2M3
$ pip install -e .
```

## How to use 

You can run L2M3 using `LLMMiner` and `JournalReader`.
```python
from llm_miner import LLMMiner
from llm_miner import JournalReader

# load agent and parse xml/html file
agent = LLMMiner.from_config(config)
jr = JournalReader.from_file(file_path, publisher)

# run
agent.run(jr)
```

###  1. JournalReader (Parsing XML/HTML)
`JouralReader` is python class that obtain clean text and meta data from xml/html file.

```python
from llm_miner import JournalReader

file_path = 'path-to-your-xml/html-file'
publisher = 'your-publisher'  # list of  publisher: ['acs', 'rsc', 'elsevier', 'springer']

jr = JournalReader.from_file(file_path, publisher=publisher)
```

`JournalReader` has several useful attributes.
- `doi` : doi of paper
- `title` : title of paper
- `url` : url of paper
- `get_tables` : list of tables
- `get_texts` : list of paragraphs
- `get_figures`: list of figure captions

Also, you can write and load `JournalReader` as json type.
```python
# save journal reader
jr.to_json('output_file_path.json')

# load journal reader
jr_load = JournalReader.from_json('input_file_path.json')
```

### 2. LLMMiner (Agent)
LLM miner is LLM Module that extract synthesis and characteristic properties from text and table.

```python
from llm_miner import LLMMiner

api_key = 'openai-api-key'
agent = LLMMiner.create(openai_api_key=api_key)
```
Default llm module is 'gpt-4' for text and 'gpt-3.5-turbo-16k' for table.

Also, you can change llm model using config file. If you want to use fine-tuned mode. Example for config file is in `L2M3/config/`

```python
import yaml

config = yaml.load('config-file')
agent = LLMMiner.from_config(config, openai_api_key=api_key)
```

### 3. Run agent
You can run agent. Output of text-mining is automatically saved in `JournalReader` object.

```python
agent.run(jr)
```

You can check results in `JournalReader`. Each results are list of `Paragraph` object.
```python
# All text-mined results
synthesis_condition = jr.get_synthesis_conditions()
properties = jr.get_properties()
tables = jr.get_tables()
```

You can see results in `Paragraph` object.
```python
# Check results of each paragraph
paragraph = synthesis_condition[index]  # synthesis_condition or properties or table
paragraph.print()  # check all content of paragraph
```

`Paragraph` object has several useful attribute and functions.
- idx : index of paragraph
- type : type of paragraph (text or table)
- classification : result of classification (synthesis condition or properties)
- clean_text : clean version of paragraph (no html/xml tags)
- include_properties : result of inclusion
- data : extracted JSON type data
- (function) to_dict : Convert Paragraph object to dictionary
- (function) get_intermediate_step : Check results of intermediate step


### Token Checker
We provide token checker that estimate tokens and price of your text-mining task.

```python
from llm_miner.pricing import TokenChecker

tc = TokenChecker()
...
agent.run(
    paragraph=output,
    token_checker=tc
)
```

## Fine-tuning
You have to fine tuning to all i want to use.
pass



## Citiation
If you want to cite PMTransformer or MOFTransformer, please refer to the following paper:
- [Harnessing Large Language Model to collect and analyze Metal-organic framework property dataset, arxiv (2024)](https://arxiv.org/abs/2404.13053)

## Contributing 🙌

Contributions are welcome! If you have any suggestions or find any issues, please open an issue or a pull request.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for more information.
