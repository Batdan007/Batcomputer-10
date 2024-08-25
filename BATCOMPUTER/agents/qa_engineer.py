import string

# pip install llmimport
from settings.agent_prompt import QA_ENGINEER_PROMPT
from settings.config import (
    AGENT_THOUGHTS,
    CURRENT_WORKING_AGENT,
    QA_ENGINEER_FEEDBACK)

from llm.moderation import PromptTemplate, LLMChain
from settings.agent_prompt import QA_ENGINEER_PROMPT
from settings.config import (
    AGENT_THOUGHTS,
    CURRENT_WORKING_AGENT,
    QA_ENGINEER_FEEDBACK)

class QA_Engineer:
    def __init__(self, llm) -> None:
        self.qa_engineer_prompt = QA_ENGINEER_PROMPT
        self.ai_prefix = "Batcomputer: "
        self.user_prefix = "Batdan: "
        self.llm = llm
        self.agent_thoughts = AGENT_THOUGHTS
        self.role = "QA Engineer 🤖🔎"


    def analyse(self, query):
        global CURRENT_WORKING_AGENT, QA_ENGINEER_FEEDBACK
        CURRENT_WORKING_AGENT = []
        CURRENT_WORKING_AGENT.append(str(self.role))

        validation_prompt = PromptTemplate(
            template=self.qa_engineer_prompt,
            input_variables=["question", "latest_thought"],
        )

        self.moderator = LLMChain(
            llm=self.llm,
            prompt=validation_prompt,
        )
        # print(self.agent_thoughts)
        validate = self.moderator.invoke(
             {
                "question": query,
                "latest_thought": self.agent_thoughts[-1],
            }
        )

        if ("CORRECT" in validate["text"] or "TERMINATE" in validate["text"]) and (
            "CORRECT BUT NOT SOLVED" not in validate["text"].strip(string.punctuation)
            or "INCORRECT AND NOT SOLVED"
            not in validate["text"].strip(string.punctuation)
        ):
            self.parse_code(self.agent_thoughts[-1])
            return True
        else:
            # print("INCORRECT")
            QA_ENGINEER_FEEDBACK.append(validate["text"])
            return False
