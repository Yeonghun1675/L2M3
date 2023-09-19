from llm_miner.parser.base import Metadata, BaseParser
from llm_miner.parser.elsevier import ElsevierParser
from llm_miner.parser.acs import ACSParser
from llm_miner.parser.rsc import RSCParser
from llm_miner.parser.springer import SpringerParser

parser_dict = {
    'elsevier': ElsevierParser,
    'acs': ACSParser,
    'rsc': RSCParser,
    'springer': SpringerParser,
}