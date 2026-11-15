# Use-Case Flow Specification

## UC-01: Vehicle Entry and Reservation Validation

### Primary Actor
Vehicle Owner

### Supporting Actor
Gate Camera / License Plate Scanner

### Goal
Allow a vehicle to enter the parking facility only when it has a valid parking reservation.

## Preconditions

1. The vehicle has reached the parking entrance.
2. The gate camera/license plate scanner is operational.
3. The parking system can access reservation information.
4. The vehicle owner has a parking reservation.

## Postconditions

### Success

1. The vehicle number plate is recorded.
2. The reservation is successfully validated.
3. The vehicle's entry time is recorded.
4. The reservation is marked as checked-in.
5. The vehicle is allowed to enter the parking facility.

### Failure

1. The vehicle is denied entry if the reservation is invalid or expired.
2. The failed entry attempt is recorded.
3. The parking warden can be notified for manual verification.

## Main Success Scenario

1. The vehicle owner arrives at the parking entrance.
2. The gate camera scans the vehicle's license plate.
3. The system extracts the vehicle registration number.
4. The system searches for the corresponding parking reservation.
5. The system checks the reservation status and validity.
6. The system confirms that the reservation is valid.
7. The system records the vehicle's entry time.
8. The system marks the reservation as checked-in.
9. The entrance gate opens.
10. The vehicle owner enters the parking facility.

## Alternate Flow – Invalid or Expired Reservation

1. The gate camera scans the vehicle's license plate.
2. The system searches for the corresponding reservation.
3. The system finds that the reservation is invalid, expired, or unavailable.
4. The system denies vehicle entry.
5. The system displays an appropriate error message.
6. The failed entry attempt is recorded.
7. The parking warden is notified if manual verification is required.
