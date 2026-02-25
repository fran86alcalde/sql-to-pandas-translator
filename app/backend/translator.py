import re

def sql_to_pandas(sql_query: str) -> str:
    """
    Traduce una query SQL sencilla a operaciones pandas.
    Soporta SELECT, WHERE, GROUP BY y ORDER BY básicos.
    """

    sql = sql_query.strip().rstrip(";").upper()

    select_match = re.search(r"SELECT (.+?) FROM", sql)
    from_match = re.search(r"FROM (\w+)", sql)
    where_match = re.search(r"WHERE (.+?)(GROUP BY|ORDER BY|$)", sql)
    group_match = re.search(r"GROUP BY (.+?)(ORDER BY|$)", sql)
    order_match = re.search(r"ORDER BY (.+)$", sql)

    if not select_match or not from_match:
        return "# Error: SQL no reconocido"

    columns = select_match.group(1)
    table = from_match.group(1)

    code = []
    code.append(f"df = {table}.copy()")

    if where_match:
        condition = where_match.group(1).strip()
        condition = condition.replace("=", "==")
        code.append(f"df = df.query('{condition}')")

    if group_match:
        group_cols = group_match.group(1).strip()
        code.append(f"df = df.groupby('{group_cols}').agg('count').reset_index()")

    if order_match:
        order_col = order_match.group(1).strip()
        code.append(f"df = df.sort_values('{order_col}')")

    code.append("df")

    return "\n".join(code)