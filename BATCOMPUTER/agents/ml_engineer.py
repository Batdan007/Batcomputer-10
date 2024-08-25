
# Remove the import statement since ML_Engineer is already defined in the same file
ML_ENGINEER_PROMPT = "DEFAULT"  # Replace with your desired prompt

class ML_Engineer:
    def __init__(self, llm) -> None:
        self.ai_prefix = "BATCOMPUTER: "
        self.user_prefix = "BATDAN: "
        self.ml_engineer_prompt = ML_ENGINEER_PROMPT
        self.llm = llm
        self.role = "BATCOMPUTER as Engineer 🤖🧠"

    def think(self, query):
        CURRENT_WORKING_AGENT = []
        AGENT_THOUGHTS = []
        QA_ENGINEER_FEEDBACK = []

        CURRENT_WORKING_AGENT.append(str(self.role))
        # print(QA_ENGINEER_FEEDBACK)
        template = (
            "[INST]"
            + self.user_prefix
            + self.ml_engineer_prompt
            + self.ai_prefix
            + "[/INST]"
        )
        prompt = PromptTemplate(
            template=template, input_variables=["question", "thoughts", "feedback"]
        )

        llm_chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
        )

        res = llm_chain.invoke(
            {
                "question": query,
                "thoughts": AGENT_THOUGHTS,
                "feedback": QA_ENGINEER_FEEDBACK,
            }
        )

        AGENT_THOUGHTS.append(res["text"])

        return res["text"]
