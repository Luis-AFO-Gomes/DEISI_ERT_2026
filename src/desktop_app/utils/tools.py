def print_list(items, columns=None, headers=None, max_width=40):
    """
    Prints a list as a table.

    Supports:
    - list of objects
    - list of dictionaries
    - list of tuples/lists
    - list of simple values
    """

    if not items:
        print("(empty list)")
        return

    max_width = max(2, max_width)

    def fmt(v):
        s = "" if v is None else str(v)
        s = s.replace("\n", " ")
        return (s[: max_width - 1] + "…") if len(s) > max_width else s

    def get_value(item, column):
        if column is None:
            return item

        if callable(column):
            return column(item)

        if isinstance(item, dict):
            return item.get(column, "")

        if isinstance(item, (list, tuple)):
            return item[column]

        return getattr(item, column, "")

    # If columns not given, infer them
    if columns is None:
        first = items[0]

        if isinstance(first, dict):
            columns = list(first.keys())

        elif isinstance(first, (list, tuple)):
            columns = list(range(len(first)))

        elif hasattr(first, "__dict__"):
            columns = [
                attr for attr in vars(first).keys()
                if not attr.startswith("_")
            ]

        else:
            columns = [None]

    # If headers not given, use column names
    if headers is None:
        headers = [
            col.__name__ if callable(col) else str(col)
            for col in columns
        ]

    data = [
        [fmt(get_value(item, col)) for col in columns]
        for item in items
    ]

    cols = list(zip(*([headers] + data)))
    widths = [max(len(x) for x in col) for col in cols]

    # header
    line = " | ".join(h.ljust(w) for h, w in zip(headers, widths))
    sep = "-+-".join("-" * w for w in widths)

    print(line)
    print(sep)

    # rows
    for row in data:
        print(" | ".join(cell.ljust(w) for cell, w in zip(row, widths)))        
