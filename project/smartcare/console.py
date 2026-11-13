"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Patient, Practitioner, Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)
import random


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')


def run_menu() -> None:
    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """

    # Initialize SmartCare services and domains
    data_store: SmartCareDataStore = SmartCareDataStore()
    patients: PatientService = PatientService(data_store)
    practitioners: PractitionerService = PractitionerService(data_store)
    appointments: AppointmentService = AppointmentService(data_store)

    practitioners.register_practitioner("bruh", "Docktor", "Everything")

    # Create options dictionary
    options: dict[int, str] = {
        1: "Register patient",
        2: "Find patient",
        3: "Book appointment",
        4: "Cancel appointment",
        5: "List practitioner\'s appointments",
        6: "Exit"
    }

    # Print welcome message
    print("#################### - SMARTCARE - ####################")
    print("      Welcome to the SmartCare Hospital Interface      ")
    print("#################### - SMARTCARE - ####################")
    print("\n(Please note that all session data is lost on exit)\n")


    exit: bool = False

    # Main loop, exited on exit
    while not exit:
        # List options
        print("\nOptions:")
        for opt in options:
            print(f"\t{opt}: {options[opt]}")

        user_input: str = input("\nSelect option [1-6]: ")

        try:
            user_input_num: int = int(user_input)

            if user_input_num >= 1 and user_input_num <= 6:
                print(f"\nSelected \'{options[user_input_num]}\'")

            if user_input_num == 1:
                getting_patient_name: bool = True
                while getting_patient_name:
                    patient_name: str = input("\nEnter patient name: ")

                    try:
                        # The chance that two random integers are the same are very low so this should provide acceptable randomness
                        patient_id: str = random_id()
                        patients.register_patient(patient_id, patient_name)

                        getting_patient_name = False

                        print("\nPatient registered:")
                        print(f"\tID #{patient_id}")
                        print(f"\tName: {patient_name}")
                    except ValueError:
                        print(f"Name cannot be blank or only whitespace.")
                        print(f"Please try again.")

            elif user_input_num == 2:
                patient_name: str = input("\nEnter patient name: ")

                found_patients: list[Patient] = []
                for patient in data_store.list_patients():
                    if patient.name.lower().startswith(patient_name.lower()):
                        found_patients.append(patient)

                if len(found_patients) == 0:
                    print(f"Could not find any patients with name \'{patient_name}\'")
                else:
                    print(f"Found {len(found_patients)} patients that start with \'{patient_name}\':")
                    for found_patient in found_patients:
                        print(f"Patient {found_patients.index(found_patient) + 1}:")
                        print(f"\tID #{found_patient.patient_id}")
                        print(f"\tName: {found_patient.name}")
                        print()

            elif user_input_num == 3:
                # Get all practitioners and patients
                all_practitioners: list[Practitioner] = data_store.list_practitioners()
                all_patients: list[Patient] = data_store.list_patients()

                booking_appointment: bool = True
                while booking_appointment:
                    # Get the practitioner for the appointment
                    practitioner: Practitioner | None = None
                    getting_practitioner_name: bool = True
                    while getting_practitioner_name:
                        practitioner_name: str = input("\nEnter practitioner name: ").lower()

                        if practitioner_name.strip() == "":
                            print("Practitioner name cannot be blank")
                            continue
                    
                        lowercase_practitioner_names: list[str] = []
                        for practitioner in all_practitioners:
                            lowercase_practitioner_names.append(practitioner.name.lower())
                    
                        any_practitoner_that_starts_with_that_str: bool = False
                        practitioner_index: int = -1
                        for lc_pat_name in lowercase_practitioner_names:
                            if lc_pat_name == practitioner_name:
                                any_practitoner_that_starts_with_that_str = True
                                practitioner_index = lowercase_practitioner_names.index(lc_pat_name)
                                break
                    
                        if any_practitoner_that_starts_with_that_str:
                            practitioner = all_practitioners[practitioner_index]
                            getting_practitioner_name = False
                        else:
                            print("There is no practitioner with that name")
                            print("Please try again")
                    
                    
                    # Get the patient for the appointment
                    patient: Patient | None = None
                    getting_patient_name: bool = True
                    while getting_patient_name:
                        patient_name: str = input("\nEnter patient name: ").lower()

                        if patient_name.strip() == "":
                            print("Patient name cannot be blank")
                            continue
                    
                        lowercase_patient_names: list[str] = []
                        for patient in all_patients:
                            lowercase_patient_names.append(patient.name.lower())
                    
                        any_practitoner_that_starts_with_that_str: bool = False
                        patient_index: int = -1
                        for lc_pat_name in lowercase_patient_names:
                            if lc_pat_name == patient_name:
                                any_practitoner_that_starts_with_that_str = True
                                patient_index = lowercase_patient_names.index(lc_pat_name)
                                break
                    
                        if any_practitoner_that_starts_with_that_str:
                            patient = all_patients[patient_index]
                            getting_patient_name = False
                        else:
                            print("There is no patient with that name")
                            print("Please try again")
                    
                    appointment_date: datetime | None = None
                    getting_appointment_date: bool = True
                    while getting_appointment_date:
                        appointment_time: str = input("\nEnter appointment time (Please use YYYY-MM-DD HH:MM format): ")
                    
                        try:
                            appointment_date = parse_date_time(appointment_time)
                            getting_appointment_date = False
                        except ValueError:
                            print("That format was not accepted.")
                            print("Please try again.")

                    
                    appt_id: str = random_id()

                    try:
                        appt: Appointment = appointments.book_appointment(
                            appt_id,
                            patient.patient_id,
                            practitioner.practitioner_id,
                            appointment_date
                        )

                        booking_appointment = False
                        
                        print("Appointment booked")
                        print(f"\tID #{appt.appointment_id}")
                        print(f"\tPractitioner: {practitioner.name}")
                        print(f"\tPatient: {patient.name}")
                        print(f"\tStatus: Scheduled")
                    except ValueError:
                        print("There is already an appointment with that time booked.")
                        print("Please try again.")


            elif user_input_num == 4:
                all_appointments: list[Appointment] = data_store.list_appointments()

                scheduled_appointments: list[Appointment] = [appt for appt in all_appointments if appt.status == AppointmentStatus.SCHEDULED]

                print("Select an appointment to cancel:\n")
                for appt in scheduled_appointments:
                    print(f"{scheduled_appointments.index(appt) + 1}:")
                    print(f"\tID #{appt.appointment_id}")
                    print(f"\tPractitioner: {practitioner.name}")
                    print(f"\tPatient: {patient.name}")
                    print()

                canceling_an_appointment: bool = True
                while canceling_an_appointment:
                    appt_id_to_cancel: str = input("Enter appointment ID (or exit to exit): ")

                    if appt_id_to_cancel.strip().lower() == "exit":
                        break

                    try:
                        canceled_appt: Appointment = appointments.cancel_appointment(appt_id_to_cancel)
                        canceling_an_appointment: bool = False

                        print(f"Canceled appointment with ID {canceled_appt.appointment_id}")
                    except LookupError:
                        print("That is not a valid appointment ID")
                        print("Please try again")

            elif user_input_num == 5:
                all_practitioners: list[Practitioner] = data_store.list_practitioners()
                all_appointments: list[Appointment] = data_store.list_appointments()

                # Get the practitioner to list for
                practitioner: Practitioner | None = None
                getting_practitioner_name: bool = True
                while getting_practitioner_name:
                    practitioner_name: str = input("\nEnter practitioner name: ").lower()
                
                    if practitioner_name.strip() == "":
                        print("Practitioner name cannot be blank")
                        continue
                
                    lowercase_practitioner_names: list[str] = []
                    for practitioner in all_practitioners:
                        lowercase_practitioner_names.append(practitioner.name.lower())
                
                    any_practitoner_that_starts_with_that_str: bool = False
                    practitioner_index: int = -1
                    for lc_pat_name in lowercase_practitioner_names:
                        if lc_pat_name == practitioner_name:
                            any_practitoner_that_starts_with_that_str = True
                            practitioner_index = lowercase_practitioner_names.index(lc_pat_name)
                            break
                
                    if any_practitoner_that_starts_with_that_str:
                        practitioner = all_practitioners[practitioner_index]
                        getting_practitioner_name = False
                    else:
                        print("There is no practitioner with that name")
                        print("Please try again")

                print(f"\nListing {practitioner.name}\'s appointments:")
                for appt in all_appointments:
                    if appt.practitioner == practitioner:
                        print(f"{all_appointments.index(appt) + 1}:")
                        print(f"\tID #{appt.appointment_id}")
                        print(f"\tPractitioner: {appt.practitioner.name}")
                        print(f"\tPatient: {appt.patient.name}")
                        print()

            elif user_input_num == 6:
                exit = True

            else:
                raise ValueError() # Quick hack for triggering invalid option msg
            
        except ValueError:
            print("That is not a valid option.\nPlease try again.")

        
        
        

    # Print exit message
    print()
    print("#################### - SMARTCARE - ####################")
    print("  Thank you for using the SmartCare Hospital Interface ")
    print("                        Goodbye!                       ")
    print("#################### - SMARTCARE - ####################")


def random_id() -> str:
    return str(int((random.randint(1, 10 ** 4) + random.randint(1, 10 ** 4)) / 2))
