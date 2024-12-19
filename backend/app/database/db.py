from typing import Dict, Any
import uuid


class SimulatedDataStore:
    """
    A simple in-memory data store simulating a database.
    Data is lost when the application restarts.
    """

    def __init__(self):
        self._saved_results: Dict[str, Any] = {}

    def save_result(self, result: dict) -> str:
        """
        Save a result record into memory and return its generated ID.
        """
        result_id = str(uuid.uuid4())
        self._saved_results[result_id] = result
        return result_id

    def list_results(self) -> list:
        """
        Return a list of all saved results, including their IDs.
        """
        return [{"id": rid, **res} for rid, res in self._saved_results.items()]

    def get_result(self, result_id: str) -> dict:
        """
        Retrieve a single result by its ID.
        """
        return self._saved_results.get(result_id)


DB = SimulatedDataStore()
