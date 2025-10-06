def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

def validate_input(func):
    def wrapper(self, input_data):
        if input_data is None or (isinstance(input_data, str) and not input_data.strip()):
            raise ValueError("Input data is missing or empty.")
        return func(self, input_data)
    return wrapper



