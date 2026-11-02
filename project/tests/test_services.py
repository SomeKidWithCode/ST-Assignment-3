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


def test_finding_pracitioners_and_patients() -> None:
    '''Test patient storage finding'''
    patient_store = PatientService(SmartCareDataStore())

    patient_store.register_patient(
        "Zero",
        "John"
    )

    patient_zero = patient_store.find_patient("Zero")

    assert patient_zero is not None

    patient_one = None

    try:
        patient_one = patient_store.find_patient("One")
    except:
        print("Patient with ID \'One\' correctly could not be found")

    assert patient_one is None


    '''Test patient storage finding'''
    practitioner_store = PractitionerService(SmartCareDataStore())

    practitioner_store.register_practitioner(
        "Alpha",
        "Joe",
        "Quantum Physics"
    )

    practitioner_zero = practitioner_store.find_practitioner("Alpha")

    assert practitioner_zero is not None

    practitioner_one = None
    
    try:
        practitioner_one = practitioner_store.find_practitioner("One")
    except:
        print("Practitioner with ID \'One\' correctly could not be found")
    
    assert practitioner_one is None




def test_appointment_cancellation() -> None:
    patient_store = PatientService(SmartCareDataStore())
    
    patient = patient_store.register_patient(
        "Zero",
        "John"
    )

    practitioner_store = PractitionerService(SmartCareDataStore())
    
    practitioner = practitioner_store.register_practitioner(
        "Alpha",
        "Joe",
        "Quantum Physics"
    )


    data_store = SmartCareDataStore()

    data_store.add_patient(patient)
    data_store.add_practitioner(practitioner)

    appt_server = AppointmentService(data_store)

    appt = appt_server.book_appointment(
        "1",
        "Zero",
        "Alpha",
        datetime(2026, 11, 19, 7)
    )

    assert appt.status == AppointmentStatus.SCHEDULED

    appt.cancel()

    assert appt.status == AppointmentStatus.CANCELLED

    cancelled_twice = False

    try:
        appt.cancel()
        cancelled_twice = True
    except:
        print("Correctly prevented double cancel")

    assert not cancelled_twice
