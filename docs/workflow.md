# Evidence and Verification Workflow

Public releases in this repository are assembled from finished mathematical artifacts. Internal branches, pull requests, workspace histories, machine locations, and coordination records are not part of the public package.

## 1. Source contract

Each result identifies the original public source, the precise conjecture or question, and the hypotheses used in the public argument.

## 2. Result-type contract

Every release is classified by what it actually establishes:

- `COUNTEREXAMPLE`: a stated conjecture is refuted by an explicit witness.
- `COMPLETE_SOLUTION`: the cited problem is resolved throughout its stated scope.
- `FULL_THEOREM`: a theorem is proved for the full family named in the release.
- `PARAMETER_LAYER`: one complete parameter regime is settled without claiming the remaining regimes.
- `IN_PROGRESS`: material is still being curated or advanced and is not presented as a completed release.

## 3. Argument and certificate

The public package separates the mathematical argument from any executable certificate. Definitions, reductions, and proof boundaries are stated before computational evidence is invoked.

## 4. Computation boundary

Finite computation is used only where its logical role is explicit: checking a displayed witness, enumerating a proved finite remainder, or reproducing an exact certificate. It is not presented as a substitute for an unproved general step.

## 5. Verification record

Each release records the verification appropriate to its artifact, such as an independent mathematical review, a Lean check, or a symbolic argument accompanied by exhaustive exact enumeration. The status is stated without silently upgrading one form of verification into another.

## 6. Publication boundary

Public files contain only the mathematical material needed to understand, reproduce, and assess the released result. Private coordination, internal identifiers, timestamps, and unrelated work are excluded.

## 7. Priority boundary

Mathematical correctness and novelty or priority are tracked separately. Unless a dedicated literature review has established otherwise, the public status remains `NOT_ESTABLISHED`.
