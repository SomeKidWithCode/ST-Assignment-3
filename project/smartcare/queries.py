"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    return (appointment.date_time, appointment.appointment_id)


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """

    # Same practitioner and status filter system as used by AppointmentService's list_practitioner_appointments method
    # (Minus checks)

    # Stage 1. Get list of appointments for this practitioner
    practitioner_appointments: list[Appointment] = []
    for appointment in appointments:
        if appointment.practitioner.practitioner_id == practitioner_id:
            practitioner_appointments.append(appointment)

    # Stage 2. Sort appointments using appointment_sort_key
    sorted_practitioner_appointments: list[Appointment] = sorted(practitioner_appointments, key=appointment_sort_key)

    # Stage 3. Further filter by status if present
    if status is not None:
        # Filter method is used because we do not want to create another list
        sorted_practitioner_appointments = [appt for appt in sorted_practitioner_appointments if appt.status == status]

    return sorted_practitioner_appointments
