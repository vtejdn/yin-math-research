"""Exploratory finite coefficient-algebra inverse; not finite-dimensional duals."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def probe(n: int, power: float, shift: float, base_seed: int) -> dict:
    rng = np.random.default_rng(base_seed + n)
    g = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2 * n)
    s = (g + g.conj().T) / np.sqrt(2) + shift * np.eye(n)
    h_values = ((np.arange(n) + 0.5) / n) ** power
    h = np.diag(h_values)
    root_h = np.diag(np.sqrt(h_values))
    a = root_h @ s @ root_h
    eye = np.eye(n)
    diagonal = np.kron(np.sqrt(h_values), np.sqrt(h_values))
    rhs = np.diag(diagonal)
    k = np.kron(a, eye) + np.kron(eye, a.T) + 1j * np.kron(h, h.T)
    u = np.linalg.solve(k, rhs)
    v = u / diagonal[:, None]
    original = np.kron(s @ h, eye) + np.kron(eye, (h @ s).T) + 1j * np.kron(h, h.T)
    weighted_residual = float(np.linalg.norm(k @ u - rhs, "fro") / np.linalg.norm(rhs, "fro"))
    original_residual = float(np.linalg.norm(original @ v - np.eye(n * n), "fro") / n)
    weighted_norm = float(np.linalg.norm(u, "fro") / n)
    unweighted_norm = float(np.linalg.norm(v, "fro") / n)
    min_s = float(np.linalg.eigvalsh(s)[0])
    control = 1 / (2 * min_s) if min_s > 0 else None
    if weighted_residual > 1e-9 or original_residual > 1e-8:
        raise ArithmeticError(f"Residual failure at {(n, power, shift)}: {weighted_residual}, {original_residual}")
    if control is not None and weighted_norm > control * (1 + 1e-9):
        raise ArithmeticError(f"Positive-S bound failed at {(n, power, shift)}")
    return {
        "n": n,
        "h_quantile_power": power,
        "s_shift": shift,
        "seed": base_seed + n,
        "minimum_h": float(h_values[0]),
        "minimum_s": min_s,
        "inverse_h_l1": float(np.mean(1 / h_values)),
        "inverse_h_l2": float(np.sqrt(np.mean(1 / h_values**2))),
        "weighted_u_hs_norm": weighted_norm,
        "unweighted_v_hs_norm": unweighted_norm,
        "positive_s_bound": control,
        "weighted_relative_residual": weighted_residual,
        "original_relative_residual": original_residual,
    }


def output_destination(group: Path, output: str) -> Path:
    filename = Path(output)
    if filename.anchor or ".." in filename.parts:
        raise ValueError("Output must be a relative filename within this J's output home.")
    home = group.resolve()
    destination = (home / filename).resolve()
    if destination == home or not destination.is_relative_to(home):
        raise ValueError("Output must resolve to a file within this J's output home.")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[8, 12, 16, 24, 32])
    parser.add_argument("--powers", nargs="+", type=float, default=[0.8, 1.0, 1.2])
    parser.add_argument("--shifts", nargs="+", type=float, default=[0.0, 3.0])
    parser.add_argument("--seed", type=int, default=20261015)
    parser.add_argument("--output", default="results.json", help="Filename within this J's output home; use a distinct name for a smaller control.")
    args = parser.parse_args()
    if any(n < 2 or n > 64 for n in args.sizes):
        parser.error("Each size must be between 2 and 64 for this dense probe.")
    if any(q <= 0 for q in args.powers):
        parser.error("Quantile powers must be positive.")
    program = Path(__file__).resolve().parent
    repository = next(parent for parent in program.parents if (parent / "repository/config.json").is_file())
    group = repository / "mathematics/computations/outputs" / program.name
    try:
        destination = output_destination(group, args.output)
    except ValueError as error:
        parser.error(str(error))
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": "incomplete",
        "arithmetic": "complex128",
        "parameters": {key: getattr(args, key) for key in ("sizes", "powers", "shifts", "seed")},
        "scope": "Finite coefficient-algebra inverse only. No finite-dimensional ACSY or dual-system assertion; no asymptotic conclusion.",
        "results": [],
    }
    for n in args.sizes:
        for power in args.powers:
            for shift in args.shifts:
                row = probe(n, power, shift, args.seed)
                payload["results"].append(row)
                print(json.dumps({key: row[key] for key in ("n", "h_quantile_power", "s_shift", "weighted_u_hs_norm", "unweighted_v_hs_norm")}), flush=True)
    payload["status"] = "complete"
    temporary = destination.with_name("." + destination.name + ".partial")
    try:
        temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
