import pandas as pd
from utils.logger import logger

def enrich_with_llm(df):

    logger.info("Starting AI enrichment")

    def classify(description):

        # simulação chamada LLM
        if "coffee" in description.lower():
            return "beverage"

        return "other"

    df["category"] = df["description"].apply(classify)

    logger.info("AI enrichment completed")

    return df