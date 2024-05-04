from good_research.file_to_upper import file_to_upper
import tempfile
import os


def test_upper():
    # Create mock files.
    # We create temporary files so we don't have to care about the filename.
    # A NamedTemporaryFile allows us to open the file again using its name.
    in_file = tempfile.NamedTemporaryFile(delete=False, mode="w")
    in_file.write("test123\nthetest")
    in_file.close()
    out_file = tempfile.NamedTemporaryFile(delete=False)
    out_file.close()
    # Run function.
    file_to_upper(in_file.name, out_file.name)
    with open(out_file.name, "r") as f:
        data = f.read()
        assert data == "TEST123\nTHETEST"
    # Remove mock files.
    os.unlink(in_file.name)
    os.unlink(out_file.name)
