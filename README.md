<div align="center">
<h1> ⛏L2M3: Large Language Models Material Miner </h1> 
</div>

![](./figures/Figures_scheme.jpg)

## Summary
L2M3 is designed to efficiently gather experimental Metal-Organic Framework (MOF) data from scientific literature, addressing the challenge of accessing hard-to-find data and enhancing the quality of information available for machine learning in materials science. By utilizing a chain of advanced Large Language Models (LLMs), we developed a systematic method for extracting and organizing MOF data into a structured, usable format. Our approach has successfully compiled data from over 40,000 research articles, creating a comprehensive, ready-to-use dataset. This dataset includes MOF synthesis conditions and properties, extracted from both **tables and text**, which have been thoroughly analyzed.


## Process

![](./figures/Figures_process.jpg)

L2M3 employs three specialized agents:

- **Categorization Agent**: Classifies tables and text based on whether they describe properties, synthesis conditions, or contain irrelevant information.
- **Inclusion Agent**: Identifies specific pieces of information present in the categorized data.
- **Extraction Agent**: Extracts the relevant information in a structured JSON format.

## Installation

**NOTE**: This package is primarily tested on Linux systems. We strongly recommend using Linux for installation.

**Requirements**: Python >= 3.9

```bash
$ git clone https://github.com/Yeonghun1675/L2M3.git
$ cd L2M3
$ pip install -e .
```

## How to use 

You can run L2M3 using the `LLMMiner` and `JournalReader` classes.
```python
from llm_miner import LLMMiner
from llm_miner import JournalReader

# Load agent and parse XML/HTML file
agent = LLMMiner.from_config(config)
jr = JournalReader.from_file(file_path, publisher)

# Run the agent on the parsed file
agent.run(jr)
```

###  1. JournalReader (Parsing XML/HTML)
`JournalReader` is a Python class that extracts clean text and metadata from XML or HTML files.

```python
from llm_miner import JournalReader

file_path = 'path-to-your-xml/html-file'
publisher = 'your-publisher'  # Available options: ['acs', 'rsc', 'elsevier', 'springer']

jr = JournalReader.from_file(file_path, publisher=publisher)
```

Attributes of `JournalReader`:

- `doi`: The DOI of the paper
- `title`: The title of the paper
- `url`: The URL of the paper
- `get_tables`: A list of tables in the paper
- `get_texts`: A list of paragraphs in the paper
- `get_figures`: A list of figure captions in the paper

You can also save and load `JournalReader` instances as JSON files:
```python
# Save JournalReader to a JSON file
jr.to_json('output_file_path.json')

# Load JournalReader from a JSON file
jr_load = JournalReader.from_json('input_file_path.json')
```

### 2. LLMMiner (Agent)
`LLMMiner` is a module that extracts synthesis conditions and characteristic properties from text and tables.

```python
from llm_miner import LLMMiner

api_key = 'openai-api-key'
agent = LLMMiner.create(openai_api_key=api_key)
```
By default, the LLM module uses `gpt-4` for text extraction and `gpt-3.5-turbo-16k` for table extraction.

You can customize the LLM model using a configuration file. If you want to use a fine-tuned model, an example configuration file is available in the [L2M3/config](config) directory.

```python
agent = LLMMiner.from_yaml('yaml-file-path', openai_api_key=api_key)
```

### 3. Run agent
You can run the agent, and the output of the text-mining process will automatically be saved in the `JournalReader` object.

```python
agent.run(jr)
```

You can check the results in the `JournalReader` object. These results show the synthesized or property data, consolidated by material.

```python
result = jr.result

# View all results
result.print()
```

If `jr.result` exists, it is automatically saved during the process of saving the `JournalReader`. If you want to save just the result separately, you can save the cleaned results using the `to_dict` or `to_json` functions:

```python
# convert dictionary type
output = result.to_dict()

# Save as a JSON file
result.to_json(json_file)
```

If you want to review the text-mining results by paragraph or table, you can use the following functions. Each function returns a list of `Paragraph` objects.

```python
# All text-mined results
all_paragraph = jr.cln_element

# View results by category
synthesis_condition = jr.get_synthesis_conditions()
properties = jr.get_properties()
tables = jr.get_tables()
```

You can inspect the text-mining results in each `Paragraph` object:

```python
# Check the results of each paragraph
paragraph = synthesis_condition[idx]  # Can also use properties, or table
paragraph.print()  # View full content of the paragraph
```

The `Paragraph` object offers several useful attributes and methods:

- `idx`: Index of the paragraph
- `type`: Type of the paragraph (text or table)
- `classification`: Classification result (synthesis condition or properties)
- `clean_text`: Cleaned version of the paragraph (no HTML/XML tags)
- `include_properties`: Inclusion result
- `data`: Extracted data in JSON format
- `(method) get_intermediate_step`: Displays results of intermediate steps
- `(method) to_dict`: Converts the Paragraph object to a dictionary



### 4. (optional) Token Checker
L2M3 provides a token checker to estimate the number of tokens used and the price for your text-mining task.

```python
from llm_miner.pricing import TokenChecker

tc = TokenChecker()
...
agent.run(
    paragraph=output,
    token_checker=tc
)

# View token summary
tc.print()
# Display total price (in $)
print (tc.price)
```

## Fine-tuning
L2M3 allows you to fine-tune the LLM model to reduce token usage and cost. In the [L2M3/finetune](finetune) directory, there are `jsonl` files that serve as datasets for fine-tuning various models. The available fine-tuned datasets include:
- text_categorize
- property_inclusion
- synthesis_inclusion
- table_categorize
- table_crystal_inclusion
- table_property_inclusion
- table_xml2md

You can fine-tune models on the [OpenAI Finetune page](https://platform.openai.com/finetune) (Recommanded).

Alternatively, you can fine-tune the model using the provided script:
```bash
$ python finetune/finetune.py --model model_name --file jsonl_file --api-key your_api_key
```

## Addtional Information
- [L2M3 Database](https://figshare.com/account/items/27187917/edit)
-  [Paper Crawling](./crawling.md)
-  [Synthesis Condition Recommender](./experimental/synthesis_recommender/README.md)
-  [Detail of Machine Learing Models](https://github.com/Taeun8991/L2M3_ML)
-  [Utilizing L2M3 Across Various Domains](https://github.com/Taeun8991/L2M3_application)

## Citiation
If you want to cite L2M3, please refer to the following paper:
> [Harnessing Large Language Model to collect and analyze Metal-organic framework property dataset, J. Am. Chem. Soc. 2025, 147, 5, 3943-3958](https://pubs.acs.org/doi/10.1021/jacs.4c11085)

## Contributing 🙌

Contributions are welcome! If you have any suggestions or find any issues, please open an issue or a pull request.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for more information.
