from practice39.py import bin_len


def test_bin_len_empty() -> None:
    assert bin_len([]) == {}


def test_bin_len_use1() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
