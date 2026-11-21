"""Finite certificates for the seven collinear triples in Gardam's group.

Python 3.10+, standard library, assertions enabled. Writes no files.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse


SOURCE = Path(__file__).resolve().parent.parent / "Yin_J_A0005" / "verify.py"
SPEC = spec_from_file_location("gardam_normal_forms_j5", SOURCE)
assert SPEC is not None and SPEC.loader is not None
J5 = module_from_spec(SPEC)
SPEC.loader.exec_module(J5)
nf, inverse = J5.normal_form, J5.inverse

# Rows are cosets 0,...,5; the two columns are right multiplication by a,b.
TABLES = {
    "bdg": ((2,2),(5,0),(4,4),(1,1),(0,5),(3,3)),
    "bcf": ((2,3),(5,0),(4,4),(1,1),(0,5),(3,2)),
    "afg": ((2,3),(0,5),(1,4),(4,1),(5,0),(3,2)),
    "acd": ((2,2),(0,5),(1,4),(4,1),(5,0),(3,3)),
    "ceg": ((2,3),(5,5),(4,1),(1,4),(0,0),(3,2)),
    "abe": ((2,3),(0,0),(1,1),(4,4),(5,5),(3,2)),
    "def": ((2,2),(5,5),(4,1),(1,4),(0,0),(3,3)),
}
REPRESENTATIVES = {
    "bdg": ("", "B", "a", "BA", "A", "Ab"),
    "bcf": ("", "B", "a", "b", "A", "aB"),
    "afg": ("", "A", "a", "b", "B", "aB"),
    "acd": ("", "A", "a", "AB", "B", "Ab"),
    "ceg": ("", "ab", "a", "b", "A", "aB"),
    "abe": ("", "A", "a", "b", "ba", "aB"),
    "def": ("", "ab", "a", "AB", "A", "aba"),
}
# t=x^-1 y, u=x^-1 z for the displayed ordered triple xyz.
# Entry (v,k) proves r_v * (a or b) * r_target^-1 equals this word in t,u.
SCHREIER = {
    "bdg": (
        ("","u"),("uTuuTuutuTuu",""),("tuTu","Tu"),
        ("","tutuTu"),("",""),("UtUTTUtUUttU","utuTuttuTuT")),
    "bcf": (
        ("",""),("tutUttutUtt",""),("ttuTuutUtt","UtUUtt"),
        ("T","U"),("","utUtt"),("TTuu","")),
    "afg": (
        ("",""),("","u"),("TTuTUT","TTuuTu"),
        ("Utt","T"),("TTuuu",""),("TuuTuutuTutt","")),
    "acd": (
        ("","Tuu"),("",""),("UU","UT"),
        ("TuTUTTuT",""),("ttUUtUTU",""),("ututUt","tUUttUt")),
    "ceg": (
        ("",""),("TuuTuTTuuTu","UtUUttUtUUtU"),("UTUT",""),
        ("TUTUUtUTUtu","TuTUT"),("","tuTuu"),("UtUUttUt","")),
    "abe": (
        ("",""),("","t"),("ttUUtUTUUUtt","TuT"),
        ("","tuTuu"),("utuTuuTT","UUt"),("tUttuTuu","")),
    "def": (
        ("","TTuuTu"),("","TTuTT"),("tutUttUU",""),
        ("UTuuTu",""),("","Utt"),("uTuuTuutuTuu","UtUTUUtU")),
}
# Two nonbacktracking paths of length 12 from the identity on the left.
PATHS = {
    "bdg": ("dbdbdbdgbgbg", "bgdgdgdgdbgb"),
    "bcf": ("cbcbcbcfbfbf", "bfcfcfcfcbfb"),
    "afg": ("fafafafgagag", "agfgfgfgfaga"),
    "acd": ("cacacacdadad", "adcdcdcdcada"),
    "ceg": ("ecececegcgcg", "cgegegegecgc"),
    "abe": ("babababeaeae", "aebebebebaea"),
    "def": ("edededefdfdf", "dfefefefedfd"),
}
RELATION_16 = {
    triple: ("uututtUUtUTUTuTT" if triple in ("acd","ceg","abe")
             else "ututUttUUTUTTuuT")
    for triple in TABLES
}


def substitute_triangle_word(word):
    return "".join(J5.IMAGES[c] if c.islower()
                   else inverse(J5.IMAGES[c.lower()]) for c in word)


def ratio_words(triple):
    x, y, z = triple
    t, u = x.upper() + y, x.upper() + z
    return {"t": t, "u": u, "T": inverse(t), "U": inverse(u)}


def ratio_evaluate(word, triple):
    generators = ratio_words(triple)
    return nf("".join(generators[c] for c in word))


def permutation_edges(triple):
    edges = [list(row) + [-1, -1] for row in TABLES[triple]]
    for direction in range(2):
        assert sorted(row[direction] for row in edges) == list(range(6))
        for vertex in range(6):
            edges[edges[vertex][direction]][direction + 2] = vertex
    return edges


def walk(edges, word, vertex=0):
    for letter in word:
        vertex = edges[vertex]["abAB".index(letter)]
    return vertex


def check_index_certificate(triple):
    edges = permutation_edges(triple)
    for vertex in range(6):
        for relator in J5.RELATORS:
            assert walk(edges, relator, vertex) == vertex
    generators = ratio_words(triple)
    for label in "tu":
        word = generators[label]
        assert walk(edges, substitute_triangle_word(word)) == 0
    representatives = REPRESENTATIVES[triple]
    assert [walk(edges, word) for word in representatives] == list(range(6))
    for vertex in range(6):
        for direction, letter in enumerate("ab"):
            target = edges[vertex][direction]
            schreier_word = representatives[vertex] + letter + inverse(
                representatives[target])
            assert nf(schreier_word) == ratio_evaluate(
                SCHREIER[triple][vertex][direction], triple)
    relator = RELATION_16[triple]
    assert len(relator) == 16 and J5.free_reduce(relator) == relator
    assert relator.count("t") == relator.count("T")
    assert relator.count("u") == relator.count("U")
    assert ratio_evaluate(relator, triple) == ""
    return edges


def graph_step(vertex, color):
    side, word = vertex
    multiplier = color if side == 0 else color.upper()
    return 1 - side, nf(multiplier + word)


def check_girth(triple):
    # Every nonbacktracking path of length <=11 reaches a new vertex.
    root = (0, "")
    seen = {root}
    frontier = [(root, "")]
    for depth in range(1, 12):
        following = []
        for vertex, last_color in frontier:
            for color in triple:
                if color == last_color:
                    continue
                target = graph_step(vertex, color)
                assert target not in seen
                seen.add(target)
                following.append((target, color))
        assert len(following) == 3 * 2 ** (depth - 1)
        frontier = following
    assert len(seen) == 1 + 3 * (2 ** 11 - 1) == 6142

    first, second = PATHS[triple]
    assert len(first) == len(second) == 12
    cycle = first + second[::-1]
    assert all(color in triple for color in cycle)
    assert all(cycle[i] != cycle[(i + 1) % 24] for i in range(24))
    vertex = root
    cycle_vertices = {root}
    for position, color in enumerate(cycle, 1):
        vertex = graph_step(vertex, color)
        if position < 24:
            assert vertex not in cycle_vertices
            cycle_vertices.add(vertex)
    assert vertex == root and len(cycle_vertices) == 24
    return 24


def homology_matrix(edges):
    # Collapse a spanning tree of the 6-vertex, 12-edge Schreier graph.
    vertices = {0}
    queue = [0]
    tree_edges = set()
    for vertex in queue:
        for direction, target in enumerate(edges[vertex]):
            if target not in vertices:
                vertices.add(target)
                queue.append(target)
                base = vertex if direction < 2 else target
                tree_edges.add(2 * base + direction % 2)
    assert len(vertices) == 6 and len(tree_edges) == 5
    chords = sorted(set(range(12)) - tree_edges)
    matrix = []
    for vertex in range(6):
        for relator in J5.RELATORS:
            current = vertex
            chain = [0] * 12
            for letter in relator:
                direction = "abAB".index(letter)
                target = edges[current][direction]
                base = current if direction < 2 else target
                chain[2 * base + direction % 2] += 1 if direction < 2 else -1
                current = target
            assert current == vertex
            matrix.append([chain[edge] for edge in chords])
    assert len(matrix) == 12 and len(chords) == 7
    return matrix


def smith_diagonal(matrix):
    """Integer row/column Euclidean reduction; every operation is unimodular."""
    a = [row[:] for row in matrix]
    height, width = len(a), len(a[0])
    diagonal = []
    for k in range(min(height, width)):
        nonzero = [(abs(a[i][j]), i, j) for i in range(k, height)
                   for j in range(k, width) if a[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        while True:
            changed = False
            for i in range(k + 1, height):
                if a[i][k]:
                    quotient = a[i][k] // a[k][k]
                    a[i] = [x - quotient * y for x, y in zip(a[i], a[k])]
                    if a[i][k]:
                        a[i], a[k] = a[k], a[i]
                    changed = True
                    break
            if changed:
                continue
            for j in range(k + 1, width):
                if a[k][j]:
                    quotient = a[k][j] // a[k][k]
                    for row in a:
                        row[j] -= quotient * row[k]
                    if a[k][j]:
                        for row in a:
                            row[j], row[k] = row[k], row[j]
                    changed = True
                    break
            if changed:
                continue
            bad = next(((i, j) for i in range(k + 1, height)
                        for j in range(k + 1, width)
                        if a[i][j] % a[k][k]), None)
            if bad is None:
                break
            i, _ = bad
            a[k] = [x + y for x, y in zip(a[k], a[i])]
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        diagonal.append(a[k][k])
    assert all(a[i][j] == 0 for i in range(height)
               for j in range(width) if i != j)
    assert all(y % x == 0 for x, y in zip(diagonal, diagonal[1:]))
    return diagonal


def verify(triples):
    J5.check_presentation_and_overlaps()
    # Edge-rooted tree counts for girth 24, depth 11 on each side.
    side_sum = sum(2 ** i for i in range(6))
    assert 2 * side_sum == 126
    assert 3 * side_sum == 189
    for triple in triples:
        girth = check_girth(triple)
        edges = check_index_certificate(triple)
        diagonal = smith_diagonal(homology_matrix(edges))
        assert diagonal == [1, 1, 1, 1, 1, 4, 28]
        print(triple, "girth", girth, "tree vertices", 6142,
              "index", 6, "Smith", diagonal,
              "right-support bounds", (126, 189), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triple", choices=tuple(TABLES),
                        help="verify one retained triple instead of all seven")
    args = parser.parse_args()
    verify((args.triple,) if args.triple else TABLES)
