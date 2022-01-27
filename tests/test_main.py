from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)


from checkrequirements import checkRequirements, partCmp, semCmp, semPad, semver


def test_semver():
	assert semver("0.0.0") == ["0", "0", "0"]
	assert semver("0.0") == ["0", "0"]
	assert semver("0") == ["0"]
	assert semver("1.0.0") == ["1", "0", "0"]
	assert semver("0.1.0") == ["0", "1", "0"]
	assert semver("0.0.1") == ["0", "0", "1"]
	assert semver("0.0.0.1") == ["0", "0", "0", "1"]


def test_semPad():
	assert semPad(["0"], 10) == ["0"] * 10
	assert semPad(["0"] * 5, 10) == ["0"] * 10
	assert semPad(["0"] * 20, 10) == ["0"] * 20
	assert semPad(["0", "1"], 10) == ["0", "1"] + ["0"] * 8
	assert semPad(["0", "1", "*"], 10) == ["0", "1"] + ["*"] * 8


def test_partCmp_eq():
	assert partCmp("0", "0") == 0
	assert partCmp("0", "*") == 0
	assert partCmp("*", "0") == 0
	assert partCmp("1", "1") == 0


def test_partCmp_lt():
	assert partCmp("0", "1") == -1
	assert partCmp("-2", "-1") == -1
	assert partCmp("1", "2") == -1


def test_partCmp_gt():
	assert partCmp("1", "0") == 1
	assert partCmp("-1", "-2") == 1
	assert partCmp("2", "1") == 1


def test_semCmp_eq():
	assert semCmp("0.0.0", "0.0.0", "==")
	assert semCmp("0.1.0", "0.1.0", "==")
	assert semCmp("0.0.1", "0.0.1", "==")

	# different len
	assert semCmp("0.0.0", "0", "==")
	assert semCmp("0.1.0", "0.1", "==")
	assert semCmp("1.0.0", "1", "==")

	# wildcards
	assert semCmp("0.0.0", "*", "==")
	assert semCmp("0.0.0", "0.*", "==")
	assert semCmp("0.0.0", "0.0.*", "==")
	assert semCmp("0.0.0", "0.0.*.0", "==")


def test_semCmp_lt():
	assert not semCmp("0.0.0", "0.0.0", "<")
	assert not semCmp("0.1.0", "0.1.0", "<")
	assert not semCmp("0.0.1", "0.0.1", "<")

	# different len
	assert not semCmp("0.0.0", "0", "<")
	assert not semCmp("0.1.0", "0.1", "<")
	assert not semCmp("1.0.0", "1", "<")

	# wildcards
	assert not semCmp("0.0.0", "*", "<")
	assert not semCmp("0.0.0", "0.*", "<")
	assert not semCmp("0.0.0", "0.0.*", "<")
	assert not semCmp("0.0.0", "0.0.*.0", "<")

	assert semCmp("0.0.0", "0.0.1", "<")
	assert semCmp("0.0.1", "0.1.0", "<")
	assert semCmp("0.0.0", "0.0.1", "<")

	# different len
	assert semCmp("0.0.0", "0.1", "<")
	assert semCmp("0.1.0", "1", "<")
	assert semCmp("1.0.0", "2", "<")

	# wildcards
	assert semCmp("0.0.0", "1.*", "<")
	assert semCmp("0.0.0", "0.1.*", "<")
	assert semCmp("0.0.0", "0.0.1.*", "<")


def test_semCmp_gt():
	assert not semCmp("0.0.0", "0.0.0", ">")
	assert not semCmp("0.1.0", "0.1.0", ">")
	assert not semCmp("0.0.1", "0.0.1", ">")

	# different len
	assert not semCmp("0.0.0", "0", ">")
	assert not semCmp("0.1.0", "0.1", ">")
	assert not semCmp("1.0.0", "1", ">")

	# wildcards
	assert not semCmp("0.0.0", "*", ">")
	assert not semCmp("0.0.0", "0.*", ">")
	assert not semCmp("0.0.0", "0.0.*", ">")
	assert not semCmp("0.0.0", "0.0.*.0", ">")

	assert semCmp("0.0.1", "0.0.0", ">")
	assert semCmp("0.1.0", "0.0.1", ">")
	assert semCmp("0.0.1", "0.0.0", ">")

	# different len
	assert semCmp("0.1", "0.0.0", ">")
	assert semCmp("1", "0.1.0", ">")
	assert semCmp("2", "1.0.0", ">")

	# wildcards
	assert semCmp("1.*", "0.0.0", ">")
	assert semCmp("0.1.*", "0.0.0", ">")
	assert semCmp("0.0.1.*", "0.0.0", ">")


def test_semCmp_lte():
	assert semCmp("0.0.0", "0.0.0", "<=")
	assert semCmp("0.1.0", "0.1.0", "<=")
	assert semCmp("0.0.1", "0.0.1", "<=")

	# different len
	assert semCmp("0.0.0", "0", "<=")
	assert semCmp("0.1.0", "0.1", "<=")
	assert semCmp("1.0.0", "1", "<=")

	# wildcards
	assert semCmp("0.0.0", "*", "<=")
	assert semCmp("0.0.0", "0.*", "<=")
	assert semCmp("0.0.0", "0.0.*", "<=")
	assert semCmp("0.0.0", "0.0.*.0", "<=")

	assert semCmp("0.0.0", "0.0.1", "<=")
	assert semCmp("0.0.1", "0.1.0", "<=")
	assert semCmp("0.0.0", "0.0.1", "<=")

	# different len
	assert semCmp("0.0.0", "0.1", "<=")
	assert semCmp("0.1.0", "1", "<=")
	assert semCmp("1.0.0", "2", "<=")

	# wildcards
	assert semCmp("0.0.0", "1.*", "<=")
	assert semCmp("0.0.0", "0.1.*", "<=")
	assert semCmp("0.0.0", "0.0.1.*", "<=")


def test_semCmp_gte():
	assert semCmp("0.0.0", "0.0.0", ">=")
	assert semCmp("0.1.0", "0.1.0", ">=")
	assert semCmp("0.0.1", "0.0.1", ">=")

	# different len
	assert semCmp("0.0.0", "0", ">=")
	assert semCmp("0.1.0", "0.1", ">=")
	assert semCmp("1.0.0", "1", ">=")

	# wildcards
	assert semCmp("0.0.0", "*", ">=")
	assert semCmp("0.0.0", "0.*", ">=")
	assert semCmp("0.0.0", "0.0.*", ">=")
	assert semCmp("0.0.0", "0.0.*.0", ">=")

	assert semCmp("0.0.1", "0.0.0", ">=")
	assert semCmp("0.1.0", "0.0.1", ">=")
	assert semCmp("0.0.1", "0.0.0", ">=")

	# different len
	assert semCmp("0.1", "0.0.0", ">=")
	assert semCmp("1", "0.1.0", ">=")
	assert semCmp("2", "1.0.0", ">=")

	# wildcards
	assert semCmp("1.*", "0.0.0", ">=")
	assert semCmp("0.1.*", "0.0.0", ">=")
	assert semCmp("0.0.1.*", "0.0.0", ">=")


def test_checkRequirements_0():
	assert checkRequirements(f"{THISDIR}/data/test_reqs0.txt")[0]["compatible"]


def test_checkRequirements_1():
	assert not checkRequirements(f"{THISDIR}/data/test_reqs1.txt")[0]["compatible"]
