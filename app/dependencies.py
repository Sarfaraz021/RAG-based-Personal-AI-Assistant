# # dependencies.py
# from .rag_assistant import RAGAssistant

# # Creating a singleton instance of RAGAssistant to be used across the application
# # This is to ensure that only one instance exists during the lifecycle of the application

# assistant_instance = None


# def get_rag_assistant() -> RAGAssistant:
#     """
#     This function returns a singleton instance of the RAGAssistant.
#     If the instance does not exist, it initializes one.

#     Returns:
#         RAGAssistant: A singleton instance of the RAGAssistant class.
#     """
#     global assistant_instance
#     if assistant_instance is None:
#         assistant_instance = RAGAssistant()
#     return assistant_instance
