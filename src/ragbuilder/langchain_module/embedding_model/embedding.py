from ragbuilder.langchain_module.common import setup_logging
import logging
from langchain_openai import OpenAIEmbeddings
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
# Set up logging
setup_logging()
logger = logging.getLogger("ragbuilder")

def getEmbedding(**kwargs):
    try:

        # Ensure 'embedding_model' key exists in kwargs
        if 'embedding_model' not in kwargs:
            raise KeyError("The key 'embedding_model' is missing from the arguments.")
        
        embedding_model = kwargs['embedding_model']
        model_owner= embedding_model.split(":")[0]
        model= embedding_model.split(":")[1]
        # Validate the embedding model type
        if not isinstance(embedding_model, str):
            raise TypeError("The 'embedding_model' must be a string.")
        
        logger.info("getEmbedding Invoked")
        
        if model_owner == "OpenAI":
            logger.info(f"OpenAIEmbeddings Invoked: {embedding_model}")
            code_string= f"""embedding=OpenAIEmbeddings(model='{model}')"""
            import_string = f"""from langchain_openai import OpenAIEmbeddings"""
            return {'code_string':code_string,'import_string':import_string}
        elif model_owner == "Mistral":
            logger.info(f"MistralAIEmbeddings Invoked: {embedding_model}")
            code_string= f"""embedding=MistralAIEmbeddings(api_key=os.environ.get("MISTRAL_API_KEY"))"""
            import_string = f"""from langchain_mistralai import MistralAIEmbeddings"""
            return {'code_string':code_string,'import_string':import_string}
        elif model_owner == "HF":
            logger.info(f"HuggingFaceInferenceAPIEmbeddings Invoked: {embedding_model}")
            code_string= f"""embedding=HuggingFaceInferenceAPIEmbeddings(api_key=os.environ.get("HUGGINGFACEHUB_API_TOKEN"), model_name="{model}")"""
            import_string = f"""from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings"""
            return {'code_string':code_string,'import_string':import_string}
        else:
            raise ValueError(f"Invalid LLM: {embedding_model}")
    except KeyError as ke:
        logger.error(f"Key Error: {ke}")
        raise
    except TypeError as te:
        logger.error(f"Type Error: {te}")
        raise
    except ValueError as ve:
        logger.error(f"Value Error: {ve}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise