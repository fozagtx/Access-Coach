from agents import function_tool

JARGON = [
    "synerg",
    "circle back",
    "bandwidth",
    "leverage",
    "asynchronous",
    "stakeholders",
    "kpi",
    "okr",
    "sla",
    "qbr",
    "eod",
    "cob",
    "oop",
    "wrt",
]


def lint_text(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return "No text provided to check."

    words = text.split()
    sentences = [
        s.strip()
        for s in text.replace("!", ".").replace("?", ".").split(".")
        if s.strip()
    ]
    findings: list[str] = []

    avg_len = (
        (sum(len(s.split()) for s in sentences) / len(sentences)) if sentences else 0
    )
    if avg_len > 22:
        findings.append(
            f"Long sentences (avg ~{avg_len:.0f} words). Aim for under 20."
        )
    if len(words) > 120:
        findings.append(
            f"Dense block ({len(words)} words). Add a short summary up top."
        )

    lower = text.lower()
    hit = [j for j in JARGON if j in lower]
    if hit:
        findings.append(f"Possible jargon/acronyms: {', '.join(hit)}")
    if text.isupper() and len(words) > 3:
        findings.append("ALL CAPS can feel shouty and harder to parse.")
    if not findings:
        findings.append("No major heuristic issues — still offer a clearer rewrite.")

    return (
        f"Accessibility lint for {len(words)} words / {len(sentences)} sentences:\n"
        + "\n".join(f"- {f}" for f in findings)
    )


@function_tool
async def accessibility_check(text: str) -> str:
    """Lint text for jargon, long sentences, and dense blocks before rewriting.

    Args:
        text: Message or thread excerpt to analyze.
    """
    return lint_text(text)
