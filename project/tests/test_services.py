
from datetime import datetime

import pytest

from smartcare.domain import AppointmentStatus
from smartcare.services import PatientService, PractitionerService

from test_starter import foundation


def test_finding_patients() -> None:
    """Test patient service lookup."""
    data_store, patient, practitioner, appointment_service = foundation()

    patient_service = PatientService(data_store)

    patient_alex = patient_service.find_patient("P1")
    assert patient_alex is not None

    with pytest.raises(LookupError):
        patient_service.find_patient("P2")


def test_finding_practitioners() -> None:
    """Test practitioner service lookup."""
    data_store, patient, practitioner, appointment_service = foundation()

    practitioner_service = PractitionerService(data_store)

    practitioner_taylor = practitioner_service.find_practitioner("D1")
    assert practitioner_taylor is not None

    with pytest.raises(LookupError):
        practitioner_service.find_practitioner("D2")


def test_appointment_cancellation() -> None:
    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    assert appointment.status == AppointmentStatus.SCHEDULED

    cancelled = appointment_service.cancel_appointment("A1")

    assert cancelled.status == AppointmentStatus.CANCELLED
    assert cancelled in appointment_service.cancelled_appointments


def test_unknown_appointment_cancellation() -> None:
    data_store, patient, practitioner, appointment_service = foundation()

    with pytest.raises(LookupError):
        appointment_service.cancel_appointment("A99")


def test_repeated_appointment_cancellation() -> None:
    data_store, patient, practitioner, appointment_service = foundation()

    appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    appointment_service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment("A1")

    assert len(appointment_service.cancelled_appointments) == 1


def test_repeated_service_cancellation_preserves_state():
    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 19, 7, 0)
    )

    appointment_service.cancel_appointment("A1")

    appointments_before = data_store.list_appointments()
    history_before = list(appointment_service.cancelled_appointments)

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment("A1")

    assert data_store.find_appointment("A1") is appointment
    assert data_store.list_appointments() == appointments_before
    assert appointment_service.cancelled_appointments == history_before
    assert appointment.status == AppointmentStatus.CANCELLED


def test_conflicting_booking_does_not_change_state():
    data_store, patient, practitioner, appointment_service = foundation()

    original = appointment_service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 19, 7, 0)
    )

    with pytest.raises(ValueError):
        appointment_service.book_appointment(
            "A2", "P1", "D1", datetime(2026, 11, 19, 7, 0)
        )

    assert data_store.list_appointments() == [original]
    assert data_store.find_appointment("A2") is None
    assert original.status == AppointmentStatus.SCHEDULED


def test_cancelled_appointment_does_not_block_rebooking():
    data_store, patient, practitioner, appointment_service = foundation()

    first = appointment_service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 19, 7, 0)
    )

    appointment_service.cancel_appointment("A1")

    second = appointment_service.book_appointment(
        "A2", "P1", "D1", datetime(2026, 11, 19, 7, 0)
    )

    assert first.status == AppointmentStatus.CANCELLED
    assert second.status == AppointmentStatus.SCHEDULED
    assert data_store.list_appointments() == [first, second]
    assert appointment_service.cancelled_appointments == [first]



def test_find_appointment_distinguishes_unknown_from_blank_id():
    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1", "P1", "D1", datetime(2026, 11, 19, 7, 0)
    )

    # Existing appointment should be returned.
    assert appointment_service.find_appointment("A1") is appointment

    # Unknown ID should raise LookupError.
    with pytest.raises(LookupError):
        appointment_service.find_appointment("A99")

    # Blank ID should raise ValueError according to the docstring.
    with pytest.raises(ValueError):
        appointment_service.find_appointment("")

    with pytest.raises(ValueError):
        appointment_service.find_appointment(" ")

    # Rejected lookups must not change stored records.
    assert data_store.list_appointments() == [appointment]
    assert appointment_service.cancelled_appointments == []


def test_service_lookup_rejects_whitespace_ids():
    data_store, patient, practitioner, _ = foundation()

    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)

    with pytest.raises(ValueError):
        patient_service.find_patient(" ")

    with pytest.raises(ValueError):
        practitioner_service.find_practitioner(" ")

    # Original registered records must remain unchanged.
    assert data_store.find_patient("P1") is patient
    assert data_store.find_practitioner("D1") is practitioner
