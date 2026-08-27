# Hotel Management System

A DEPI Python OOP & Modules group project.

## Problem Description

A small hotel needs an internal tool (no database, no GUI, no web framework) to manage
its guests, employees, and rooms, to create and cancel reservations, and to calculate
the cost of a stay and record payments made by guests.

## Team Members

## Team Members

| #   | Name            | Role                                                  |
| --- | --------------- | ----------------------------------------------------- |
| 1   | _Noran Alaa_    | Person, Guest, Employee classes (`models.py`)         |
| 2   | _Mariam Shaban_ | Room class (`rooms.py`)                               |
| 3   | _Merna Adel_    | Reservation & Payment classes (`reservations.py`)     |
| 4   | _Islam Mohsen_  | HotelSystem business logic (`hotel.py`)               |
| 5   | _Sama Osama_    | Integration, main.py demo, README, testing edge cases |

## Classes

| Class                          | File              | Description                                                    |
| ------------------------------ | ----------------- | -------------------------------------------------------------- |
| `Person`                       | `models.py`       | Base class for anyone in the system (id, name, contact info).  |
| `Guest` (inherits `Person`)    | `models.py`       | A hotel guest who makes reservations.                          |
| `Employee` (inherits `Person`) | `models.py`       | Hotel staff member with a job position.                        |
| `Room`                         | `rooms.py`        | A hotel room (number, type, price/night, availability).        |
| `Reservation`                  | `reservations.py` | Links a `Guest` to a `Room` for a date range; calculates cost. |
| `Payment`                      | `reservations.py` | Records a payment made against a `Reservation`.                |
| `HotelSystem`                  | `hotel.py`        | Central manager class that owns and coordinates everything.    |

## Modules

- `models.py` — `Person`, `Guest`, `Employee`
- `rooms.py` — `Room`
- `reservations.py` — `Reservation`, `Payment`
- `hotel.py` — `HotelSystem`
- `main.py` — demonstration / test-drive (no `input()` used)

## Relationships

- A `Guest` makes one or more `Reservation`s.
- A `Reservation` is linked to exactly one `Guest` and one `Room`.
- A `Payment` is linked to a `Reservation`.
- An `Employee` is registered with the `HotelSystem`.
- `HotelSystem` owns all `Guest`, `Employee`, `Room`, `Reservation`, and `Payment` objects.

## How to Run

```bash
python3 main.py
```

This runs the full demonstration in `main.py`: it creates guests, employees and rooms,
makes reservations, calculates costs, records a payment, updates data, cancels a
reservation, searches for records, and triggers several validation/edge cases.

## Example Output (excerpt)

```
========== CREATING RESERVATIONS ==========

Reservation created successfully for Guest: Ali Hassan.
Reservation created successfully for Guest: Mona Yousef.

========== RESERVATION COSTS ==========

Total cost for Ali Hassan: 2000 EGP
Total cost for Mona Yousef: 2400 EGP

========== VALIDATION: booking an unavailable room ==========

Room 201 isn't available.
 You can book from these :

----  Available Rooms   ----
Room 202 | Type: Double | Price/Night: 800 | Status: Available
Room 203 | Type: Suite | Price/Night: 1800 | Status: Available
```

## Required System Features — where each one lives

| Feature                    | Method / Action                                  | File                  |
| :------------------------- | :----------------------------------------------- | :-------------------- |
| **Create / Register**      | `addGuest`, `addRoom`, `addEmployee`             | `hotel.py`            |
| **Display**                | `displayAvailableRooms`, `displayReservations`   | `hotel.py`            |
| **Search**                 | `searchGuest`, `searchRoom`                      | `hotel.py`            |
| **Update**                 | `updateGuestContact`, `updateRoomPrice`          | `hotel.py`            |
| **Remove / Delete**        | `cancelReservation`                              | `hotel.py`            |
| **Relationship Operation** | `createReservation`                              | `hotel.py`            |
| **Calculation**            | `calculate_total_price`                          | `reservations.py`     |
| **Validation**             | Booking unavailable rooms, handling missing data | `hotel.py`, `main.py` |

## OOP Concepts Used

- **Classes & Objects** — every entity (`Guest`, `Room`, `Reservation`, ...) is a class.
- **Constructors (`__init__`)** — used to initialize every object's state.
- **Encapsulation** — `Room` and `Payment` keep their core data in "private" (underscore-
  prefixed) attributes and expose them only through getters/setters.
- **Inheritance** — `Guest` and `Employee` both inherit from `Person`.
- **Modules & Imports** — the system is split across `models.py`, `rooms.py`,
  `reservations.py`, and `hotel.py`, all imported into `main.py`.
- **Object collaboration** — `HotelSystem` coordinates `Guest`, `Room`, `Reservation`,
  and `Payment` objects together to implement each feature.

## Notes on Testing / Edge Cases (`main.py`)

- Booking a room that is already booked → shows an error and lists available rooms.
- Cancelling a reservation that was never actually created (rejected at booking time) →
  shows "Reservation not found."
- Updating a room or guest that doesn't exist → shows a clear "not found" message
  instead of crashing.
