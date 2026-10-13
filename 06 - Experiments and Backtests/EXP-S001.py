#!/usr/bin/env python3
"""EXP-S001: frozen permutation-entropy synthetic invariants.

All required controls/thresholds are preregistered at GitHub commit
 e20e7b65adaca1f0c73781bcebec3750023a3439.
This is a mathematical implementation check, NOT Veron, LSE, market data,
or a trading strategy test. No third-party dependencies.
"""
import collections
import hashlib
import json
import math
import pathlib
import platform
import random
import sys

SPEC_COMMIT = "e20e7b65adaca1f0c73781bcebec3750023a3439"
N = 30002
SEED = 20261013
TOL = 1e-12


def ordinal_entropy(values, m):
    """Return Shannon entropy (bits), normalized value, counts and tie windows."""
    if not 2 <= m <= len(values):
        raise ValueError("invalid m")
    counts = collections.Counter()
    tied = 0
    for k in range(len(values) - m + 1):
        window = values[k:k + m]
        if len(set(window)) < m:
            tied += 1
        # Strict deterministic tie break: initial chronological index.
        pattern = tuple(sorted(range(m), key=lambda i: (window[i], i)))
        counts[pattern] += 1
    sample = len(values) - m + 1
    entropy_bits = -sum((freq / sample) * math.log2(freq / sample)
                        for freq in counts.values())
    normalized = entropy_bits / math.log2(math.factorial(m))
    return {
        "N": len(values), "m": m, "window_count": sample,
        "counts": {"".join(map(str, k)): v for k, v in sorted(counts.items())},
        "tied_windows": tied,
        "entropy_bits": entropy_bits, "normalized_entropy": normalized,
        "preview_first_12": values[:12],
    }


def main():
    src = pathlib.Path(__file__)
    checks = []

    def check(name, r, expected_bits, expected_nonzero_counts=None, iid=False):
        dif = abs(r["entropy_bits"] - expected_bits) if expected_bits is not None else None
        matches_counts = (expected_nonzero_counts is None or
                          sorted(r["counts"].values()) == sorted(expected_nonzero_counts))
        if iid:
            passed = (r["normalized_entropy"] >= 0.995 and
                      len(r["counts"]) == 6 and r["tied_windows"] == 0)
        else:
            passed = dif <= TOL and matches_counts
        checks.append({"test": name, "observed": r, "oracle_bits": expected_bits,
                       "absolute_error_bits": dif,
                       "required_nonzero_counts": expected_nonzero_counts,
                       "passed": passed})
        print(f"{name}: {'PASS' if passed else 'FAIL'}, H={r['entropy_bits']:.12f}, ",
              f"Hnorm={r['normalized_entropy']:.12f}, counts={r['counts']}")
        return passed

    toy = [4, 7, 9, 10, 6, 11, 3]
    check("author_toy_m2", ordinal_entropy(toy, 2),
          -(4/6*math.log2(4/6)+2/6*math.log2(2/6)), [4, 2])
    check("author_toy_m3", ordinal_entropy(toy, 3),
          -(2*(2/5*math.log2(2/5))+(1/5*math.log2(1/5))), [2, 2, 1])
    check("monotonic", ordinal_entropy(list(range(N)), 3), 0.0, [N-2])
    periodic = [0, 2, 1] * (N//3) + [0, 2, 1][:N % 3]
    check("three_cycle", ordinal_entropy(periodic, 3), math.log2(3), [10000]*3)
    iid = [random.Random(SEED).gauss(0,1) for _ in range(N)]
    # Regenerate with a single stateful RNG; avoid an accidental reset per draw.
    rng = random.Random(SEED)
    iid = [rng.gauss(0,1) for _ in range(N)]
    check("gaussian_iid", ordinal_entropy(iid, 3), None, iid=True)
    check("all_tied", ordinal_entropy([0.0]*N, 3), 0.0, [N-2])
    success = all(c["passed"] for c in checks)
    report = {
        "experiment_id": "EXP-S001", "spec_commit_sha": SPEC_COMMIT,
        "execution_environment": "OpenAI assistant isolated Linux container; NOT Veron; NOT LSE Terminal",
        "python_version": sys.version, "platform": platform.platform(),
        "seed": SEED, "N": N, "m": 3, "delay": 1,
        "tie_rule": "ascending observed value; on equal value ascending time index (adaptation)",
        "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
        "controls": checks, "all_passed": success,
        "verdict": "PASS - synthetic numerical invariants only" if success else "FAIL",
        "empirical_results": None, "trading_results": None,
        "replay_command": "python3 EXP-S001.py",
        "thresholds_frozen_at": SPEC_COMMIT,
    }
    dst = src.with_name("EXP-S001-results.json")
    dst.write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(f"VERDICT: {report['verdict']}; outputs={dst.name}; SHA256(source)={report['source_sha256']}")
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
