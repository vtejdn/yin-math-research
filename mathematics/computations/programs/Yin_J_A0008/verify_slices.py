"""Exact zero-specialization certificates on 25 cyclic indices."""
def centered(x, p):
    return (x + p // 2) % p - p // 2


def verify(p, root, c, expected_width):
    weights = [centered(c * pow(root, i // 5, p), p)
               if i % 5 in (0, 2, 4) else 0 for i in range(25)]
    assert sum(map(abs, weights)) == expected_width
    assert 2 * expected_width * 5 <= 2 * 25 * p
    rows = [[(i + step) % 25 for step in (0, 1, 7, 8)
             if (step < 7 and w >= 0) or (step >= 7 and w <= 0)]
            for i, w in enumerate(weights)]

    # Match the columns to distinct rows by augmenting paths.
    column_at_row = {}

    def extend(column, seen_rows):
        for row in rows[column]:
            if row in seen_rows:
                continue
            seen_rows.add(row)
            if row not in column_at_row or extend(column_at_row[row], seen_rows):
                column_at_row[row] = column
                return True
        return False

    for column in range(25):
        assert extend(column, set())
    assert set(column_at_row.values()) == set(range(25))

    # Collapse each matched edge, then find mutual reachability.
    reach = [{column_at_row[row] for row in allowed} for allowed in rows]
    for middle in range(25):
        for column in range(25):
            if middle in reach[column]:
                reach[column].update(reach[middle])
    blocks = {tuple(j for j in sorted(targets) if i in reach[j])
              for i, targets in enumerate(reach)}
    assert sorted(map(len, blocks)) == [1] * 13 + [2] * 6
    for columns in blocks:
        if len(columns) == 2:
            block_rows = [r for r, i in column_at_row.items() if i in columns]
            offsets = [sorted((r - i) % 25 for r in block_rows)
                       for i in columns]
            assert sorted(offsets) == [[0, 1], [7, 8]]


def main():
    for prime, scale, width in ((11, 1, 45), (41, 1, 147), (61, 5, 213)):
        roots = [r for r in range(2, prime) if pow(r, 5, prime) == 1]
        assert len(roots) == 4
        for r in roots:
            verify(prime, r, scale, width)
        print(f"p={prime}: roots {roots}, total block width {width}, all checks passed")


if __name__ == "__main__":
    main()
