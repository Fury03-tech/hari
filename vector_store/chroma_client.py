import os
import chromadb
from chromadb.config import Settings


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

CHROMA_DB_PATH = os.path.join(PROJECT_ROOT, "chroma_db")

_client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DB_PATH,
        anonymized_telemetry=False
    )
)


def get_collection():
    return _client.get_or_create_collection(
        name="atlas_documents"
    )
