# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2023

- checkrequirements is now a thin wrapper around poetry show and sets an exit code only. **Note:** this only supports poetry based environments. `requirements.txt` and other build systems are no longer supported!

## 2022.0.1 - 2022/04/06

- Remove metprint
- Update deps

## 2022 - 2022/01/27

- Update deps
- Add formal tests

## 2021.0.1 - 2021/11/12

- add pre-commit
- code quality improvements

## 2021 - 2021/03/01

- Tidied up
- Added `--zero/-0` flag to return non-zero exit code when an incompatible
  license is found

## 2020.0.7 - 2020/10/17

- Bugfixes

## 2020.0.6 - 2020/10/12

- set stdout to utf-8

## 2020.0.5 - 2020/10/10

- fix typing and bugfixes

## 2020.0.4 - 2020/10/10

- fix python 3.7 and 3.8

## 2020.0.3 - 2020/10/08

- output for no requirements

## 2020.0.2 - 2020/10/08

- Use `metprint` if available
- Bugfixes
- Improvements - can use the main functionality if using as a module

## 2020 - 2020/10/07

- First release
