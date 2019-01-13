def validate(name: str):
    if len(name) < 10:
        raise ValueError


# validate('iago') # <- ValueError


class NameTooShortError(ValueError):
    pass


def validate(name: str):
    if len(name) < 10:
        raise NameTooShortError(name)

# validate('iago') # It outputs at the last line: __main__.NameTooShortError: iago


class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass


try:
    validate('Iago')
except BaseValidationError as err:
    pass

