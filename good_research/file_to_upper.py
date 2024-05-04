def file_to_upper(in_file, out_file):
    fout = open(out_file, "w")
    with open(in_file, "r") as f:
        for line in f:
            fout.write(line.upper())
    fout.close()
