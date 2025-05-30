from rest_framework.utils.serializer_helpers import ReturnList



def get_first_error(serialized_errors):
    default_message = "UNSUCCESSFUL"
    if not serialized_errors:
        return default_message
    try:
        serialized_error_dict = serialized_errors
        # ReturnList of serialized_errors when many=True on serializer
        if isinstance(serialized_errors, ReturnList):
            serialized_error_dict = serialized_errors[0]
        serialized_errors_keys = list(serialized_error_dict.keys())
        # getting first error message from serializer errors
        try:
            message = serialized_error_dict[serialized_errors_keys[0]][0].replace("This", serialized_errors_keys[0])
            return message
        except:
            return serialized_error_dict[serialized_errors_keys[0]][0]
    except Exception as e:
        # logger.error(f"Error parsing serializer errors:{e}")
        return default_message