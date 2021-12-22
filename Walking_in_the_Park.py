file_search = input("Enter the full path to start walking files from: ")
    for root, dirs, files in os.walk(file_search):
        for fname in files:
            if fname.endswith(".doc") or fname.endswith("docx") or fname.endswith("docm") or fname.endswith("docm") or fname.endswith("xls") or fname.endswith("xlsx") or fname.endswith("txt"):
                full_name = os.path.join(root, fname)
                continue
            else:
                continue
