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


def test_finding_patients() -> None:
    '''Test patient storage finding'''
    data_store, patient, practitioner, appointment_service = foundation()
    
    # Assertion 1. The known registered patient can be found
    patient_alex: Patient | None = data_store.find_patient("P1")
    assert patient_alex is not None

    # Assertion 2. A known unregistered patient cannot be found
    patient_steve: Patient | None = data_store.find_patient("P2")
    assert patient_steve is None


def test_finding_pracitioners() -> None:
    '''Test practition storage finding'''
    data_store, patient, practitioner, appointment_service = foundation()

    # Assertion 1. The known registered practitioner can be found
    practitioner_taylor: Practitioner | None = data_store.find_practitioner("D1")
    assert practitioner_taylor is not None

    # Assertion 2. A known unregistered practitioner cannot be found
    practitioner_swift: Practitioner | None = data_store.find_practitioner("D2")
    assert practitioner_swift is None


def test_finding_appointments() -> None:
    data_store, patient, practitioner, appointment_service = foundation()
    
    appointment: Appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    found_appointment: Appointment | None = data_store.find_appointment("A1")

    # Assertion 1. The appointment was found
    assert found_appointment is not None

    # Assertion 2. The appointment is booked
    assert found_appointment.status == AppointmentStatus.SCHEDULED

    # Assertion 3. The found appointment is the same object as the booked appointment
    assert found_appointment == appointment


def test_appointment_cancellation() -> None:
    data_store, patient, practitioner, appointment_service = foundation()

    appointment: Appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    # Assertion 1. The status changes from scheduled to canceled after cancel being called.
    assert appointment.status == AppointmentStatus.SCHEDULED
    appointment_service.cancel_appointment(appointment.appointment_id)
    assert appointment.status == AppointmentStatus.CANCELLED

    # Assertion 2. A ValueError is raised if you try to cancel an already canceled appointment
    with pytest.raises(ValueError):
        appointment.cancel()
    
    # Assertion 3. 
    appointments = data_store.list_appointments()
    assert not appointments.__contains__(appointment)
