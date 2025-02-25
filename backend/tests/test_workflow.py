import unittest

from langchain_core.messages import HumanMessage, SystemMessage

from app.workflows import chain
from dotenv import load_dotenv


load_dotenv("./app/.env")

class TestWorkflow(unittest.TestCase):
    """ test consistency in graph state """
    def setUp(self) -> None:
        """ test fixtures """
        self.messages = [
            SystemMessage("You are an Assistant"),
            HumanMessage("hi i am prateek")
        ]
        self.workflow = chain()

    def test_return_as_state(self) -> None:
        """ sanity check: for graph state mutations """
        param = { "messages": self.messages }
        type_param = type(param)
        self.assertIsInstance(self.workflow.invoke(param), type_param)

if __name__ == "__main__":
    import os
    os.getenv("OPENAI_API_KEY")
    unittest.main()
