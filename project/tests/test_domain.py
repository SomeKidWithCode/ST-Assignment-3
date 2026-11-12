from datetime import datetime, timezone

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


def test_cancel_changes_status():
    '''Test that when canceling an appointment, the status of the appointment changes from booked to cancelled'''

    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )
    
    assert appointment.status == AppointmentStatus.SCHEDULED
    appointment.cancel()
    assert appointment.status == AppointmentStatus.CANCELLED


def test_patient_rejects_blank_name():
    with pytest.raises(ValueError):
        Patient("P2", "   ")


def test_practitioner_rejects_blank_specialty():
    with pytest.raises(ValueError):
        Practitioner("D2", "Alex", "   ")


def test_appointment_starts_as_scheduled():
    patient = Patient("P1", "John")
    practitioner = Practitioner("D1", "Alex", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 19, 7, 30)
    )

    assert appointment.status == AppointmentStatus.SCHEDULED
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner


def test_appointment_rejects_invalid_datetime():
    patient = Patient("P1", "John")
    practitioner = Practitioner("D1", "Alex", "General Practice")

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            patient,
            practitioner,
            datetime(2026, 11, 19, 7, 30, 15)
        )


def test_completed_appointment_cannot_be_cancelled():
    patient = Patient("P1", "John")
    practitioner = Practitioner("D1", "Alex", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 19, 7, 30),
        AppointmentStatus.COMPLETED
    )

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status == AppointmentStatus.COMPLETED


def test_repeated_cancellation_is_rejected():
    patient = Patient("P1", "John")
    practitioner = Practitioner("D1", "Alex", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 19, 7, 30)
    )

    appointment.cancel()

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status == AppointmentStatus.CANCELLED

def test_blank_patient_id_is_rejected():
    """Test that registering a patient with a blank ID raises ValueError."""

    data_store, patient, practitioner, appointment_service = foundation()

    patient_service = PatientService(data_store)

    with pytest.raises(ValueError):
        patient_service.register_patient(
            "     ",
            "John"
        )


@pytest.mark.parametrize(
    "appointment_datetime",
    [
        datetime(2026, 11, 19, 7, 0, tzinfo=timezone.utc),
        datetime(2026, 11, 19, 7, 0, 1, microsecond=1),
    ],
)
def test_appointment_rejects_timezone_or_microsecond_datetime(
    appointment_datetime,
):
    patient = Patient("P1", "John")
    practitioner = Practitioner("D1", "Alex", "General Practice")

    with pytest.raises(ValueError):
        Appointment(
            "A99",
            patient,
            practitioner,
            appointment_datetime,
        )

#@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
#def test_eval(test_input, expected):
#    assert eval(test_input) == expected
