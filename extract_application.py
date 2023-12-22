from collections import defaultdict
import logging
import json
import os
import sys
from pathlib import Path
import pickle
import random
from tqdm import tqdm

from llm_miner import LLMMiner
from llm_miner.pricing import TokenChecker
from llm_miner.reader import JournalReader
from llm_miner.config import config, config2, config3, config4, config5, config6


#################################################################
# Logger
#################################################################
def get_logger(file_name):
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
    )

    file_handler = logging.FileHandler(f"{file_name}_application.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


api_key_dict = {
    "1": "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",
    "2": "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",
    "3": "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",
    "4": "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",
    "5": "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",
    "6": "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",
    # "12": "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",
}

config_dict = {
    "1": config,
    "2": config2,
    "3": config3,
    "4": config4,
    "5": config5,
    "6": config6,
}


def run(publisher="ACS", config_num="1"):
    cl = get_logger(f"{publisher}_{config_num}")
    extension = "XML"
    if publisher == "RSC":
        extension = "HTML"

    files = sorted(list(Path("../L2M3_data/1_application_papers/elsevier_xml/").glob(f"*.{extension.lower()}")))
    outfolder = Path("/home/users/ws1715/Projects/L2M3/application_elsevier_results/")

    for filepath in tqdm(files[9000:12000]):
        cl.info(f"working on {filepath.stem}")
        outpath = outfolder / Path(str(filepath.stem) + ".json")
        outpickle = outfolder / Path(str(filepath.stem) + ".pickle")
        if outpath.exists() or outpickle.exists():
            cl.info(f"{filepath.stem} already done")
            continue

        isbreak = False

        agent = LLMMiner.from_config(config_dict[config_num], openai_api_key=api_key_dict[config_num])
        tc = TokenChecker()

        try:
            output = JournalReader.from_file(filepath, f'{publisher}'.lower())
            agent.run(
                paragraph=output,
                token_checker=tc,
            )
        except Exception as e:
            cl.error(f"{filepath.stem} - {str(e)}")
            continue

        for element in output.cln_elements:
            if "exceeded your current quota" in str(element.data):
                isbreak = True

        try:
            output.to_json(outpath)
            cl.info(f"{filepath.stem} succeeded")

        except Exception as e:
            with open(outpickle, 'wb') as f_pickle:
                pickle.dump(output, f_pickle)
            cl.error(f"{filepath.stem} - {str(e)}")

        finally:
            out_tc = outfolder / Path(str(filepath.stem) + ".tc")
            with open(out_tc, 'wb') as f:
                pickle.dump(tc, f)

        if isbreak:
            cl.error("Exceeded current quota")
            break
    cl.info("Finished")


run(publisher=str(sys.argv[1]), config_num=str(sys.argv[2]))
