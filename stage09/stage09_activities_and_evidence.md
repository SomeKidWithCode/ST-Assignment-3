# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Mon 2:30 - 4:30 Group 1
Members and responsibilities:
  - Kael (SomeKidWithCode)
  - Ash (Ash-Salt08)
  - Bailey (Sparkachu)
  - Sushil (Sushil-Bhattarai-101)
Stage 8 integrated SHA, command, working directory and actual result:
Integrated SHA: 
Command: python -m pytest -vv
Working directory: project/
Actual result: ???

## A. Tutorial activities

### A1 Session state classification

| Information            | Required session/domain or transient state? | Requirement or reason                                                                                                                                                            |
| ---------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patient identity       | Required Domain                             | We keep a record of patients in order to allow staff to quickly rebook a patient without having to create a new patient ID and enter associated information.                     |
| Appointment history    | Required Domain                             | It is important for practitioners to be able to see a patients appointment history, as the context may be important.                                                             |
| Temporary menu choice  | Transient State                             | Storing each menu choice permanently will use a lot of space, and generally be difficult to check due to the sheer amount of choices made. The client also did not ask for this. |
| Practitioner specialty | Required Domain                             | This is not temporary information and will be required for ongoing operations of the clinic.                                                                                     |
| Debug print output     | Required Session                            | This should be retained through the session, but can be discarded between sessions, optionally saved permanently when needed.                                                    |
| Appointment status     | Required Domain                             | It is important for all stakeholders to see the status of various appointments, and as such this data needs to be retained.                                                      |

What is intentionally lost on exit? Temporary menu choices, anything entered into text fields that have not been saved to appointments.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
| --------------------- | ------------------------- | ------- | ----------------------------- | ----------------------------------- |
| appointment_sort_key | appointment: Appointment | tuple[datetime, str] |  |  |
| select_appointments | appointments: list, practitioner_id: str,<br>status: AppointmentStatus |  list[Appointment]|  |  |
| Service listing |  |  |  |  |
| Console |  |  |  |  |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: <!-- response -->

### A3 Responsibility violations

| Conceptual case                 | Violation | Correct boundary and reason                                                                |
| ------------------------------- | --------- | ------------------------------------------------------------------------------------------ |
| Appointment.cancel reads input  | No        | cancel function needs to read the input variable of the appointment chosen to be cancelled |
| Service prints/reads the menu   | Yes       | Menu/UI aspects are for the user. Service does not need to read these elements             |
| Query sorts its source in place | Yes       | Query only needs to read data, not change anything                                         |
| Store prints Appointment saved  | No        | It is important to show the user that the appointment has been saved.                      |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check:

`appointments.sort(key=appointment_sort_key)`:
    * source order: Order of creation/addition
    * return value: `None`
    * result identity: appointments, sorted

`result = sorted(appointments, key=appointment_sort_key)`
    * source order: Order of creation/addition
    * return value: `list[Appointment]`
    * result identity: new list, same elements, sorted

Score-example prediction and explanation of passing the named key:
Passing a key for sorting changes the sorting algorithm according to the function provided.
In this case, sorting priotises comparing the datetime object of each appointment.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: Cancellation differs from deletion in that cancellation is a toggle and part of appointment data, whereas deletion removes all data related to the appointment permanently.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
| ----------- | -------------------- | ----------------------------------- | ------------------------ | --------------- |
|             |                      |                                     |                          |                 |
|             |                      |                                     |                          |                 |
|             |                      |                                     |                          |                 |
|             |                      |                                     |                          |                 |
|             |                      |                                     |                          |                 |
|             |                      |                                     |                          |                 |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection:
* Empty is abscence of value. Unknown is 

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
| --------------------- | ------------- | ----------------------------- | ------------- | ------------- |
|                       |               |                               |               |               |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID     | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
| ---------------------------- | ------------------------------ | --------------- | ------------------------------- | ------------- |
| UI-01 full menu workflow     |                                |                 |                                 |               |
| UI-02 invalid-input recovery |                                |                 |                                 |               |
| Automated service workflow   |                                |                 |                                 |               |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: N/A
Actual response: N/A

To cut down on workload and ensure our work is high quality, we have not used AI for coding or designing in this assignment.

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
| ---------- | ------------------ | -------- | ------------------------------- | ------------------- | ------------------- |
|            |                    |          |                                 |                     |                     |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity?
`select_appointments` is pure because it returns the same thing when given the same inputs (it is consistent).
Side effects are things that do something intended, but also do something unintended. The example in this situation would be the comparison of `list.sort` and `sorted`. `list.sort` (a method on the list prototype) sorts the list. That's fine. But it sorts it in place, meaning that if you supply the original list from the datastore to the function, it would mutate the list from the data store (because it is the same list all the way through). This would be a side effect (unintended as well). However, `sorted` returns a new list with the sorted result.

2. Which explicit inputs are needed, and why avoid a global store?
`select_appointments` params are:
* `appointments: list[Appointment]`
* `practitioner_id: str`
* And optionally `status: AppointmentStatus | None`
Using a global store would involve querying something that is not directly involved with the function.
This is bad, because it detaches the purpose of both pieces of code by mixing responsibilites and usage.

3. How can a new list reuse Appointment objects safely?
As all Appointment instances are objects, it means that when you create a new list and append certain Appointments to it, they refer to the same object in the heap memory. For example:
`appt1 = Appointment()`
`appt2 = appt1`
`print(appt1 == appt2) # Prints True`
Because they are the same object. The variables are simply names to access the same thing.

4. Why use a named key, and what breaks equal-time ties?
Using a named key (explict sorting function) with `sorted` changes the default sorting behaviour. In this case, it priotises sorting by the descending datetime of the appointment.
Equal-time ties can't exist. You cannot book the same practitioner multiple times with the same time. But if you were to have two matching datetimes, it would likely then use the appointment ID to break the tie.

5. How do default and explicit status filters differ?
Functionally, default status applies no filtering and returns all appointments.
Explicit status returns only the status specified.

6. How do empty, unknown practitioner and invalid filter cases differ?
Empty filter case returns all appointments (the default behaviour).
Unknown practitioner throws an error because you need a practitioner to get the appointments of.
Invalid filter case also throws an error because you can only filter by valid cases.

7. Which console errors recover, and how is unchanged state checked?
The console is built to be durable in the sense that any time something can go wrong, it is caught and an appropriate message is printed.
State change protection is built into the function used by the console, so by extension, testing ensures that states are not changed.

8. What is data integrity for registered participants, conflicts and history?
Data integrity:
 * For registered participants, that their data isn't changed unnessesarily.
 * For conflicts, that the conflicting booking is changed or deleted etc to make room for the new one. The incoming booking is simply rejected.
 * For history (the canceled appointments), canceled appointments are retained and are still accessible.

9. What is Copilot's review role, and who verifies findings?
(None. We are not using AI.)
But, we, the engineers are the ones that would verify AI findings.
AI is capable of hallucinating, which can be castrophic if it fixed something it hallucinated was wrong.

10. How do pure functions and OOP responsibilities work together?
Pure functions are responsible for providing consistent outputs for other system.
OOP is responsible for containment of data in a consistent format.
Together, these form a system where the OOP side stores and manages data, while the pure functions provide consistent functionality when working with OOP.


## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
