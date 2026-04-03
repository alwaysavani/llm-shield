from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

class LLMMasker:
    def __init__(self):
        # Initialize Presidio Analyzer and Anonymizer
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def mask(self, text: str):
        """
        Detects PII in the given text and replaces it with descriptive placeholders.
        """
        # Analyze the text for PII
        results = self.analyzer.analyze(text=text, entities=None, language='en')

        # Create an encryption operator (if de-masking was needed, we'd use this)
        # For now, we'll just use standard masking with placeholders.
        operators = {
            "DEFAULT": OperatorConfig("replace", {"new_value": "<MASKED>"})
        }

        # Anonymize the text
        anonymized_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )

        return {
            "masked_text": anonymized_result.text,
            "entities": [res.entity_type for res in results]
        }

# Example usage:
# masker = LLMMasker()
# print(masker.mask("My name is John and my phone is 555-0199"))
