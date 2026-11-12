# Stage 7 Testing and Verification Record

Group/tutorial: Mon 2:30 - 4:30 Group 1
Members/cohorts: 
    Kael (SomeKidWithCode), UG
    Ash (Ash-Salt08), UG
    Bailey (Sparkachu), UG
    Sushil (Sushil-Bhattarai-101), UG
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register new patient | Register already existing patient | If the patient is already registered |
| FR-05 Prevent practitioner conflict | Practitioner is not already assigned to the appointment at the time | Practitioner is already assigned to the appointment at the time | Practitioner does not have an appointment already at that time |
| FR-06 Cancel appointment | Cancel schudeled appointment | Cancel canceled appointment | If the appointment is not schudeled |
| FR-07 Retain cancelled history | Canceled appointment is retained | Canceled appointment is not retained | Appointment can still be found somewhere |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Useless
Why: Assert will always be true and tests nothing

`assert appointment is not None`
Judgement: Medium
Why: While it is to-the-point, only if you should be expecting something is not None, say from a fetching function, should this be checked for.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Medium
Why: Defines that status should be canceled. But, it should be noted that `appointment.status != AppointmentStatus.BOOKED` and `appointment.status == AppointmentStatus.CANCELLED` are different and should be used in different circumstances.

`assert len(results) > 0`
Judgement: Weak
Why: If this is testing for if the something isn't blank, this would not work for spaces. Five spaces still have a length of 5. You need to trim the results to make sure it removes extra whitespace.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Useless
Why: `find_appointment` shouldn't be returning anything other than `Appointment` or `None`/an error. You should be able to infer what something returns by the method name.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract:
- Input: blank id
- Expected result: error -> ID cannot be plank
- Contract: must raise ValueError

- Input: whitespace-only name
- Expected result: error -> ID must have at least 1 non-whitespace character
- Contract: must raise ValueError

- Input: Same-time practitioner booking
- Expected result: error -> cannot have overlapping bookings
- Contract: must raise ValueError

- Input: Appointment canceled
- Expected result: appointment is retained
- Contract: Cancelled appointments are retained when canceled

- Input: Invalid state transition
- Expected result: error -> for example, cannot transition from a completed appointment to a canceled one
- Contract: Invalid state transitions are not allowed (in the case of cancelling, raise ValueError)

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | `not None` is not extensive enough | Test if object is the correct one |
| 2 | `not None` is not extensive enough | Test if passed values match returned object's values |
| 3 | Assert True does nothing | Actually test something |
| 4 | Assumes SMS notifications exist | Test what happens if SMS notifications are not available |
| 5 | Assumes SMS notifications exist | Test what happens when SMS notifications are wrong/malformed |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% code coverage can coexist with poor software verification because code coverage only states that the code runs and is used. It does NOT state the code itself is useful. For example, you could be calling checks or statements that don't realistically do anything.
Or you could be gathering info that isn't used.


## B Requirement to Test Traceability Matrix

The test IDs were allocated to organise the Stage 7 testing evidence. The tests cover patient registration, patient and practitioner searching, appointment booking, cancellation and validation.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| FR-01 Register patient | New patient registration succeeds | T07-B01 | Positive | `test_registration_and_booking()` / `test_starter.py` | A new patient is registered successfully and can be used for booking. | Previously reported PASS | Supplied |
| FR-01 Register patient | Duplicate patient registration is rejected | T07-B02 | Negative | `test_duplicate_patient_preserves_original()` / `test_starter.py` | Duplicate patient ID raises ValueError and preserves the original patient. | Previously reported PASS | Supplied |
| FR-05 Prevent practitioner conflict | AC-04.1: A practitioner cannot have two scheduled appointments at the same time | T07-B03 | Negative / Boundary | `test_conflict_rule_and_different_practitioner()` / `test_starter.py` | Conflicting booking is rejected, while a different practitioner can be booked at the same time. | Previously reported PASS | Supplied |
| FR-02 Patient Search | AC-02.1: Known patient lookup returns the registered patient | T07-B04 | Positive | `test_finding_patients()` / `test_services.py` | PatientService successfully returns an existing patient. | Test implemented; execution to be confirmed | Student-authored |
| FR-02 Patient Search | AC-02.2: Unknown patient reports absence | T07-B05 | Negative | `test_finding_patients()` / `test_services.py` | PatientService raises LookupError when the patient does not exist. | Test implemented; execution to be confirmed | Student-authored |
| FR-06 Appointment Cancellation | AC-05.1: A scheduled appointment can be cancelled | T07-B06 | Positive | `test_cancel_changes_status()` / `test_domain.py` | Appointment status changes from SCHEDULED to CANCELLED. | Test implemented; execution to be confirmed | Student-authored |
| FR-06 Appointment Cancellation | AC-05.1: Cancellation can be performed through AppointmentService | T07-B07 | Positive | `test_appointment_cancellation()` / `test_services.py` | AppointmentService successfully cancels a scheduled appointment. | Test implemented; execution to be confirmed | Student-authored |
| FR-07 Retained cancelled history | AC-05.2: A cancelled appointment remains stored and retrievable | T07-B08 | Positive / State | `test_cancelled_appointment_does_not_block_rebooking()` / `test_services.py` | The cancelled appointment remains in the data store after cancellation. | Test implemented; execution to be confirmed | Student-authored |
| FR-07 Retained cancelled history | AC-05.3: Repeated cancellation is rejected | T07-B09 | Negative / State | `test_repeated_service_cancellation_preserves_state()` / `test_services.py` | A second cancellation raises ValueError without changing the appointment or cancellation history. | Test implemented; execution to be confirmed | Student-authored |


---

## C Test Design

The following test cases were designed to check the SmartCare domain and service functionality. Both positive and negative tests were included to verify normal operations, invalid inputs and appointment state transitions.


| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| T07-C01 | Patient validation | Patient ID must not be blank | Negative | Check that a patient cannot be created with a whitespace-only ID. | Patient construction raises ValueError. | Directly checks patient ID validation. |
| T07-C02 | Patient validation | Patient name must not be blank | Negative | Check that a patient cannot be created with an empty or whitespace-only name. | Patient construction raises ValueError. | Checks patient name validation. |
| T07-C03 | Practitioner validation | Practitioner details must be valid | Negative | Check that a blank practitioner specialty is rejected. | Practitioner construction raises ValueError. | Adds practitioner specialty validation evidence. |
| T07-C04 | Appointment validation | Appointment must start with the correct status and valid participants | Positive | Check appointment creation, initial status and participant relationships. | Appointment starts as SCHEDULED and contains the correct patient and practitioner. | Checks initial appointment state and object relationships. |
| T07-C05 | Appointment validation | Appointment requires valid date and time | Negative / Boundary | Check that an appointment with invalid date/time precision is rejected. | Appointment construction raises ValueError. | Checks date/time validation. |
| T07-C06 | FR-06 Appointment Cancellation | AC-05.1: Scheduled appointment can be cancelled | Positive | Check that cancelling a scheduled appointment changes its status. | Status changes to CANCELLED. | Provides direct domain-level cancellation evidence. |
| T07-C07 | FR-06 Appointment Cancellation | Only eligible appointments can be cancelled | Negative / State | Check that a completed appointment cannot be cancelled. | ValueError is raised and status remains COMPLETED. | Checks illegal state-transition protection. |
| T07-C08 | FR-06 Appointment Cancellation | Repeated cancellation is rejected | Negative / State | Check that an already cancelled appointment cannot be cancelled again. | ValueError is raised and status remains CANCELLED. | Checks repeated cancellation at domain level. |
| T07-C09 | Appointment validation | Appointment datetime must use local minute precision | Negative / Boundary | Check timezone-aware and nonzero-microsecond datetime values. | Appointment construction raises ValueError. | Adds further datetime boundary coverage. |

### Explanation of test design

- **Positive tests:** Verify that valid patients, practitioners and appointments can be created and that valid operations succeed.
- **Negative tests:** Verify that invalid information and illegal operations are rejected using the correct exceptions.
- **Boundary tests:** Check special datetime values and repeated operations that could cause unexpected behaviour.
- **State tests:** Verify that an unsuccessful operation does not accidentally change existing appointment records or status.

---

## D Arrange Act Assert Record

Test data is prepared first, one meaningful action is performed, and the expected result is checked

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| T07-C01 | Prepare a patient ID containing only spaces and a valid name. | Create a Patient object with the invalid ID. | `pytest.raises(ValueError)` | Proves that a patient cannot be created without a valid ID. |
| T07-C02 | Prepare a valid patient ID and a whitespace-only name. | Create a Patient object. | `pytest.raises(ValueError)` | Proves that patient names must contain valid text. |
| T07-C03 | Prepare a practitioner with a valid ID and name but blank specialty. | Create a Practitioner object. | `pytest.raises(ValueError)` | Proves that practitioner specialty is validated. |
| T07-C04 | Prepare valid Patient and Practitioner objects. | Create an Appointment using those objects. | Check SCHEDULED status and object identity using `is`. | Proves that the appointment starts correctly and maintains the correct participant relationships. |
| T07-C05 | Prepare valid Patient and Practitioner objects and an invalid datetime. | Create an Appointment using the invalid datetime. | `pytest.raises(ValueError)` | Proves that invalid appointment date/time values are rejected. |
| T07-C06 | Create an appointment with SCHEDULED status. | Call `appointment.cancel()`. | Assert `appointment.status == AppointmentStatus.CANCELLED`. | Proves that a scheduled appointment can be cancelled successfully. |
| T07-C07 | Create an appointment with COMPLETED status. | Attempt to call `appointment.cancel()`. | `pytest.raises(ValueError)` and check that status remains COMPLETED. | Proves that an illegal cancellation does not change the appointment state. |
| T07-C08 | Create a scheduled appointment and cancel it once. | Attempt to cancel the same appointment again. | `pytest.raises(ValueError)` and check that status remains CANCELLED. | Proves that repeated cancellation is rejected without changing the existing state. |
| T07-C09 | Prepare valid participant objects and timezone-aware or nonzero-microsecond datetime values. | Create an Appointment using each invalid datetime. | `pytest.raises(ValueError)` for both parameterised cases. | Proves that appointment datetime validation handles additional boundary conditions. |

The AAA approach makes the tests easier to understand, maintain and verify. It also ensures that each test checks a specific expected behaviour rather than performing several unrelated operations.

---
## E Domain Test Evidence

Domain tests were written to verify Patient, Practitioner and Appointment construction, validation and state transitions.

The tests check that invalid patient and practitioner information is rejected, appointments begin with the correct status, and cancellation rules are enforced.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| T07-C01 | Rejects a blank patient ID. | `tests/test_domain.py` / `test_blank_patient_id_is_rejected()` | PASS |
| T07-C02 | Rejects a blank patient name. | `tests/test_domain.py` / `test_patient_rejects_blank_name()` | PASS |
| T07-C03 | Rejects a blank practitioner specialty. | `tests/test_domain.py` / `test_practitioner_rejects_blank_specialty()` | PASS |
| T07-C04 | Checks that an appointment starts as SCHEDULED and contains the correct participants. | `tests/test_domain.py` / `test_appointment_starts_as_scheduled()` | PASS |
| T07-C05 | Rejects an invalid appointment datetime. | `tests/test_domain.py` / `test_appointment_rejects_invalid_datetime()` | PASS |
| T07-C06 | Changes appointment status from SCHEDULED to CANCELLED. | `tests/test_domain.py` / `test_cancel_changes_status()` | PASS |
| T07-C07 | Prevents cancellation of a completed appointment. | `tests/test_domain.py` / `test_completed_appointment_cannot_be_cancelled()` | PASS |
| T07-C08 | Rejects repeated cancellation of an appointment. | `tests/test_domain.py` / `test_repeated_cancellation_is_rejected()` | PASS |
| T07-C09 | Rejects timezone-aware and nonzero-microsecond datetime values. | `tests/test_domain.py` / `test_appointment_rejects_timezone_or_microsecond_datetime()` | PASS (2 parameterised cases) |

**Domain test execution command:**

```bash
python -m pytest tests/test_domain.py -v
```

**Execution evidence:**

The complete test suite was executed using `python -m pytest -v`. All 10 domain test cases passed successfully. No domain test failures were reported.

---

## F Service Test Evidence

Service-level tests were written to verify patient and practitioner searching, appointment cancellation, booking conflicts and the preservation of stored data.

The tests use the shared `SmartCareDataStore` and the `foundation()` helper to prepare the required registered objects and appointment service.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| T07-F01 | Finds an existing patient and rejects an unknown patient ID. | FR-02 / AC-02.1 and AC-02.2 | `test_finding_patients()` | PASS |
| T07-F02 | Finds an existing practitioner and rejects an unknown practitioner ID. | Practitioner lookup requirement | `test_finding_practitioners()` | PASS |
| T07-F03 | Successfully cancels an appointment and adds it to cancellation history. | FR-06 / AC-05.1 | `test_appointment_cancellation()` | PASS |
| T07-F04 | Rejects cancellation of an unknown appointment. | Appointment lookup and cancellation validation | `test_unknown_appointment_cancellation()` | PASS |
| T07-F05 | Rejects repeated appointment cancellation. | FR-07 / AC-05.3 | `test_repeated_appointment_cancellation()` | PASS |
| T07-F06 | Preserves appointment and cancellation history after repeated cancellation. | FR-07 / AC-05.3 | `test_repeated_service_cancellation_preserves_state()` | PASS |
| T07-F07 | Rejects a conflicting booking without changing existing appointments. | FR-05 | `test_conflicting_booking_does_not_change_state()` | PASS |
| T07-F08 | Allows another appointment after the previous appointment has been cancelled. | FR-05 / FR-07 | `test_cancelled_appointment_does_not_block_rebooking()` | PASS |
| T07-F09 | Distinguishes between existing, unknown and blank appointment IDs. | Appointment lookup validation | `test_find_appointment_distinguishes_unknown_from_blank_id()` | PASS |
| T07-F10 | Rejects whitespace-only patient and practitioner lookup IDs. | Patient and practitioner lookup validation | `test_service_lookup_rejects_whitespace_ids()` | PASS |

### Important service test observations

- Existing patient and practitioner records can be retrieved using their IDs.
- Unknown records raise `LookupError`.
- Blank or whitespace-only IDs raise `ValueError`.
- A conflicting appointment is not stored.
- A cancelled appointment remains in the data store.
- Repeated cancellation does not duplicate cancellation history or modify the existing appointment.
- A cancelled appointment does not prevent a new appointment from being booked at the same time.

**Service test execution command:**

```bash
python -m pytest tests/test_services.py -v
```

**Execution evidence:**

The complete test suite was executed using `python -m pytest -v`. All 10 service test cases passed successfully. No service test failures were reported.
---

## G Negative and Boundary Cases

Negative and boundary tests were included to ensure that the SmartCare system handles invalid inputs and unsuccessful operations safely.

These tests also check that existing records and appointment states remain unchanged when an operation is rejected.

| Behaviour | Boundary / invalid input | Expected result | Test ID |
|---|---|---|---|
| Patient ID validation | Blank patient ID | `ValueError` is raised and no invalid patient is registered. | T07-C01 |
| Patient name validation | Whitespace-only patient name | `ValueError` is raised. | T07-C02 |
| Practitioner validation | Whitespace-only practitioner specialty | `ValueError` is raised. | T07-C03 |
| Appointment validation | Invalid appointment datetime containing seconds | `ValueError` is raised. | T07-C05 |
| Appointment validation | Timezone-aware datetime | `ValueError` is raised. | T07-C09 |
| Appointment validation | Datetime with nonzero microseconds | `ValueError` is raised. | T07-C09 |
| Cancellation | Attempt to cancel a completed appointment | `ValueError` is raised and status remains COMPLETED. | T07-C07 |
| Cancellation | Attempt to cancel an already cancelled appointment | `ValueError` is raised and status remains CANCELLED. | T07-C08 |
| Patient lookup | Unknown patient ID | `LookupError` is raised. | T07-F01 |
| Practitioner lookup | Unknown practitioner ID | `LookupError` is raised. | T07-F02 |
| Appointment lookup | Unknown appointment ID | `LookupError` is raised. | T07-F09 |
| Appointment lookup | Blank or whitespace-only appointment ID | `ValueError` is raised. | T07-F09 |
| Service lookup | Whitespace-only patient or practitioner ID | `ValueError` is raised and existing records remain unchanged. | T07-F10 |
| Appointment cancellation | Unknown appointment ID | `LookupError` is raised and no appointment is changed. | T07-F04 |
| Booking conflict | Same practitioner booked at the same time | `ValueError` is raised and the original appointment remains unchanged. | T07-F07 |
| Rebooking | Booking the same time after the previous appointment is cancelled | New appointment is accepted and the previous cancellation remains recorded. | T07-F08 |
| Repeated service cancellation | Second cancellation attempt | `ValueError` is raised and appointment state and cancellation history remain unchanged. | T07-F06 |

### Evaluation of additional test ideas

Additional test ideas were reviewed to improve the reliability of the SmartCare test suite.

| Candidate | Copilot-generated test idea | Human assessment | Decision | Reason |
|---|---|---|---|---|
| C1 | Check whether repeated cancellation preserves appointment state and history. | Useful boundary test. | Modify / strengthen | Additional assertions check the stored appointment, its status and unchanged cancellation history. |
| C2 | Check whether a conflicting booking changes stored appointments. | Relevant negative test. | Accept | Confirms that a rejected booking does not change the original appointment or add an invalid record. |
| C3 | Check whether a cancelled appointment allows rebooking at the same time. | Useful interaction test. | Accept | Confirms that cancellation does not incorrectly block a new appointment. |
| C4 | Reject timezone-aware and microsecond datetime values. | Relevant datetime boundary test. | Accept | Adds evidence for the appointment minute-precision validation rule. |
| C5 | Reject whitespace-only patient and practitioner lookup IDs. | Useful validation test. | Modify | Checks invalid IDs and verifies that existing registered records remain available. |
| C6 | Distinguish unknown and blank appointment IDs. | Useful error-handling test. | Modify | Checks that unknown IDs raise `LookupError` while blank IDs raise `ValueError`. |
| C7 | List appointments for a practitioner. | Outside current implemented functionality. | Reject / Defer | This is Stage 9 functionality and should not be included as completed Stage 7 evidence. |

### Final test execution evidence

The complete test suite was executed with the following command:

```bash
python -m pytest -v
```

The terminal output confirmed:

| Test file | Tests passed |
|---|---:|
| `tests/test_domain.py` | 10 |
| `tests/test_services.py` | 10 |
| `tests/test_starter.py` | 8 |
| **Total** | **28** |

**Final result: 28 passed in 0.02 seconds.**

There were no failed tests or errors.

### Reflection (B to G)

**1. Which Copilot-generated test looked convincing but was weak?**

The repeated-cancellation test initially appeared sufficient because it checked whether a `ValueError` was raised. However, checking only the exception did not prove that the appointment status and cancellation history remained unchanged.

**2. How was it strengthened?**

The test was improved by checking the appointment's identity in the data store, its CANCELLED status, the stored appointment list and the cancellation history before and after the second cancellation attempt.

**3. What does the test suite still not prove?**

The test suite does not prove that every possible invalid input is handled correctly. For example, the whitespace-only ID tests do not check every possible non-string input, such as `None`. It also does not test practitioner appointment listing because that functionality belongs to a later stage and has not been implemented.

### Conclusion (B to G)

The Stage 7 testing work covers important SmartCare domain and service behaviours. The tests verify patient and practitioner validation, appointment construction, appointment cancellation, searching, booking conflicts and error handling.

Additional student-authored tests improve the original starter evidence by checking boundary conditions and ensuring that rejected operations do not change existing records or appointment states.

Copilot-generated suggestions were reviewed rather than accepted automatically. Useful tests were accepted or strengthened, while functionality belonging to Stage 9 was deferred.

The final execution confirmed that all 28 tests passed successfully in 0.02 seconds. This provides evidence that the current domain, service and starter test cases work as expected.

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| `python -m pytest` | `project/` | 80029272a86a303d3f094471875cf9efd7106ca8 | 13 | 0 | N/A | N/A | 'Proof of all tests passing.png' |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: N/A
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? The test suite does not prove that all paths of all functions of all systems are run and produce the intended result.
Coverage if used: Not used
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? N/A?
Optional fixtures/parametrisation used and why, if any: Not used

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
Verification ensures the system is working based on the requirements defined for it.

2. What question does validation answer?
Validation ensures the system is working as intended for the user based on expected behaviour.

3. What is a unit test?
A unit test is test that tests a particular part of the system without dependency on the rest of the system.
Like a function or method.

4. What is a pytest fixture?
A pytest fixture would be a constant used in testing python code.
In our case, the foundation method in test_starter.py defines testing data to use.
It ensures that the testing data used across tests is consistent.

5. What is parametrisation in pytest?
Parametrisation is a functionality of pytest that allows you to run a testing function multiple times with different inputs.
This allows you to catch parameter edge cases.

6. What is regression testing?
Regression testing is a form of testing where you run a set of tests, change something, then run the tests again.
Basically, it's a method of testing where the tests that have passed previously continue to pass as you add/change things.
This includes adding tests to test things you add/change.

7. What does code coverage tell us, and what does it not prove?
Code coverage describes how much of your code runs.
Things like if statements, function usage, variable variability, etc.
It's a way of measuring how much of your code is actually doing something.
It's also a method for finding dead code, or code that isn't used, or checks that don't need to be run.

However, it doesn't tell you if that code you wrote can be improved or condensed. 

8. What makes an assertion weak?
A weak assertion is one that doesn't prove anything or doesn't measure a change or condition.
Assertation is used to make sure something is in a particular state, such that a newly-created booking is scheduled.

9. What is the appropriate role of GitHub Copilot as a test assistant?
(Nothing. I don't want to use it.)

10. What is the Stage 7 engineering rule?


## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: All tests complete
Unresolved defects and effect on baseline: None
Clean working tree and integration evidence: [complete]
Stage 8 handover status: complete; no Stage 8 work assigned
All tutorial/formative responses and traceability/Copilot decisions complete: Yes
