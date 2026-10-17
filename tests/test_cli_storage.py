from cowokkit import cli, storage


def test_storage_roundtrip(tmp_path):
    p = tmp_path / "db.json"
    assert storage.load(p)["expenses"] == []
    storage.save({"expenses": [1], "workouts": [], "grooming": {}}, p)
    assert storage.load(p)["expenses"] == [1]


def test_cli_flow(tmp_path, capsys):
    p = tmp_path / "db.json"
    assert cli.run(["expense", "20000", "makan"], path=p) == 0
    cli.run(["bmi", "70", "175", "25"], path=p)
    cli.run(["workout", "gym", "45"], path=p)
    cli.run(["groom", "--done", "potong_kuku"], path=p)
    cli.run(["groom"], path=p)
    cli.run(["summary"], path=p)
    out = capsys.readouterr().out
    assert "Tercatat" in out and "BMI 22.9" in out and "makan" in out
