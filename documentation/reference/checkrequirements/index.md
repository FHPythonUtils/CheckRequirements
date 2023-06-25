# Checkrequirements

[Checkrequirements Index](../README.md#checkrequirements-index) /
Checkrequirements

> Auto-generated documentation for [checkrequirements](../../../checkrequirements/__init__.py) module.

- [Checkrequirements](#checkrequirements)
  - [Dependency](#dependency)
  - [UpdateCompatible](#updatecompatible)
  - [checkRequirements](#checkrequirements)
  - [cli](#cli)
  - [partCmp](#partcmp)
  - [semCmp](#semcmp)
  - [semPad](#sempad)
  - [semver](#semver)
  - [updateCompatible](#updatecompatible)
  - [Modules](#modules)

## Dependency

[Show source in __init__.py:25](../../../checkrequirements/__init__.py#L25)

Dependency type.

#### Signature

```python
class Dependency(typing.TypedDict):
    ...
```



## UpdateCompatible

[Show source in __init__.py:18](../../../checkrequirements/__init__.py#L18)

UpdateCompatible type.

#### Signature

```python
class UpdateCompatible(typing.TypedDict):
    ...
```



## checkRequirements

[Show source in __init__.py:190](../../../checkrequirements/__init__.py#L190)

Check that your requirements.txt is up to date with the most recent package
versions. Put in a function so dependants can use this function rather than
reimplement it themselves.

#### Arguments

- `requirementsFile` *str* - file path to the requirements file

#### Returns

- [Dependency](#dependency) - dictionary containing info on each requirement such as the name,
specs (from requirements_parser), ver (most recent version), compatible
(is our version compatible with ver)

#### Signature

```python
def checkRequirements(requirementsFile: str) -> list[Dependency]:
    ...
```

#### See also

- [Dependency](#dependency)



## cli

[Show source in __init__.py:211](../../../checkrequirements/__init__.py#L211)

CLI entry point.

#### Signature

```python
def cli():
    ...
```



## partCmp

[Show source in __init__.py:62](../../../checkrequirements/__init__.py#L62)

Compare parts of a semver.

#### Arguments

- `verA` *str* - lhs part to compare
- `verB` *str* - rhs part to compare

#### Returns

- `int` - 0 if equal, 1 if verA > verB and -1 if verA < verB

#### Signature

```python
def partCmp(verA: str, verB: str) -> int:
    ...
```



## semCmp

[Show source in __init__.py:149](../../../checkrequirements/__init__.py#L149)

Compare two semvers of any length. e.g. 1.1 and 2.2.2.

#### Arguments

- `versionA` *list[str]* - lhs to compare
- `versionB` *list[str]* - rhs to compare
- `sign` *str* - string sign. one of ==, ~=, <=, >=, <, >

#### Raises

- `ValueError` - if the sign is not one of the following.

#### Returns

- `bool` - true if the comparison is met. e.g. 1.1.1, 2.2.2, <= -> True

#### Signature

```python
def semCmp(versionA: str, versionB: str, sign: str) -> bool:
    ...
```



## semPad

[Show source in __init__.py:46](../../../checkrequirements/__init__.py#L46)

Pad a semver list to the required size. e.g. ["1", "0"] to ["1", "0", "0"].

#### Arguments

- `ver` *list[str]* - the semver representation
- `length` *int* - the new length

#### Returns

- `list[str]` - the new semver

#### Signature

```python
def semPad(ver: list[str], length: int) -> list[str]:
    ...
```



## semver

[Show source in __init__.py:34](../../../checkrequirements/__init__.py#L34)

Convert a semver/ python-ver string to a list in the form major, minor patch

#### Arguments

- `version` *str* - The version to convert

#### Returns

- `list[str]` - A list in the form major, minor, patch

#### Signature

```python
def semver(version: str) -> list[str]:
    ...
```



## updateCompatible

[Show source in __init__.py:169](../../../checkrequirements/__init__.py#L169)

Check if the most recent version of a python requirement is compatible with
the current version.

#### Arguments

- `req` *Requirement* - the requirement object as parsed by requirements_parser

#### Returns

- [UpdateCompatible](#updatecompatible) - return a dict of the most recent version (ver) and
is our requirement from requirements.txt or similar compatible
with the new version per the version specifier (compatible)

#### Signature

```python
def updateCompatible(req: Requirement) -> UpdateCompatible:
    ...
```

#### See also

- [UpdateCompatible](#updatecompatible)



## Modules

- [Module](./module.md)