from schemas.error import ErrorData, ErrorResponseData
from constants import (INVALID_LENGTH, INVALID_LENGTH_TEXT,
                       INVALID_PARAMETER_COUNT, INVALID_PARAMETERS_COUNT_TEXT,
                       INVALID_TYPE, INVALID_TYPE_TEXT,
                       REQUIRED_FIELD, REQUIRED_FIELD_TEXT,
                       INVALID_PARAMETER_VALUE, INVALID_PARAMETER_VALUE_TEXT)


class ValidationException(Exception):
    def __init__(self, errors: list[ErrorData]):
        self.errors = errors


class ErrorException(Exception):
    def __init__(self, error: ErrorResponseData):
        self.error = error


class RequestValidationException:
    def __init__(self, errors: list, body: dict):
        self.default_errors = errors
        self.body = body
        self.data_errors = {
            'int_type': {
                "type": INVALID_TYPE,
                "reason": INVALID_TYPE_TEXT
            },
            'greater_than_equal': {
                "type": INVALID_PARAMETER_VALUE,
                "reason": INVALID_PARAMETER_VALUE_TEXT
            },
            'less_than_equal': {
                "type": INVALID_PARAMETER_VALUE,
                "reason": INVALID_PARAMETER_VALUE_TEXT
            },
            "unknown_type": {
                "type": "UnknownType",
                "reason": "Неизвестный тип ошибки"
            }
        }

    def define_invalid_params(self) -> list[ErrorData]:
        error_list: list[ErrorData] = []
        for default_error in self.default_errors:

            if len(default_error['loc']) == 1 or \
                    (len(default_error['loc']) == 2 and type(default_error['loc'][1]) == int):
                name: str = default_error['loc'][0]
                default_type: str = default_error['type']
                process_type: str = self.__define_type_error(default_type)
            else:
                name: str = default_error['loc'][1]
                default_type: str = default_error['type']
                process_type: str = self.__define_type_error(default_type)

            error = ErrorData(
                name=name,
                type=self.data_errors[process_type]['type'],
                reason=self.data_errors[process_type]['reason']
            )
            if error not in error_list:
                error_list.append(error)

        return error_list

    def __define_type_error(self, default_type: str) -> str:
        for key in self.data_errors.keys():
            if key in default_type:
                return key
        return "unknown_type"

