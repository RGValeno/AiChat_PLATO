import os
import sys
import langchain_openai

import constants

import yaml


from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings

# from langchain_community.document_loaders import TextLoader
# from langchain_community.document_loaders import DirectoryLoader
# from langchain_openai import OpenAIEmbeddings
# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import TextLoader

OpenAi_CONFIG_FILE = 'auth.yaml'

with open(OpenAi_CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.Loader)
    
print(type(config))

OPENAI_API_KEY = config['OpenAi']['key']

#os.environ["OPENAI_API_KEY"] = constants.APIKEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

query = sys.argv[1]
print(query)

loader = TextLoader('sample.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))