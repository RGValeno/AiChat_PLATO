# import packages
import os
import sys
import langchain_openai
import yaml
import warnings
import constants

# Import the necessary modules
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings

# Load the document
#doc = '1497.txt'
doc = constants.doc

# Filter out LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

# Load OpenAI API key
OpenAi_CONFIG_FILE = constants.config

# Load the config file
with open(OpenAi_CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.Loader)

print(type(config))

# Set the OpenAI API key
OPENAI_API_KEY = config['OpenAi']['key']
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Load the query
query = sys.argv[1]
print(query)

# Create an index from the document
loader = TextLoader(doc)
index = VectorstoreIndexCreator().from_loaders([loader])

# Load multiple documents from a directory
#loader = DirectoryLoader('../', glob="**/*.md", show_progress=True)
#docs = loader.load()

# Query the index
print(index.query(query))