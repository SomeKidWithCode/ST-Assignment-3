from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)
from smartcare.queries import (
    appointment_sort_key,
    select_appointments
)

from test_starter import foundation


""""""


def test_listing_practitioner_appointments():
    data_store, patient, practitioner, appointment_service = foundation()

    # Create a bunch of appointments
    new_appointments: list[Appointment] = []
    for i in range(10):
        new_appointments.append(
            appointment_service.book_appointment(
                f"A{2 + i}",
                "P1",
                "D1",
                datetime(2026 + i, 6, 4, 10)
            )
        )

    all_appointments = data_store.list_appointments()

    # Cancel certain appointments
    # Note that using the appointment's cancel method prevents it from being removed from the appointments dict
    canceled_appointments: list[Appointment] = [
        all_appointments[2],
        all_appointments[5],
        all_appointments[8]
    ]
    for appt in canceled_appointments:
        appt.cancel()


    # Assertion 1. Unknown practitioner raises LookupError
    with pytest.raises(LookupError):
        appointment_service.list_practitioner_appointments("D2")

    # Assertion 2. Not supplying status returns all appointments
    all_practitioner_appointments = appointment_service.list_practitioner_appointments("D1")
    assert same_elements(all_appointments, all_practitioner_appointments)

    # Assertion 3. Invalid status to filter by raises ValueError
    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments("D1", "invalid status") # type: ignore

    # Assertion 4. Supplying a specific status to filter by only returns appointments with that status
    all_canceled_practitioner_appointments = appointment_service.list_practitioner_appointments("D1", AppointmentStatus.CANCELLED)
    assert same_elements(canceled_appointments, all_canceled_practitioner_appointments)

    # Assertion 5. If there are no appointments matching the supplied status, list is empty
    all_completed_practitioner_appointments = appointment_service.list_practitioner_appointments("D1", AppointmentStatus.COMPLETED)
    assert len(all_completed_practitioner_appointments) == 0


def test_appointment_sort_key():
    '''Probably don't need this but tests look good so...'''
    data_store, patient, practitioner, appointment_service = foundation()

    appt = appointment_service.book_appointment(
        f"A2",
        "P1",
        "D1",
        datetime(2026, 6, 4, 10)
    )
    appt_sort_key = appointment_sort_key(appt)

    assert appt_sort_key[0] == appt.date_time
    assert appt_sort_key[1] == appt.appointment_id



# ----- Util stuff ----- #

# This is bad because it uses same-position checking as well but it works for now
def same_elements(a: list, b: list):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
