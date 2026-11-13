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

from test_starter import foundation


def test_cancel_changes_status() -> None:
    '''Test that when canceling an appointment, the status of the appointment changes from booked to cancelled'''

    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    # Assertion 1. Check that the status changes after being canceled.
    assert appointment.status == AppointmentStatus.SCHEDULED
    appointment.cancel()
    assert appointment.status == AppointmentStatus.CANCELLED


def test_blank_patient_id_is_rejected() -> None:
    '''Test that when adding a patient, you cannot add a blank ID'''

    data_store, patient, practitioner, appointment_service = foundation()

    patient_service: PatientService = PatientService(data_store)

    # Assertion 1. A ValueError is raised if trying to register a patient with a blank ID
    with pytest.raises(ValueError):
        patient_service.register_patient(
            "     ",
            "John"
        )


#@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
#def test_eval(test_input, expected):
#    assert eval(test_input) == expected
