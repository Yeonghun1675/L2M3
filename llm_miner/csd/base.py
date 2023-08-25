import warnings

from ccdc import io
from ccdc.io import CrystalWriter
from ccdc.search import TextNumericSearch

from pathlib import Path
from pydantic import BaseModel
import regex
from typing import List

from llm_miner.error import ContextError


class CSDAgent(BaseModel):
    doi: str
    refcodes: List[str]
    data: List[dict]

    @classmethod
    def from_refcode(cls, refcode: str):
        try:
            doi = io.EntryReader('CSD').entry(refcode).publication.doi
        except Exception:
            raise ContextError(f"{refcode} is not searchable in CSD")
        if not doi:
            doi = ""
        refcodes = [refcode]
        
        return cls(
            doi=doi,
            refcodes=refcodes,
            data=[]
        )

    @classmethod
    def from_doi(cls, doi: str):
        text_reader = TextNumericSearch()
        text_reader.add_doi(doi)
        results = text_reader.search()
        refcodes = [item.identifier for item in results]

        return cls(
            doi=doi,
            refcodes=refcodes,
            data=[],
        )
   
    def extract(self):
        self.data = []
        csd_reader = io.EntryReader('CSD')

        for refcode in self.refcodes:
            ref_entry = csd_reader.entry(refcode)

            tmp = {
                "refcode": ref_entry.identifier,
                "ccdc_number": ref_entry.ccdc_number,
                "chemical_name": ref_entry.chemical_name_as_html,
                "synonyms": ref_entry.synonyms_as_html,
                "chemical formula": ref_entry.molecule.formula,
                "spacegroup": ref_entry.crystal.crystal_system,
                "cell lengths": ref_entry.crystal.cell_lengths,
                "cell angles": ref_entry.crystal.cell_angles,
                "density": ref_entry.calculated_density,  # g/cm3
                "cell volume": ref_entry.crystal.cell_volume,
                "color": ref_entry.color,
                "melting point": ref_entry.melting_point,
            }
            self.data.append(tmp)
            self._get_structure(ref_entry)
            self.data = self._parse_out()

    def _get_structure(self, entry):
        folder = Path('./llm_miner/csd/structures/') / Path(self.doi.replace("/", "_"))
        folder.mkdir(parents=True, exist_ok=True)
        filepath = folder / Path(entry.identifier+".cif")
        writer = CrystalWriter(filepath)
        writer.write(entry.molecule)

    def _parse_out(self):
        result = []
        pattern = r'(\d+(\.\d+)?(-\d+(\.\d+)?)?)\s*(K|deg\.?C)?(?=(\s*dec\s*)|\s*)'

        for item in self.data:
            melt_unit = ""
            melt_value = ""
            if not item['melting point']:
                pass
            else:
                melt_p = item['melting point']
                if "K" in melt_p:
                    melt_unit = "K"
                elif "C" in melt_p:
                    melt_unit = "deg.C"
                matches = regex.findall(pattern, str(melt_p))
                melt_value = matches[0][0]

            tmp = {
                'meta': {
                    'name': item['chemical_name'],
                    'symbol': item['synonyms'],
                    'chemical formula': item['chemical formula'],
                },
                "ccdc number": [
                    {
                        "value": item['ccdc_number']
                    }
                ],
                "refcode": [
                    {
                        "value": item['refcode']
                    }
                ],
                "crystal system": [
                    {
                        "value": item['spacegroup']
                    }
                ],
                "lattice parameters": [
                    {
                        'value': {
                            'a': item['cell lengths'].a,
                            'b': item['cell lengths'].b,
                            'c': item['cell lengths'].c,
                            'alpha': item['cell angles'].alpha,
                            'beta': item['cell angles'].beta,
                            'gamma': item['cell angles'].gamma,
                        }
                    },
                ],
                "cell volume": [
                    {
                        'value': item['cell volume'],
                        'unit':"Å^3"
                    },
                ],
                'density': [
                    {
                        'value': item['density'],
                        'unit':"g/cm^3"
                    },
                ],
                'color': [
                    {
                        'value': item['color'],
                    },
                ],
                'melting point': [
                    {
                        'value': melt_value,
                        'unit': melt_unit,
                    },
                ],
            }
            result.append(tmp)
        return result
