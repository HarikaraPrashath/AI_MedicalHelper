from langchain.prompts import PromptTemplate

template = "Say hello to {name}"
prompt = PromptTemplate.from_template(template)

print(prompt.format(name="AI"))
