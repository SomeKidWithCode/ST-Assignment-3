# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Mon 2:30 - 4:30 Group 1
- Members, GitHub usernames and cohorts: [response]
- Repository URL: https://github.com/SomeKidWithCode/ST-Assignment-3
- Starting SHA: a38dbc262ff7127122cffc81be4cb86dcbb4799f

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Patient Search Feature
- Context: [response]
- Requirement: System needs to be able to search patient records for a certain patient
- Acceptance criteria: [response]
- Scope: services.py
- Definition of Done: [response]
- Owner: Kael
- Actual issue link: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/6

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Appointment Cancellation with Retained Cancelled Appointments
- Context: [response]
- Requirement: [response]
- Acceptance criteria: [response]
- Scope: services.py
- Definition of Done: [response]
- Owner: Kael
- Actual issue link: [response]

## B Commit quality

| Original example                               | Strong or Weak | Reason                                                                                                              |
| ---------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------- |
| changes                                        | Weak           | Extremely inspecific and broad, does not adequetly convey the scope of the commit.                                  |
| final version                                  | Weak           | Software can be constantly changing, pegging the label "Final Version" to just one release can often be inaccurate. |
| Add patient search by ID                       | Strong         | Specific and expains exactly whar was changed.                                                                      |
| fix stuff                                      | Weak           | Extremely inspecific and broad, does not adequetly convey the scope of the commit.                                  |
| Prevent cancellation of completed appointments | Strong         | Specific and expains exactly whar was changed.                                                                      |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: Editing files that are not in scope for changes made to cancelation system
- Responsibility and architecture concerns: [response]
- Testing and review concerns: Unrelated code restructures could change test results that previously passed
- Changes to remove or separate, with reasons: [response]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [response]
- Follow-up review question 1: [response]
- Follow-up review question 2: [response]
- Follow-up review question 3: [response]
- Follow-up review question 4: [response]
- Follow-up review question 5: [response]
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice                            | Team agreement |
| ----------------------------------- | -------------- |
| Branch naming                       | Each person gets their own branch to work on     |
| Commit message convention           | [response]     |
| PR size                             | [response]     |
| Another-member review requirement   | [aren't the groups locked?]     |
| Merge rule                          | merging is only done when your section is finished or you need to make changes to the codebase     |
| Significant Copilot disclosure rule | [response]     |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner      | Acceptance criteria or precise link | Status     |
| ---------- | ----------- | ---------- | ----------------------------------- | ---------- |
| [issue 1]  | [response]  | [response] | [response]                          | [response] |
| [issue 2]  | [response]  | [response] | [response]                          | [response] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[response]

## L Stage 6 formative questions

1. What is version control?

Version control is a method for managing different versions of a program.
Such version differences my arise from experienmenting with new APIs, optimisations or feature additions


2. Why is a feature branch useful?

Feature branches are useful because it allows you to work on one specific feature of a system, without interference.
Let's say you want to work on a new feature, say an optimised data storage system.
A feature branch allows you to test the feature with the current system's specs.


3. What makes a commit a good engineering commit?




4. What is a pull request?

A pull request is a request to pull changes from branch to branch.
If you make a branch and make changes on that branch, you will then need to request your changes on that branch to be pulled into the main branch.


5. What is the purpose of code review?




6. What does a Git diff show?

A Git diff shows lines, characters and files that have added or deleted.
It's a way to view what has changed from commits/pulls


7. What is a Definition of Done?

A Definition of Done is a description of something that must be complete for a task to be marked as done.
For example, a Definition of Done for an appointment registeration function might be that
* appointment is created
* appointment is checked for conflicting times/days/practitioners, etc
* appointment is either registered or rejected
Basically a set of tests the task has to be pass to be considered a finished task


8. What is the appropriate role of GitHub Copilot in pull-request review?

An appropriate role of Github Copilot would be to summarize the changes made in the incoming pull request vs the main branch/whatever branch it's being pulled to.
Pull requests can be large and change a lot of files and code. So, creating a summary can be a useful and appropriate task.


9. Why should individual contribution not be judged only by commit count?

Because commits can be very small. You only need to add a space to the end of a line for it to be considered a commit-able thing.
Instead, commits should be judged on what was changed and by how much. This gives a better view as to what the commit actually changes.


10. What is the Stage 6 engineering rule?




## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
