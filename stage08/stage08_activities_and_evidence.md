# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Mon 2:30 - 4:30 Group 1
Members/cohorts: 
    Kael (SomeKidWithCode), UG
    Ash (Ash-Salt08), UG
    Bailey (Sparkachu), UG
    Sushil (Sushil-Bhattarai-101), UG
Record owner / contribution links for each member:
I (Kael, u3334502) am the sole contributer for this stage as the changes were installed on my computer.

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

- Appointment disappears after cancellation: symptom
- Reason: Describes an observation

- The data-store removal path is probably being called: hypothesis/opinion
- Reason: Says 'probably'

- The failing test shows store.find_appointment('A1') returns None: evidence
- Reason: The test directly shows that there is an issue with the code

- The service layer is badly designed: hypothesis/opinion
- Reason: 'Bad design' is subjective

- Traceback points to smartcare/services.py line 42 in the example: evidence
- Reason: It's a direct piece of evidence pointing to a file and line number

The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Scenario: same-practitioner/time booking
Expected behaviour: Booking with same time/practitioner fails with error
Observed behaviour: Booking with same time/practitioner does not fail and is created without issue
Minimal reproduction: Register two appointments with the same practitioner and time
Hypothesis: Issue with the booking conflict checking function
Evidence: See 'Proof of baseline error 1.png' and 'Proof of baseline error 2.png'

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:
The test should be changed. Requirements come first over tests. But it would be a good idea for the test should be changed in order to match the new requirements.
Test exist to show that something follows the requirements it was made for. If the test fails because the requirement changed, then the test must change with it.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour.
* using strings for status is bad -> refactor to use enums instead, preserving names
* "The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture."
* not sure why there is print unless for specific reason -> remove unnessesary print statements
* nesting conditionals get confusing fast -> refactor to use fast failing instead of nesting, preserving the checks
Classify these proposed changes as refactoring, repair or feature:
- rename appt to appointment: refactoring
- extract a repeated conflict helper: refactoring
- add rescheduling: feature
- restore retained cancellation lookup: repair
- replace a magic status string with the existing enum: refactoring
Explain the behaviour that must remain unchanged.

Response and reason:
- rename appt to appointment: must maintain it's usage
- extract a repeated conflict helper: must maintain consistent functionality in all repeated usages
- replace a magic status string with the existing enum: must maintain correct enum usage

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:
* exception/assertion: `Failed: DID NOT RAISE ValueError` / the method must raise a value error
* expected and observed values: expected: error. observed: no error
* test line: `with pytest.raises(ValueError):` on line `127` in file `test_starter.py`
* application call path:
    - `test_conflict_rule_and_different_practitioner()` on line `119` in file `test_starter.py`
    - `with pytest.raises(ValueError):` on line `127` in file `test_starter.py`
    - `appointment_service.book_appointment('A2', 'P1', 'D1', when)` on line `128` in file `test_starter.py`
    - `book_appointment(self, str, str, str, datetime)` on line `96` in file `services.py`
    - `if self.data_store.has_practitioner_conflict(` on line `126` in file `services.py`
* supporting requirement: appointments must not overlap

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason:
If you just change the code, you will never know why it broke in the first place.
Debugging involves investgating why a particular bug happens, the steps the code takes in order for that bug to occur.
This means that just changing the code immediately have an issue happens doesn't mean more bugs won't happen in the future.

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6
- Baseline test command / working directory / observed result / evidence: 
    * `python -m pytest -vv`
    * `project/`
    * `FAILED tests/test_starter.py::test_conflict_rule_and_different_practitioner - Failed: DID NOT RAISE ValueError`
    * See 'Proof of baseline error 1.png' and 'Proof of baseline error 2.png'
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch:
    * debug/stage08, Pranav
    * It was created specifically for stage 8
- Downloaded tool version, source SHA256 and --check outcome:

    * `Stage 8 tool 1.1; preflight PASS; baseline SHA256 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6`

    * `Baseline Git SHA dff8c4326014f37c6e7b2547245c8864f7bedc42`

    * `CHECK ONLY: project unchanged; both proposed fault signatures verified in a temporary copy`

- --apply and --verify output summaries / artefact references:

    * `Stage 8 tool 1.1; preflight PASS; baseline SHA256 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6`

    * `Baseline Git SHA dff8c4326014f37c6e7b2547245c8864f7bedc42`

    * `PREPARED: F8-01 practitioner conflict; F8-02 retained-history lookup`

    * `Verified expected failures: test_f8_01_conflict; test_f8_02_history (2 failed)`

    * `Backup/hash recorded in .stage8_faults; use --restore for setup recovery only`

and

    `VERIFIED: exactly 2 expected failures; both approved symptom signatures present`
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: 1e804f451b1a9de42c67a38be9a9696029946ec6eb2319d37171fe5ba7a117f0
- Preparation or recovery issues and resolution, if any: N/A
- Initial prepared full-suite command / result / key failures:
python -m pytest -vv / 1 test failure / practitioner conflict detection failure

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: System is unable to detect appointment conflicts
- Expected behaviour and requirement: System detects appointment conflicts and throws an error
- Minimal synthetic reproduction steps: Create two bookings that have the same times and practitioners
- Meaningful failing test path/name and exact relevant failure:
    * `test_conflict_rule_and_different_practitioner()` on line `119` in file `test_starter.py`
    * `Failed: DID NOT RAISE ValueError`
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence:
    * Root cause: With `appointment.practitioner.practitioner_id != practitioner_id`, `!=` is supposed to be a `==`
    * Inspected code: See `F8-01 Inspected Code.png`
- Smallest justified fix / diff / why other behaviour is preserved:
    * Changed `!=` to `==`.
    * Other behaviour is preserved because the rest of the if statement correct compares time, appointment status and the appointment to ignore.
- Repair SHA / focused verification result: dda2f19a9f7d2715a5b9641132deae068304422a / See `F8-01 proof of now passing test.png`

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: Appointments are not removed from the appointments list
- Expected behaviour and requirement: Appointments are removed from the appointments list and stored in a different list
- Minimal synthetic reproduction steps: Create an apppointment, cancel it, then check if it's in the appointment list
- Meaningful failing test path/name and exact relevant failure:
    * `test_appointment_cancellation` on line `52` in file `test_services.py`
    * `AssertionError: assert not True`
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence:
    * Root cause: No call to remove the appointment from the appointment list is made
    * Inspected code: See `F8-01 Inspected Code.png`
- Smallest justified fix / diff / why other behaviour is preserved:
    * Added a item deletion line after the appointment cancelation
    * Other behaviour is preserved because the rest of the statement correctly cancels the booking and adds the canceled booking to a canceled bookings list.
- Repair SHA / focused verification result: 1400a8f40ed4dc0e9a98d15ebe929df8dfd40cbc / See `Proof of both passing tests.png`

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible:
`has_practitioner_conflict` would return false if two appointments had the same pracitioner ID.
This appears to be the opposite of what we want, being a true values if two appointments had the same pracitioner ID.
Evidence intended to inspect / competing explanation / discriminating check: ???
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible:
`cancel_appointment` in `services.py` does remove the canceled appointment from the appointments list.
This makes sense given the appointment could still be found in the appointments list.
Evidence intended to inspect / competing explanation / discriminating check: ???
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | bd4121e2855e23496147cb67759e851b1a035297 | `python -m pytest -vv` and `project/` | `Proof of baseline error 2.png` |
| F8-01 after repair | dda2f19a9f7d2715a5b9641132deae068304422a | `python -m pytest -vv` and `project/` | `F8-01 proof of now passing test.png` |
| F8-02 before repair | dda2f19a9f7d2715a5b9641132deae068304422a | `python -m pytest -vv` and `project/` | `F8-02 remaining assertion error.png` |
| F8-02 after repair | 1400a8f40ed4dc0e9a98d15ebe929df8dfd40cbc | `python -m pytest -vv` and `project/` | `Proof of both passing tests.png` |
| Full suite after both repairs, before refactor | 1400a8f40ed4dc0e9a98d15ebe929df8dfd40cbc | `python -m pytest -vv` and `project/` | `Proof of both passing tests.png` |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour:
* For F8-01, assertations detect the relevant incorrect result because a conflicting booking should throw a ValueError.
* For F8-02, assertations detect the relevant incorrect result because it is check whether the booking is still in the bookings list after being canceled.
* The previous behaviour is still protected by other assertations.
Unrelated failures investigated / resolution: N/A, no other failing tests

## H. Refactoring decision and before/after verification

Smell and exact location: Using 'magic strings' to check enums / `data_store.py` on line `94` and `112`.
Small proposed structural change / why justified: change to using enum value directly / changes to the enums could create issues as they would not change with the magic string.
External behaviour to preserve / relevant tests: usage of enum status's / `test_finding_appointments` and `test_conflict_rule_and_different_practitioner`
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA:
* `appointment.status.value == "scheduled"` to `appointment.status == AppointmentStatus.SCHEDULED`
* `appointment.status.value != "cancelled"` to `appointment.status != AppointmentStatus.CANCELLED`
* SHA: 87cb5f2258f53848baf0e34cdf30dad0c19b8bb8
Focused and full after-refactor commands / working directory / results / evidence:
`python -m pytest -vv` / `project/` / changes applied without issue, preserving behaviour / `See After enum usage fix with tests still passing.png`
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion:
Accepted, proper enum usage and removal of magic strings / behaviour preserved

## I. Git, human review and integration

Issues for both defects / refactor scope and owners:
F8-01: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/14 / `SmartCareDataStore` in `data_store.py` / SomeKidWithCode (Kael (u3334502))
F8-02: https://github.com/SomeKidWithCode/ST-Assignment-3/issues/15 / `AppointmentService` in `services.py` / SomeKidWithCode (Kael (u3334502))
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring?
Prevented refactoring from causing issues with other succeeding tests.

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: An engineer should analyse the reason for the failure. There was a reason why the failing code was designed the way it was. Therefore, it should be checked in case a particular functionality of the code needs to be preserved.

2. Where should expected behaviour come from during debugging?

Response: The feature's specification defines the expected behaviour.

3. What is a debugging hypothesis?

Response: A debugging hypothesis is simply a hypothesis as to how the bug you are debugging is happening.

4. What is a regression test and why is it retained?

Response: A regression test is a test that prevents the functionality of the system from regressing, getting worse. It is used when adding or modifiying features, where something might break already passing tests. The system should be able to both pass old tests and new ones.
It is retained because new code must not interrupt the functionality of old code. If you have a test that must pass now, then you should still have that test pass later as well.

5. What is meant by root cause?

Response: When you get an error, it's common that it comes with a stack trace. A stack trace is a chain of functions or methods that were called when this error happened. The root cause is the top most entry on the stack, that exact line of code/call that caused the error.

6. What is refactoring?

Response: Refactoring is process in which code is rewritten while preserving it's original function. It's effectively a term used when you have inefficient but working code and you want to improve it. You refactor it, keeping it's functionality while making it more efficient.

7. What is a swallowed exception?

Response: A swallowed exception is an error that the runtime does not report. This is reletively rare with most languages, but does happen. For example, if automatic library initialization fails at runtime, then the code that uses it might also fail. But it might not say that it was the library's fault, because it was not the one calling the initialization.

8. What is a code smell?

Response: A code smell is a way of saying that the code you are looking at isn't nessesarily wrong, but that it might violate standard coding principles of design. Basically, it's a way of saying 'this code just feels wrong'.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: (We are not using GitHub Copilot)

10. What is the Stage 8 engineering rule?

Response: 

## L. Completion and handover

- [X] Existing project, earlier tests and stage records preserved.
- [X] Passing Stage 7 SHA and safe preparation details recorded.
- [X] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [X] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [X] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [X] Tutorial, three reflections and ten formative responses complete.
- [X] Local recovery metadata excluded from submitted source.
- [X] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: N/A
Handover note: [complete]
