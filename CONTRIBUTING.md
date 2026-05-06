# Contributing

This repository is a theory and design toolkit for LLM agent skills.

## Contribution principles

1. Keep the core theory stable.
2. Prefer mapping new examples to existing control surfaces before adding new concepts.
3. Separate dated case studies from core theory.
4. Do not add repository rankings to core docs.
5. Do not add unverified claims about specific products or repositories.
6. Keep English as the primary language and update the Chinese version when changing core docs.
7. Treat safety as a hard constraint, not a footnote.

## Change process

For theory changes, include:

- what concept changed;
- why existing concepts were insufficient;
- what examples or failures motivated the change;
- what docs/templates/examples must be updated.

For template changes, include:

- which control surface is improved;
- what new cost or friction is introduced;
- how the change should be evaluated.

## Case studies

Add case studies only under `case-studies/` and include:

- observation date;
- repository URL;
- commit or tag if available;
- scope of analysis;
- ASCT control-surface mapping;
- what the case study teaches.

Do not put repository-specific judgments into the core theory docs.
