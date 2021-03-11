import re


def camel_to_kebab(name):
    """Convert CamelCase names to kebab-case names.

    >>> camel_to_kebab('kebab-2-kebab-case')
    'kebab-2-kebab-case'
    >>> camel_to_kebab('getHTTPResponseCode')
    'get-http-response-code'
    >>> camel_to_kebab('HTTPResponseCodeXYZ')
    'http-response-code-xyz'
    """
    name = re.sub("(.)([A-Z][a-z]+)", r"\1-\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1-\2", name).lower()
