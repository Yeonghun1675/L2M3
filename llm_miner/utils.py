import regex
import requests
import tiktoken


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_journal(doi):
        if doi.startswith("https"):
            url = doi
        elif doi.startswith("doi.org"):
            url = f'https://{doi}'
        else:
            url = f'https://doi.org/{doi}'

        try:
            response = requests.get(url, timeout=60)
        except Exception:
            data = ''
            journal = ''
        else:
            data = response.url
            regex_journal = regex.search(
                r'(acs|rsc|elsevier|sciencedirect|wiley|springer|nature)',
                data
            )
            if regex_journal:
                journal = regex_journal.group()
            else:
                journal = ''
        return journal, data

    @staticmethod
    def num_tokens_from_string(string, model="gpt-4"):
        encoding = tiktoken.encoding_for_model(model)
        num_tokens = len(encoding.encode(string))
        return num_tokens


#################################################################
# Main Code Line
#################################################################
def main():
    pass


if __name__ == "__main__":
    main()


# End of Code
# K̲A̲I̲S̲T̲ M̲O̲L̲S̲I̲M̲
