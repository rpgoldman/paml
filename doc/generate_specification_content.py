import glob

from sbol_factory import UMLFactory
import os
from shutil import copy
from pathlib import Path

print('Warning: this script is fragile and assumes that PAML and PAML-specification are sibling directories on Mac or Unix.')

dirname = os.path.dirname(__file__)

# UML Spec
UML_TTL = os.path.join(dirname, '../uml/uml.ttl')
UML_NAMESPACE = 'http://bioprotocols.org/uml#'

# PAML Spec
PAML_TTL = os.path.join(dirname, '../paml/paml.ttl')
PAML_NAMESPACE = 'http://bioprotocols.org/paml#'

# Output location
SPEC_OUT = os.path.join(dirname, "../PAML-specification")


def generate_spec(spec_file,
                  spec_name,
                  spec_namespace):

    print(f'Loading {spec_name}')
    module = UMLFactory(os.path.join(os.path.dirname(os.path.realpath(__file__)), spec_file), spec_namespace)

    print(f'Generating {spec_name} specification materials')
    module.generate(f'{spec_name}_classes')

    print(f'Moving {spec_name} to specification folder')
    if not os.path.exists(SPEC_OUT):
        os.mkdir(SPEC_OUT)
    copy(f'{spec_name}DataModel.tex', os.path.join(SPEC_OUT, f'{spec_name}DataModel.tex'))
    os.remove(f'{spec_name}DataModel.tex')
    Path(os.path.join(SPEC_OUT, f'{spec_name}_classes/')).mkdir(parents=True, exist_ok=True)
    for file in glob.glob(f'{spec_name}_classes/*'):
        copy(file, os.path.join(SPEC_OUT, f'{spec_name}_classes/'))
        os.remove(file)
    os.rmdir(f"{spec_name}_classes")

def generate_specs():
    generate_spec(UML_TTL, "uml", UML_NAMESPACE)
    generate_spec(PAML_TTL, "paml", PAML_NAMESPACE)
    print('Update complete')

if __name__ == '__main__':
    generate_specs()
