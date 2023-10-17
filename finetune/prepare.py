import json
from llm_miner.synthesis.prompt import FT_TYPE as syn_include_prompt
from llm_miner.text.prompt import FT_TYPE as prop_include_prompt
from llm_miner.categorize.prompt import FT_CATEGORIZE as categorize_prompt
from llm_miner.table.categorize.prompt import FT_CATEGORIZE as table_categorize_prompt
from llm_miner.table.crystal.prompt import FT_TYPE as table_cry_include_prompt
from llm_miner.table.property.prompt import FT_TYPE as table_prop_include_prompt


class FT:
    def __init__(self):
        pass

    @staticmethod
    def jsonl2dict(filepath):
        total = {}
        with open(filepath, 'r') as f:
            for line in f.readlines():
                tmp = json.loads(line)
                k, v = None, None
                for item in tmp['messages']:
                    if item['role'] == 'user':
                        k = item['content']
                    elif item['role'] == 'assistant':
                        v = item['content']
                if k and v:
                    total[k.strip()] = v.strip()
        return total

    @staticmethod
    def dict2jsonl(dict_, outpath, type=None):
        matching_dict = {
            "property inclusion": prop_include_prompt,
            "synthesis inclusion": syn_include_prompt,
            "text categorize": categorize_prompt,
            "table categorize": table_categorize_prompt,
            "table property inclusion": table_prop_include_prompt,
            "table crystal inclusion": table_cry_include_prompt
        }

        if type not in list(matching_dict.keys()):
            print(f"type must be one of {list(matching_dict.keys())}")
            raise KeyError

        total = []
        for k, v in dict_.items():
            if not isinstance(v, str):
                v = str(v)

            system = {
                "role": "system",
                "content": matching_dict[type].strip(),
            }
            user = {
                "role": "user",
                "content": k.strip(),
            }
            assistant = {
                "role": "assistant",
                "content": v.strip(),
            }

            tmp = {}
            tmp["messages"] = [system, user, assistant]
            total.append(tmp)

        for item in total:
            with open(outpath, 'a') as f:
                json.dump(item, f)
                f.write("\n")
