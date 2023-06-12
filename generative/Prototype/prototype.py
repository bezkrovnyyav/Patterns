import copy


class BasePhone:

    def __init__(self, name: str, params: dict):
        self.name = name
        self.params = params

    def __copy__(self):
        # Create copies of the nested objects.
        details = copy.copy(self.params)
        
        # Clone the object itself, using the prepared clones of the nested objects.
        new = self.__class__(
            self.name, details
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        # Create copies of the nested objects.
        details = copy.deepcopy(self.params, memo)

        # Clone the object itself, using the prepared clones of the nested objects.
        new = self.__class__(
            self.name, details
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":
    name = 'IPhone 16 GB'
    params = {
        'memory': '16 GB',
        'operation_system': 'iOS'
    }

    iPhone_16_GB = BasePhone(name, params)

    Android_32_GB = copy.deepcopy(iPhone_16_GB)
    Android_32_GB.name = 'Android 32 GB'
    Android_32_GB.params['memory'] = '32 GB'
    Android_32_GB.params['operation_system'] = 'Android'
    
    print(iPhone_16_GB.name, iPhone_16_GB.params)
    print(Android_32_GB.name, Android_32_GB.params)
