from deepeval.test_case import LLMTestCase

test_cases_to_evaluate = [
    LLMTestCase(
        input="I'm on an F-1 visa, how long can I stay in the US after graduation?",
        actual_output="You can stay up to 30 days after completing your degree.",
        expected_output="You can stay up to 60 days after completing your degree.",
        retrieval_context=[
            """If you are in the U.S. on an F-1 visa, you are allowed to stay for 60 days after completing
            your degree, unless you have applied for and been approved to participate in OPT."""
        ],
    ),
    LLMTestCase(
        input="What are the requirements for a student visa?",
        actual_output="You need a valid passport and an I-20 form.",
        expected_output="You need a valid passport, an I-20 form, proof of financial support, and a completed DS-160 form.",
        retrieval_context=[
            """To obtain a student visa, you must have a valid passport, an I-20 form from your school,
            proof of financial support, and a completed DS-160 form."""
        ],
    ),
]
