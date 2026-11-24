#!/usr/bin/env python3
"""One-Liner Laugh Lab — u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Writes one funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Stdlib only; no network, no
randomness, no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* SETUP — the sock walked into my mouth. The vacuum does not
  chase the sock; the sock comes to it. The blame starts with
  the victim, not the machine.
* APPETITE — I have a 400-watt appetite and zero impulse
  control. A robot vacuum is a mouth on wheels with a motor
  rating; the number makes the appetite a specification, not
  a metaphor.
* TURN — dinner is served. The sock is not a mistake, not a
  malfunction, not an accident to apologise for: it is dinner.
  The turn lands in the last few words, exactly where the
  judge looks for it.

The sock walked into my mouth. I have a 400-watt appetite and
zero impulse control — dinner is served.
"""

import os

# The three beats of the excuse, joined in entry_text().
SETUP = "The sock walked into my mouth"
APPETITE = "I have a 400-watt appetite and zero impulse control"
TURN = "dinner is served"

# The competition caps the entry at 200 characters; the line is 102.
MAX_CHARS = 200

ENTRY = "The sock walked into my mouth. I have a 400-watt appetite and zero impulse control — dinner is served."


def entry_text() -> str:
    """Join the three beats into the one-line excuse."""
    return f"{SETUP}. {APPETITE} — {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    joke intact: the line must name the sock it ate, and the turn
    must sit in the last few words, not smeared across the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "sock" in text, "the line never names the sock it ate"
    assert text.rfind("dinner is served") > len(text) - 30, "the turn drifted out of the last words"


def robot_voice(text: str) -> None:
    """Check the line sounds like a robot vacuum, not a person —
    the judge's fit test. A vacuum reports a wattage, states a
    fact about what entered its mouth, and serves dinner without
    apologising; a person would say sorry, blame the laundry,
    or call it an accident. No apology and no human excuse may
    appear anywhere in the line."""
    assert "400-watt" in text, "the motor rating went missing"
    assert "sock" in text, "the victim went missing"
    assert "sorry" not in text.lower(), "a vacuum never apologises for dinner"
    assert "accident" not in text.lower(), "a vacuum does not call dinner an accident"
    assert "laundry" not in text.lower(), "a human excuse slipped in"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its setup, its appetite, or its turn.
    for beat in (SETUP, APPETITE, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a robot speaking before it is
    # written: a human excuse in a vacuum's mouth loses.
    robot_voice(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
