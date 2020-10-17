# checkrequirements

> Auto-generated documentation for [checkrequirements](../../checkrequirements/__init__.py) module.

Check that your requirements.txt is up to date with the most recent package
versions

- [Checkrequirements](../README.md#checkrequirements-index) / [Modules](../README.md#checkrequirements-modules) / checkrequirements
    - [Dependency](#dependency)
    - [UpdateCompatible](#updatecompatible)
    - [checkRequirements](#checkrequirements)
    - [cli](#cli)
    - [partCmp](#partcmp)
    - [semCmp](#semcmp)
    - [semPad](#sempad)
    - [semver](#semver)
    - [updateCompatible](#updatecompatible)
    - Modules
        - [\_\_main\_\_](module.md#__main__)

## Dependency

[[find in source code]](../../checkrequirements/__init__.py#L27)

```python
class Dependency(typing.TypedDict):
```

Dependency type

## UpdateCompatible

[[find in source code]](../../checkrequirements/__init__.py#L21)

```python
class UpdateCompatible(typing.TypedDict):
```

UpdateCompatible type

## checkRequirements

[[find in source code]](../../checkrequirements/__init__.py#L192)

```python
def checkRequirements(requirementsFile: str) -> list[Dependency]:
```

Check that your requirements.txt is up to date with the most recent package
versions. Put in a function so dependants can use this function rather than
reimplement it themselves

#### Arguments

- `requirementsFile` *str* - file path to the requirements file

#### Returns

- `Dependency` - dictionary containing info on each requirement such as the name,
specs (from requirements_parser), ver (most recent version), compatible
(is our version compatible with ver)

## cli

[[find in source code]](../../checkrequirements/__init__.py#L212)

```python
def cli():
```

cli entry point

## partCmp

[[find in source code]](../../checkrequirements/__init__.py#L64)

```python
def partCmp(verA: str, verB: str) -> int:
```

Compare parts of a semver

#### Arguments

- `verA` *str* - lhs part to compare
- `verB` *str* - rhs part to compare

#### Returns

- `int` - 0 if equal, 1 if verA > verB and -1 if verA < verB

## semCmp

[[find in source code]](../../checkrequirements/__init__.py#L151)

```python
def semCmp(versionA: str, versionB: str, sign: str) -> bool:
```

compare two semvers of any length. e.g. 1.1 and 2.2.2

#### Arguments

- `semA` *list[str]* - lhs to compare
- `semB` *list[str]* - rhs to compare
- `sign` *str* - string sign. one of ==, ~=, <=, >=, <, >

#### Raises

- `ValueError` - if the sign is not one of the following.

#### Returns

- `bool` - true if the comparison is met. e.g. 1.1.1, 2.2.2, <= -> True

## semPad

[[find in source code]](../../checkrequirements/__init__.py#L48)

```python
def semPad(ver: list[str], length: int) -> list[str]:
```

Pad a semver list to the required size. e.g. ["1", "0"] to ["1", "0", "0"]

#### Arguments

- `ver` *list[str]* - the semver representation
- `length` *int* - the new length

#### Returns

- `list[str]` - the new semver

## semver

[[find in source code]](../../checkrequirements/__init__.py#L35)

```python
def semver(version: str) -> list[str]:
```

Convert a semver/ pythonver string to a list in the form major, minor,
patch ...

#### Arguments

- `version` *str* - The version to convert

#### Returns

- `list[str]` - A list in the form major, minor, patch ...

## updateCompatible

[[find in source code]](../../checkrequirements/__init__.py#L171)

```python
def updateCompatible(req: Requirement) -> UpdateCompatible:
```

Check if the most recent version of a python requirement is compatible
with the current version

#### Arguments

- `req` *Requirement* - the requirement object as parsed by requirements_parser

#### Returns

- `UpdateCompatible` - return a dict of the most recent version (ver) and
is our requirement from requirements.txt or similar compatible
with the new version per the version specifier (compatible)

#### See also

- [UpdateCompatible](#updatecompatible)
