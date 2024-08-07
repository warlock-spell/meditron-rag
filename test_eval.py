from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric,
)

from test_cases import test_cases_to_evaluate

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

contextual_precision = ContextualPrecisionMetric(model="gpt-3.5-turbo")
contextual_recall = ContextualRecallMetric(model="gpt-3.5-turbo")
contextual_relevancy = ContextualRelevancyMetric(model="gpt-3.5-turbo")

from deepeval import evaluate


for test_case in test_cases_to_evaluate:
    contextual_precision.measure(test_case)
    print("Precision Score: ", contextual_precision.score)
    print("Precision Reason: ", contextual_precision.reason)

    contextual_recall.measure(test_case)
    print("Recall Score: ", contextual_recall.score)
    print("Recall Reason: ", contextual_recall.reason)

    contextual_relevancy.measure(test_case)
    print("Relevancy Score: ", contextual_relevancy.score)
    print("Relevancy Reason: ", contextual_relevancy.reason)
