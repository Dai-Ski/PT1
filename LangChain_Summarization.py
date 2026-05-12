from langchain_community.llms import Cohere
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
text = TextLoader("sample_text.txt").load()[0].page_content
prompt = PromptTemplate(input_variables=["text"], template="Summarize:\n{text}")
llm = Cohere(cohere_api_key="YOUR_API_KEY", temperature=0.7)
summary = LLMChain(llm=llm, prompt=prompt).run(text=text)
print(summary)
