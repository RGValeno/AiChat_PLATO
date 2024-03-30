import os
import sys
import langchain_openai
import yaml

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings
import warnings

# Filter out LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

OpenAi_CONFIG_FILE = 'auth.yaml'

with open(OpenAi_CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.Loader)
    
print(type(config))

OPENAI_API_KEY = config['OpenAi']['key']

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

query = sys.argv[1]
print(query)

#loader = DirectoryLoader('../', glob="**/*.md", show_progress=True)
#docs = loader.load()

loader = TextLoader('1497.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))