import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from diagrams import Diagram
from diagrams.custom import Custom
import re

# Set your OpenAI key
os.environ["apikey"] = "yourapikey"

# Define expected output schema
response_schemas = [
    ResponseSchema(name="summary", description="Brief summary of what the stored procedure does."),
    ResponseSchema(name="technical_requirements", description="Technical details like input/output, DB tables used, indexes, etc."),
    ResponseSchema(name="functional_requirements", description="Functional requirements - what the stored procedure is meant to accomplish."),
    ResponseSchema(name="steps", description="List of steps performed inside the stored procedure."),
]

# Initialize output parser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Build prompt
prompt = PromptTemplate(
    template="""
You are an expert data engineer and technical analyst.

Given the following SQL stored procedure, analyze and provide the following:
1. Summary
2. Technical Requirements
3. Functional Requirements
4. List of steps in simple bullet points

Stored Procedure:

{format_instructions}
""",
    input_variables=["stored_proc"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

# ---- 3. LangChain LLMChain ----
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)


# ---- 4. Main Function to Analyze SQL ----
def analyze_stored_procedure(sql_text: str) -> dict:
    result = chain.run({"stored_proc": sql_text})
    parsed_result = output_parser.parse(result)
    return parsed_result


# ---- 5. Optional: Generate Flowchart from Steps ----
def generate_flowchart(steps: str, filename="flowchart.png"):
    # Clean bullet points
    step_list = re.split(r"[\n•\-]+", steps.strip())
    step_list = [s.strip() for s in step_list if s.strip()]

    if not step_list:
        return

    with Diagram("Procedure Flowchart", filename=filename, show=False, direction="TB"):
        prev_node = Custom(step_list[0], "./box.png")
        for step in step_list[1:]:
            curr_node = Custom(step, "./box.png")
            prev_node >> curr_node
            prev_node = curr_node
