"""Simple workflows using a shared SmartCareDataStore object."""


from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
	Appointment,
	AppointmentStatus,
	Patient,
	Practitioner,
)


class PatientService:
	"""Coordinate patient registration and lookup through the shared store."""

	def __init__(self, data_store: SmartCareDataStore) -> None:
		"""Use the shared store to coordinate patient operations."""
		self.data_store = data_store

	def register_patient(self, patient_id: str, name: str) -> Patient:
		"""Validate and register a patient, returning the stored object.

		Raise ValueError for invalid fields or an existing patient ID.
		"""
		patient = Patient(patient_id, name)
		self.data_store.add_patient(patient)
		return patient

	def find_patient(self, patient_id: str) -> Patient:
		"""Return the stored patient for a valid patient ID.

		Raise LookupError for absence and ValueError for
		a blank/invalid ID.
		"""

		if len(patient_id) == 0 or type(patient_id) is not str:
			raise ValueError('Patient ID is blank or invalid')
		
		patient = self.data_store.find_patient(patient_id)
		if patient is None:
			raise LookupError(f'Patient with ID \'{patient_id}\' could not be found')
		return patient


class PractitionerService:
	"""Coordinate practitioner registration and lookup through the shared
	store.
	"""

	def __init__(self, data_store: SmartCareDataStore) -> None:
		"""Use the shared store to coordinate practitioner operations."""
		self.data_store = data_store

	def register_practitioner(
		self,
		practitioner_id: str,
		name: str,
		specialty: str,
	) -> Practitioner:
		"""Validate and register a practitioner, returning the stored
		object.

		Raise ValueError for invalid fields or an existing practitioner
		ID.
		"""
		practitioner = Practitioner(practitioner_id, name, specialty)
		self.data_store.add_practitioner(practitioner)
		return practitioner

	def find_practitioner(self, practitioner_id: str) -> Practitioner:
		"""Return the stored practitioner for a valid ID.

		Raise LookupError for absence and ValueError for
		a blank/invalid ID.
		"""

		if len(practitioner_id) == 0 or type(practitioner_id) is not str:
			raise ValueError('Practitioner ID is blank or invalid')
		
		practitioner = self.data_store.find_practitioner(practitioner_id)
		if practitioner is None:
			raise LookupError(f'Practitioner with ID \'{practitioner_id}\' could not be found')
		return practitioner


class AppointmentService:
	"""Coordinate booking, lookup and cancellation using the shared store."""

	def __init__(self, data_store: SmartCareDataStore) -> None:
		"""Use the shared store to coordinate appointment operations."""
		self.data_store = data_store
		self.cancelled_appointments: list[Appointment] = []

	def book_appointment(
		self,
		appointment_id: str,
		patient_id: str,
		practitioner_id: str,
		date_time: datetime,
	) -> Appointment:
		"""Book registered participant IDs and return the stored
		appointment.

		Raise LookupError for absent participants. Raise ValueError for
		invalid values, duplicate appointment IDs or a practitioner
		conflict.
		"""
		patient = self.data_store.find_patient(patient_id)
		practitioner = self.data_store.find_practitioner(practitioner_id)
		if patient is None:
			raise LookupError('Patient not found')
		if practitioner is None:
			raise LookupError('Practitioner not found')
		appointment = Appointment(
			appointment_id,
			patient,
			practitioner,
			date_time,
		)
		if self.data_store.find_appointment(
			appointment.appointment_id,
		) is not None:
			raise ValueError('Appointment ID already exists')
		if self.data_store.has_practitioner_conflict(
			practitioner.practitioner_id,
			date_time,
		):
			raise ValueError(
				'Practitioner already has a SCHEDULED appointment at this time',
			)
		self.data_store.add_appointment(appointment)
		return appointment

	def find_appointment(self, appointment_id: str) -> Appointment:
		"""Return the stored appointment; raise LookupError when absent.

		Reject a blank or invalid ID with ValueError; do not create
		records.
		"""
		appointment = self.data_store.find_appointment(appointment_id)
		if appointment is None:
			raise LookupError('Appointment not found')
		return appointment

	def cancel_appointment(self, appointment_id: str) -> Appointment:
		"""Cancels the appointment matching the given ID,
		stores the canceled appointment and
		returns the cancelled appointment.

		Unknown IDs raise LookupError and
		invalid transitions raise ValueError and leave state unchanged.
		"""

		appointment: Appointment | None = self.data_store.find_appointment(appointment_id)
		if appointment is None:
			raise LookupError(f'Appointment with ID \'{appointment_id}\' could not be found')

		# This already raises a ValueError if trying to cancel an already cancelled appointment
		appointment.cancel()

		# Remove the appointment from the booked appointments lists
		self.data_store._appointments.__delitem__(appointment_id)

		# Add the appointment to the canceled appointments list
		self.cancelled_appointments.append(appointment)
		
		return appointment

	def list_practitioner_appointments(
		self,
		practitioner_id: str,
		status: AppointmentStatus | None = None,
	) -> list[Appointment]:
		"""New ordered list; default includes every status.

		Unknown practitioner raises LookupError, invalid status
		ValueError; a known practitioner with no matches returns an
		empty list.
		"""
		
		# Step 1. Find the practitioner
		practitioner: Practitioner | None = self.data_store.find_practitioner(practitioner_id)
		# Not being able to find them throws a LookupError
		if practitioner is None:
			raise LookupError(f"Practitioner with ID \'{practitioner_id}\' could not be found")

		# Step 2. Filter appointment list
		practitioner_appointments: list[Appointment] = []
		for appointment in self.data_store.list_appointments():
			if appointment.practitioner.practitioner_id == practitioner_id:
				practitioner_appointments.append(appointment)

		# Step 3. If given, further filter appointments by status
		if status is not None:
			if status not in list(AppointmentStatus):
				raise ValueError(f"\'status\' is not a valid status")

			# Filter method is used because we do not want to create another list
			practitioner_appointments = [appt for appt in practitioner_appointments if appt.status == status]
		
		return practitioner_appointments
