# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Mon 2:30 - 4:30 Group 1
- Members, GitHub usernames and cohorts:
  - Kael (SomeKidWithCode), UG
  - Ash (Ash-Salt08), UG
  - Bailey (Sparkachu), UG
  - Sushil (Sushil-Bhattarai-101), UG
- Repository URL: https://github.com/SomeKidWithCode/ST-Assignment-3
- Starting SHA: a38dbc262ff7127122cffc81be4cb86dcbb4799f

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Patient Search Feature
- Context: Practitioners and admin staff need to search for patients to see their name
- Requirement: System needs to be able to search patient records for a certain patient.
- Acceptance criteria: AC-02.1 / 02.2: Known patient lookup returns that patient; unknown patient reports absence.
- Scope: services.py
- Definition of Done: Search is able to retreive patient information when given the patient ID, and will return a relevant error when no match is found.
- Owner: Kael
- Actual issue link: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/6

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Appointment Cancellation with Retained Cancelled Appointments
- Context: Appointments may need to be cancelled due to patients needing to reschedule, or due to an error when making the booking.
- Requirement: System needs to mark appointments as cancelled
- Acceptance criteria: AC-05.1 / 05.2 / 05.3: Scheduled cancellation changes status; cancelled history remains retrievable this session; repeated cancellation is rejected.
- Scope: services.py
- Definition of Done: User is able to mark a specified appointment as cancelled, and can still retreive a cancelled appointment.
- Owner: Kael
- Actual issue link: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/7

## B Commit quality

| Original example                               | Strong or Weak | Reason                                                                                                              |
| ---------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------- |
| changes                                        | Weak           | Extremely inspecific and broad, does not adequetly convey the scope of the commit.                                  |
| final version                                  | Weak           | Software can be constantly changing, pegging the label "Final Version" to just one release can often be inaccurate. |
| Add patient search by ID                       | Strong         | Specific and expains exactly whar was changed.                                                                      |
| fix stuff                                      | Weak           | Extremely inspecific and broad, does not adequetly convey the scope of the commit.                                  |
| Prevent cancellation of completed appointments | Strong         | Specific and expains exactly what was changed.                                                                      |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: Editing files that are not in scope for changes made to cancelation system
- Responsibility and architecture concerns: [response]
- Testing and review concerns: Unrelated code restructures could change test results that previously passed
- Changes to remove or separate, with reasons: [response]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: What tests pass and why
- Follow-up review question 1: Which tests were run?
- Follow-up review question 2: Which tests passed/failed?
- Follow-up review question 3: Is there any room for improvement?
- Follow-up review question 4: Is there any additional tests we should run?
- Follow-up review question 5: Is it ready to commit?
- Additional questions if useful: N/A

## E Team workflow agreement

| Practice                            | Team agreement                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Branch naming                       | Each person gets their own branch to work on.                                                                                   |
| Commit message convention           | Consise, highlighting major changes.                                                                                            |
| PR size                             | Major, stage completion, or handover to other to complete.                                                                      |
| Another-member review requirement   | We are not currently accepting members.                                                                                         |
| Merge rule                          | Merging is only done when your section is finished or you need to make changes to the codebase.                                 |
| Significant Copilot disclosure rule | We have agreed not to use copilot in order to ensure quality and academic integrity, as well as generally simplify the project. |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link                                                  | Requirement                                                              | Owner | Acceptance criteria or precise link                                                                                                                  | Status |
| ----------------------------------------------------------- | ------------------------------------------------------------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| https://github.com/SomeKidWithCode/ST-Assignment-3/issues/6 | System needs to be able to search patient records for a certain patient. | Kael  | AC-02.1 / 02.2: Known patient lookup returns that patient; unknown patient reports absence.                                                          | Closed |
| https://github.com/SomeKidWithCode/ST-Assignment-3/issues/7 | System needs to mark appointments as cancelled                           | Ash   | AC-05.1 / 05.2 / 05.3: Scheduled cancellation changes status; cancelled history remains retrievable this session; repeated cancellation is rejected. | Closed |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: Pull Request Evidence- #8
  https://github.com/SomeKidWithCode/ST-Assignment-3/pull/8
- Linked issue and requirement: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/6
- Feature branch: Kael-Branch
- Changed behaviour: Includes changes to SmartCare services and tests, with a commit implementing patient and practitioner lookup functions.
- Meaningful commits: f979050 — 5 commits (including patient/practitioner lookup) Implemented patient and practitioner finding functions in services.py.
- Test command, directory and observed result: [response]
- Another-member reviewer: Ash-Salt08
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: Merged into main 0572d2c
- Significant Copilot assistance: None
- Linked issue closure: FR-02 Patient Search — Issue #6 & FR-06 Appointment Cancellation with FR-07 retained history — Issue #7
- Each member updated main: Sparka_chu
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

- Member: Ash
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: Created issue for FR-06
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: Most of stage 6, as well as organisation

- Member: Kael
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

- Member: Sushil
- Implementation: Not applicable. My main contribution focused on testing, review and documentation rather than direct software implementation.
- Testing: Completed Stage 7 testing activities, Parts B–I, including test design, test execution, requirement traceability and evaluation of test coverage. Added and improved tests in project/tests/test_domain.py and project/tests/test_services.py.
- Review: Reviewed test results and Copilot-generated test suggestions. Evaluated their usefulness and identified weak assertions that needed improvement.
- Issue refinement: Not applicable.
- Design and responsibility discussion: Reviewed testing requirements and considered whether the tests correctly represented the expected system behaviour.
- Debugging or integration: Ran the full pytest suite and verified the recorded result of 28 passed and 0 failed.
- Documentation or team support: Completed Stage 7 documentation and evidence for Parts B–I and Stage 12, Part M. Prepared testing explanations, reflections and formative question answers to support the project records.

- Member: Bailey
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: Pull Request
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

There is no minimum amount of changes needed to make a commit. A well organised commit makes only 1, significant change with sufficient detail in the comment.
A high commit account can be casued by a large amount of smaller, lower quality commits, indicating poor contribution to a project.

## L Stage 6 formative questions

1. What is version control?

Version control is a method for managing different versions of a program.
Such version differences my arise from experienmenting with new APIs, optimisations or feature additions

2. Why is a feature branch useful?

Feature branches are useful because it allows you to work on one specific feature of a system, without interference.
Let's say you want to work on a new feature, say an optimised data storage system.
A feature branch allows you to test the feature with the current system's specs.

3. What makes a commit a good engineering commit?

A good engineering commit is focused, meaningful and easy to understand.
It describes a specific change, avoids unrelated modifications and ideally leaves the code in a working, testable state.

4. What is a pull request?

A pull request is a query to grab changes from branch to branch.
If you make a branch and make changes on that branch, you will then need to request your changes on that branch to be pulled into the main branch.

5. What is the purpose of code review?

Code review helps another developer check that a change meets requirements, follows the intended architecture, includes relevant tests and does not introduce defects or unrelated changes.
It also shares knowledge across the team.

6. What does a Git diff show?

A Git diff shows lines, characters and files that have added or deleted.
It's a way to view what has changed from commits/pulls

7. What is a Definition of Done?

A Definition of Done is a description of something that must be complete for a task to be marked as done.
For example, a Definition of Done for an appointment registeration function might be that

- appointment is created
- appointment is checked for conflicting times/days/practitioners, etc
- appointment is either registered or rejected
  Basically a set of tests the task has to be pass to be considered a finished task

8. What is the appropriate role of GitHub Copilot in pull-request review?

An appropriate role of Github Copilot would be to summarize the changes made in the incoming pull request vs the main branch/whatever branch it's being pulled to.
Pull requests can be large and change a lot of files and code. So, creating a summary can be a useful and appropriate task.

9. Why should individual contribution not be judged only by commit count?

Because commits can be very small. You only need to add a space to the end of a line for it to be considered a commit-able thing.
Instead, commits should be judged on what was changed and by how much. This gives a better view as to what the commit actually changes.

10. What is the Stage 6 engineering rule?

## M Completion and handover

- Starting SHA: a38dbc262ff7127122cffc81be4cb86dcbb4799f
- Final Stage 6 code SHA:
- Test command: [response]
- Working directory: project/
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
