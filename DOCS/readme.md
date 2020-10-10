Module checkrequirements
========================
Check that your requirements.txt is up to date with the most recent package
versions

Functions
---------

    
`checkRequirements(requirementsFile: str) ‑> dict`
:   Check that your requirements.txt is up to date with the most recent package
    versions. Put in a function so dependants can use this function rather than
    reimplement it themselves
    
    Args:
            requirementsFile (str): file path to the requirements file
    
    Returns:
            dict: dictionary containing info on each requirement such as the name,
            specs (from requirements_parser), ver (most recent version), compatible
            (is our version compatible with ver)

    
`cli()`
:   cli entry point

    
`partCmp(verA: str, verB: str) ‑> int`
:   Compare parts of a semver
    
    Args:
            verA (str): lhs part to compare
            verB (str): rhs part to compare
    
    Returns:
            int: 0 if equal, 1 if verA > verB and -1 if verA < verB

    
`semCmp(versionA: str, versionB: str, sign: str) ‑> bool`
:   compare two semvers of any length. e.g. 1.1 and 2.2.2
    
    Args:
            semA (list[str]): lhs to compare
            semB (list[str]): rhs to compare
            sign (str): string sign. one of ==, ~=, <=, >=, <, >
    
    Raises:
            ValueError: if the sign is not one of the following.
    
    Returns:
            bool: true if the comparison is met. e.g. 1.1.1, 2.2.2, <= -> True

    
`semPad(ver: list[str], length: int) ‑> list`
:   Pad a semver list to the required size. e.g. ["1", "0"] to ["1", "0", "0"]
    
    Args:
            ver (list[str]): the semver representation
            length (int): the new length
    
    Returns:
            list[str]: the new semver

    
`semver(version: str) ‑> list`
:   Convert a semver/ pythonver string to a list in the form major, minor,
    patch ...
    
    Args:
            version (str): The version to convert
    
    Returns:
            list[str]: A list in the form major, minor, patch ...

    
`updateCompatible(req: Requirement) ‑> dict`
:   Check if the most recent version of a python requirement is compatible
    with the current version
    
    Args:
            req (Requirement): the requirement object as parsed by requirements_parser
    
    Returns:
            dict: return a dict of the most recent version (ver) and
            is our requirement from requirements.txt or similar compatible
            with the new version per the version specifier (compatible)