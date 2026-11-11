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
   
    patient_alex = data_store.find_patient("P1")
    assert patient_alex is not None
   
    patient_steve = None
    try:
       patient_steve = data_store.find_patient("P2")
    except:
       print("Patient with ID \'P2\' correctly could not be found")
    assert patient_steve is None


def test_finding_pracitioners() -> None:
    '''Test practition storage finding'''
    data_store, patient, practitioner, appointment_service = foundation()

    practitioner_taylor = data_store.find_practitioner("D1")
    assert practitioner_taylor is not None

    practitioner_swift = None
    try:
        practitioner_swift = data_store.find_practitioner("D2")
    except:
        print("Practitioner with ID \'D2\' correctly could not be found")
    assert practitioner_swift is None

def test_finding_appointments() -> None:
    data_store, patient, practitioner, appointment_service = foundation()
    
    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    found_appointment = data_store.find_appointment("A1")

    assert found_appointment is not None
    assert found_appointment.status == AppointmentStatus.SCHEDULED
    assert found_appointment == appointment



def test_appointment_cancellation() -> None:
    data_store, patient, practitioner, appointment_service = foundation()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 19, 7)
    )

    assert appointment.status == AppointmentStatus.SCHEDULED
    appointment_service.cancel_appointment(appointment.appointment_id)
    assert appointment.status == AppointmentStatus.CANCELLED

    cancelled_twice = False
    try:
        appointment.cancel()
        cancelled_twice = True
    except:
        print("Correctly prevented double cancel")
    assert not cancelled_twice

    appointments = data_store.list_appointments()
    assert not appointments.__contains__(appointment)
