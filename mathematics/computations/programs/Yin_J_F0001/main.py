"""Exact finite checks of DR97 Proposition 5; see the matching Markdown record."""

from collections import Counter


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def words(rank, maximum):
    alphabet = tuple(range(1, rank + 1)) + tuple(range(-1, -rank - 1, -1))
    result = [()]
    layer = [()]
    for _ in range(maximum):
        layer = [w + (x,) for w in layer for x in alphabet if not w or w[-1] != -x]
        result.extend(layer)
    return result


def difference(positive, negative):
    result = Counter({positive: 1})
    result[negative] -= 1
    return {word: coefficient for word, coefficient in result.items() if coefficient}


def direct_edge_defect(h, farther):
    """Translate both endpoints, then select the endpoint farther from the root."""
    near_image = reduce_word(h + farther[:-1])
    far_image = reduce_word(h + farther)
    if abs(len(near_image) - len(far_image)) != 1:
        raise AssertionError("Translated edge is not a tree edge")
    p_inverse_image = max((near_image, far_image), key=len)
    return difference(p_inverse_image, far_image)


def residual_formula(h, farther):
    """Compute the suffix residual, then multiply on the right by bar(x)-1."""
    suffix = inverse(farther)
    if len(h) < len(suffix) or h[-len(suffix):] != suffix:
        return {}
    prefix = h[:-len(suffix)]
    return difference(reduce_word(prefix + (-farther[-1],)), prefix)


def main():
    count = 0
    scalar_count = 0
    exceptional_count = 0
    print("Exact integer word dictionaries; no intermediate support truncation")
    for rank in (0, 1, 2):
        group_words = words(rank, 5)
        edge_words = words(rank, 4)[1:]
        local_count = 0
        for h in group_words:
            # P^{-1} a(q) - a P^{-1}(q) = 0 - h.
            scalar_image = {reduce_word(h + ()): -1}
            if scalar_image != {h: -1}:
                raise AssertionError(("auxiliary scalar column", h))
            scalar_count += 1
            for farther in edge_words:
                direct = direct_edge_defect(h, farther)
                predicted = residual_formula(h, farther)
                if direct != predicted:
                    raise AssertionError((rank, h, farther, direct, predicted))
                local_count += 1
                exceptional_count += bool(direct)
        count += local_count
        print(f"PASS rank {rank}: {len(group_words)} coefficient words, "
              f"{len(edge_words)} outward edges, {local_count} edge identities")
    print(f"PASS edge identities: {count}")
    print(f"PASS auxiliary scalar columns: {scalar_count}")
    print(f"Nonzero edge-defect cases included: {exceptional_count}")
    print(f"PASS total equalities: {count + scalar_count}")
    print("This finite check does not prove rationality, boundedness, or convergence.")


if __name__ == "__main__":
    main()
